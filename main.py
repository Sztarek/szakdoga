import sys
import getopt
from transformers import AutoTokenizer
from datasets import load_dataset
from tqdm.auto import tqdm
from transformers import AdamW
from torch.utils.data import DataLoader
from transformers import get_scheduler
from transformers import AutoModelForSequenceClassification
from datasets import load_metric
import torch
from transformers.data.data_collator import DataCollatorWithPadding
import re

file_name='out.txt'
checkpoint_base = "bert-base-uncased"
freeze_layer_count = 12

def main(argv):
  layerNum = []
  dbName = []
  try:
    opts, args = getopt.getopt(argv, "hn:l:", ["numberOfLayers=", "learningDatabase="])
  except getopt.GetoptError:
    print('main.py -n <numberOfLayers> -l <learningDatabaseName>')
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print('main.py -n <numberOfLayers> -l <learningDatabaseName>')
      sys.exit()
    elif opt in ("-n", "--numberOfLayers"):
      layerNum.append(int(arg))
    elif opt in ("-l", "--learningDatabaseName"):
      if(arg not in ['cola', 'rte', 'mrpc']):
        raise Exception('Not supported parameter, use cola, rte or mrpc')
      dbName.append(arg)

  multipleLearn(generateParameters(dbName, layerNum))


def multipleLearn(params):
  for param in params:
    print('Started learing with following parameters: ', param)
    modelName = re.sub("\(|\)|\[|\]|,|\'", '', str(param).replace(', ', '_'))
    print('Name of the model is: ' + modelName)
    for db in param[0]:
      learn(db, param[1], modelName, param[0].index(db))
      print('Finished learning with database: ', db)
      print('Frozed layer count: ', param[1])
    print('Finished learning with following parameters: ', param)
    print('Saved results in: ', file_name)


def generateParameters(dbName, freeze_layer_count):
  dbPermutations = permutations(dbName)
  result = []
  for db in dbPermutations:
    for layer_count in freeze_layer_count:
      result.append([db, layer_count])
  return result

def permutations(iterable, r=None):
  pool = tuple(iterable)
  n = len(pool)
  r = n if r is None else r
  if r > n:
    return
  indices = list(range(n))
  cycles = list(range(n, n - r, -1))
  yield tuple(pool[i] for i in indices[:r])
  while n:
    for i in reversed(range(r)):
      cycles[i] -= 1
      if cycles[i] == 0:
        indices[i:] = indices[i + 1:] + indices[i:i + 1]
        cycles[i] = n - i
      else:
        j = cycles[i]
        indices[i], indices[-j] = indices[-j], indices[i]
        yield tuple(pool[i] for i in indices[:r])
        break
    else:
      return


def preprocess(dbName):
  if(dbName == 'cola'):
    return preprocessCola()
  elif(dbName == 'rte'):
    return preprocessRTE()
  elif(dbName == 'mrpc'):
    return preprocessMRPC()
  else:
    raise Exception('Not supported parameter, use sst2, rte or mrpc')

def learn(dbName, freeze_layer_count, model_name, numInIteration):
  checkpoint = './models/'+model_name
  if numInIteration == 0:
    checkpoint = checkpoint_base
  result = preprocess(dbName)
  tokenized_datasets = result[0]
  data_collator = result[1]

  train_dataloader = DataLoader(
    tokenized_datasets["train"], shuffle=True, batch_size=1, collate_fn=data_collator
  )
  eval_dataloader = DataLoader(
    tokenized_datasets["validation"], batch_size=1, collate_fn=data_collator
  )

  model = AutoModelForSequenceClassification.from_pretrained(checkpoint, num_labels=2)
  optimizer = AdamW(model.parameters(), lr=5e-5)

  num_epochs = 3
  num_training_steps = num_epochs * len(train_dataloader)
  lr_scheduler = get_scheduler(
    "linear",
    optimizer=optimizer,
    num_warmup_steps=0,
    num_training_steps=num_training_steps,
  )

  device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
  model.to(device)
  model.half()
  print(device)

  progress_bar = tqdm(range(num_training_steps))
  for layer in model.bert.encoder.layer[:freeze_layer_count]:
    for param in layer.parameters():
      param.requires_grad = False
  model.train()
  for epoch in range(num_epochs):
    for batch in train_dataloader:
      batch = {k: v.to(device) for k, v in batch.items()}
      outputs = model(**batch)
      loss = outputs.loss
      loss.backward()

      optimizer.step()
      lr_scheduler.step()
      optimizer.zero_grad()
      progress_bar.update(1)

  eval(model, eval_dataloader, device, model_name, numInIteration)


#rte, sst, mrpc
def preprocessMRPC():
  raw_datasets = load_dataset("glue", 'mrpc')
  checkpoint = "bert-base-uncased"
  tokenizer = AutoTokenizer.from_pretrained(checkpoint)

  def tokenize_function(example):
    return tokenizer(example["sentence1"], example["sentence2"], truncation=True)

  tokenized_datasets = raw_datasets.map(tokenize_function, batched=True)
  data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

  tokenized_datasets = tokenized_datasets.remove_columns(["sentence1", "sentence2", "idx"])
  tokenized_datasets = tokenized_datasets.rename_column("label", "labels")
  tokenized_datasets.set_format("torch")

  return [tokenized_datasets, data_collator]

def preprocessRTE():
  raw_datasets = load_dataset("glue", 'rte')
  checkpoint = "bert-base-uncased"
  tokenizer = AutoTokenizer.from_pretrained(checkpoint)

  def tokenize_function(example):
    return tokenizer(example["sentence1"], example["sentence2"], truncation=True)

  tokenized_datasets = raw_datasets.map(tokenize_function, batched=True)
  data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

  tokenized_datasets = tokenized_datasets.remove_columns(["sentence1", "sentence2", "idx"])
  tokenized_datasets = tokenized_datasets.rename_column("label", "labels")
  tokenized_datasets.set_format("torch")

  return [tokenized_datasets, data_collator]

def preprocessCola():
  raw_datasets = load_dataset("glue", 'cola')
  checkpoint = "bert-base-uncased"
  tokenizer = AutoTokenizer.from_pretrained(checkpoint)

  def tokenize_function(example):
    return tokenizer(example["sentence"], truncation=True)

  tokenized_datasets = raw_datasets.map(tokenize_function, batched=True)
  tokenized_datasets = tokenized_datasets.remove_columns(["sentence", "idx"])
  tokenized_datasets = tokenized_datasets.rename_column("label", "labels")
  data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
  tokenized_datasets.set_format("torch")

  return [tokenized_datasets, data_collator]

def eval(model, eval_dataloader, device, model_name, numInIteration):
  model.save_pretrained('./models/'+model_name)
  f = open(file_name, "a")
  f.write(model_name + ' - ' + str(numInIteration) + ':\n')
  for metricName in ["sst2", "mnli", "mnli_mismatched", "mnli_matched", "cola", "stsb", "mrpc", "qqp", "qnli", "rte", "wnli", "hans"]:
    metric = load_metric('glue', metricName)
    for batch in eval_dataloader:
      batch = {k: v.to(device) for k, v in batch.items()}
      with torch.no_grad():
        outputs = model(**batch)

      logits = outputs.logits
      predictions = torch.argmax(logits, dim=-1)
      metric.add_batch(predictions=predictions, references=batch["labels"])

    f.write(metricName + ": " + str(metric.compute()) + '\n')
  f.write('\n')
  f.close()


if __name__ == "__main__":
  main(sys.argv[1:])
