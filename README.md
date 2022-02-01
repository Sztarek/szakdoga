This project is a command line program which is used to test for catastrophic forgetting.

**Usage**:

- Run the main file
- Use parameter `-l` for giving the name of the database, multiple can be used at once
- When using multiple `-l` parameters, it will go through all possible iterations of the given databases
- Use parameter `-n` for giving the number of layer that you wish to freeze during the learning process
- Multiple `-n` parameters can be used, it will go through the learning process with each `-n` parameter given
- Models are saved in the `/models/model_name` folder
- It creates a .txt file which contains the evaluated results of given models
- The default name of the .txt is `out.txt`


**Results**

cola_rte_mrpc_0 - 0:

sst2: {'accuracy': 0.6912751677852349}  
mnli: {'accuracy': 0.6912751677852349}  
mnli_mismatched: {'accuracy': 0.6912751677852349}  
mnli_matched: {'accuracy': 0.6912751677852349}  
cola: {'matthews_correlation': 0.0}  
stsb: {'pearson': nan, 'spearmanr': nan}  
mrpc: {'accuracy': 0.6903163950143816, 'f1': 0.8167895632444696}  
qqp: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qnli: {'accuracy': 0.6912751677852349}  
rte: {'accuracy': 0.6912751677852349}  
wnli: {'accuracy': 0.6912751677852349}  
hans: {'accuracy': 0.6912751677852349}  

cola_rte_mrpc_0 - 1:

sst2: {'accuracy': 0.49458483754512633}  
mnli: {'accuracy': 0.5523465703971119}  
mnli_mismatched: {'accuracy': 0.5090252707581228}  
mnli_matched: {'accuracy': 0.5054151624548736}  
cola: {'matthews_correlation': 0.020497029939120007}  
stsb: {'pearson': -0.00934439887803606, 'spearmanr': -0.009344398878036071}  
mrpc: {'accuracy': 0.592057761732852, 'f1': 0.5425101214574899}  
qqp: {'accuracy': 0.48375451263537905, 'f1': 0.45627376425855515}  
qnli: {'accuracy': 0.49458483754512633}  
rte: {'accuracy': 0.51985559566787}  
wnli: {'accuracy': 0.4981949458483754}  
hans: {'accuracy': 0.555956678700361}  

cola_rte_mrpc_0 - 2:

sst2: {'accuracy': 0.6813725490196079}  
mnli: {'accuracy': 0.6813725490196079}  
mnli_mismatched: {'accuracy': 0.678921568627451}  
mnli_matched: {'accuracy': 0.6862745098039216}  
cola: {'matthews_correlation': -0.03370509448285096}  
stsb: {'pearson': 0.07289706481174736, 'spearmanr': 0.07289706481174744}  
mrpc: {'accuracy': 0.6838235294117647, 'f1': 0.8122270742358079}  
qqp: {'accuracy': 0.6838235294117647, 'f1': 0.8122270742358079}  
qnli: {'accuracy': 0.6838235294117647}  
rte: {'accuracy': 0.6838235294117647}  
wnli: {'accuracy': 0.6838235294117647}  
hans: {'accuracy': 0.6838235294117647}  

cola_mrpc_rte_0 - 0:

sst2: {'accuracy': 0.6912751677852349}  
mnli: {'accuracy': 0.6903163950143816}  
mnli_mismatched: {'accuracy': 0.6912751677852349}  
mnli_matched: {'accuracy': 0.6912751677852349}  
cola: {'matthews_correlation': -0.020702674026557004}  
stsb: {'pearson': nan, 'spearmanr': nan}  
mrpc: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qqp: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qnli: {'accuracy': 0.6912751677852349}  
rte: {'accuracy': 0.6912751677852349}  
wnli: {'accuracy': 0.6912751677852349}  
hans: {'accuracy': 0.6893576222435283}  

cola_mrpc_rte_0 - 1:

sst2: {'accuracy': 0.6838235294117647}  
mnli: {'accuracy': 0.6862745098039216}  
mnli_mismatched: {'accuracy': 0.6838235294117647}  
mnli_matched: {'accuracy': 0.6838235294117647}  
cola: {'matthews_correlation': 0.07289706481174742}  
stsb: {'pearson': 0.07289706481174739, 'spearmanr': 0.07289706481174744}  
mrpc: {'accuracy': 0.678921568627451, 'f1': 0.8087591240875913}  
qqp: {'accuracy': 0.6813725490196079, 'f1': 0.8104956268221574}  
qnli: {'accuracy': 0.6838235294117647}  
rte: {'accuracy': 0.6838235294117647}  
wnli: {'accuracy': 0.6838235294117647}  
hans: {'accuracy': 0.6838235294117647}  

cola_mrpc_rte_0 - 2:

sst2: {'accuracy': 0.51985559566787}  
mnli: {'accuracy': 0.51985559566787}  
mnli_mismatched: {'accuracy': 0.47653429602888087}  
mnli_matched: {'accuracy': 0.49097472924187724}  
cola: {'matthews_correlation': 0.013010087122651923}  
stsb: {'pearson': -0.014600455827460538, 'spearmanr': -0.014600455827460546}  
mrpc: {'accuracy': 0.5234657039711191, 'f1': 0.5074626865671642}  
qqp: {'accuracy': 0.5415162454873647, 'f1': 0.5313653136531366}  
qnli: {'accuracy': 0.47653429602888087}  
rte: {'accuracy': 0.5306859205776173}  
wnli: {'accuracy': 0.5451263537906137}  
hans: {'accuracy': 0.5306859205776173}  

rte_cola_mrpc_0 - 0:

sst2: {'accuracy': 0.5090252707581228}  
mnli: {'accuracy': 0.4693140794223827}  
mnli_mismatched: {'accuracy': 0.5306859205776173}  
mnli_matched: {'accuracy': 0.5090252707581228}  
cola: {'matthews_correlation': 0.1022058430173232}  
stsb: {'pearson': -0.027249166381744728, 'spearmanr': -0.027249166381744672}  
mrpc: {'accuracy': 0.516245487364621, 'f1': 0.3909090909090909}  
qqp: {'accuracy': 0.51985559566787, 'f1': 0.43881856540084385}  
qnli: {'accuracy': 0.48014440433212996}  
rte: {'accuracy': 0.5379061371841155}  
wnli: {'accuracy': 0.47653429602888087}  
hans: {'accuracy': 0.4981949458483754}  

rte_cola_mrpc_0 - 1:

sst2: {'accuracy': 0.6912751677852349}  
mnli: {'accuracy': 0.6893576222435283}  
mnli_mismatched: {'accuracy': 0.6903163950143816}  
mnli_matched: {'accuracy': 0.6912751677852349}  
cola: {'matthews_correlation': 0.0}  
stsb: {'pearson': nan, 'spearmanr': nan}  
mrpc: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qqp: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qnli: {'accuracy': 0.6912751677852349}  
rte: {'accuracy': 0.6903163950143816}  
wnli: {'accuracy': 0.6912751677852349}  
hans: {'accuracy': 0.6912751677852349}  

rte_cola_mrpc_0 - 2:

sst2: {'accuracy': 0.6838235294117647}  
mnli: {'accuracy': 0.6838235294117647}  
mnli_mismatched: {'accuracy': 0.6838235294117647}  
mnli_matched: {'accuracy': 0.6813725490196079}  
cola: {'matthews_correlation': 0.027747016194979744}  
stsb: {'pearson': nan, 'spearmanr': nan}  
mrpc: {'accuracy': 0.6813725490196079, 'f1': 0.8104956268221574}  
qqp: {'accuracy': 0.6813725490196079, 'f1': 0.8104956268221574}  
qnli: {'accuracy': 0.6838235294117647}  
rte: {'accuracy': 0.6838235294117647}  
wnli: {'accuracy': 0.6838235294117647}  
hans: {'accuracy': 0.6838235294117647}  

rte_mrpc_cola_0 - 0:

sst2: {'accuracy': 0.48736462093862815}  
mnli: {'accuracy': 0.49458483754512633}  
mnli_mismatched: {'accuracy': 0.4657039711191336}  
mnli_matched: {'accuracy': 0.4981949458483754}  
cola: {'matthews_correlation': -0.015162605876816898}  
stsb: {'pearson': -0.02225249618744217, 'spearmanr': -0.022252496187442163}  
mrpc: {'accuracy': 0.48375451263537905, 'f1': 0.46037735849056605}  
qqp: {'accuracy': 0.45126353790613716, 'f1': 0.45714285714285713}  
qnli: {'accuracy': 0.5379061371841155}  
rte: {'accuracy': 0.48736462093862815}  
wnli: {'accuracy': 0.5054151624548736}  
hans: {'accuracy': 0.4620938628158845}  

rte_mrpc_cola_0 - 1:

sst2: {'accuracy': 0.6838235294117647}  
mnli: {'accuracy': 0.6838235294117647}  
mnli_mismatched: {'accuracy': 0.6838235294117647}  
mnli_matched: {'accuracy': 0.6838235294117647}  
cola: {'matthews_correlation': 0.0}  
stsb: {'pearson': nan, 'spearmanr': nan}  
mrpc: {'accuracy': 0.6838235294117647, 'f1': 0.8122270742358079}  
qqp: {'accuracy': 0.6838235294117647, 'f1': 0.8122270742358079}  
qnli: {'accuracy': 0.6838235294117647}  
rte: {'accuracy': 0.6838235294117647}  
wnli: {'accuracy': 0.6862745098039216}  
hans: {'accuracy': 0.6813725490196079}  

rte_mrpc_cola_0 - 2:

sst2: {'accuracy': 0.6912751677852349}  
mnli: {'accuracy': 0.6912751677852349}  
mnli_mismatched: {'accuracy': 0.6912751677852349}  
mnli_matched: {'accuracy': 0.6912751677852349}  
cola: {'matthews_correlation': 0.0}  
stsb: {'pearson': nan, 'spearmanr': nan}  
mrpc: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qqp: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qnli: {'accuracy': 0.6912751677852349}  
rte: {'accuracy': 0.6912751677852349}  
wnli: {'accuracy': 0.6903163950143816}  
hans: {'accuracy': 0.6912751677852349}  

mrpc_cola_rte_0 - 0:

sst2: {'accuracy': 0.6813725490196079}  
mnli: {'accuracy': 0.6813725490196079}  
mnli_mismatched: {'accuracy': 0.6887254901960784}  
mnli_matched: {'accuracy': 0.6862745098039216}  
cola: {'matthews_correlation': -0.05852290412010273}  
stsb: {'pearson': -0.03370509448285092, 'spearmanr': -0.03370509448285096}  
mrpc: {'accuracy': 0.6862745098039216, 'f1': 0.8134110787172011}  
qqp: {'accuracy': 0.6862745098039216, 'f1': 0.8134110787172011}  
qnli: {'accuracy': 0.678921568627451}  
rte: {'accuracy': 0.6838235294117647}  
wnli: {'accuracy': 0.6838235294117647}  
hans: {'accuracy': 0.6838235294117647}  

mrpc_cola_rte_0 - 1:

sst2: {'accuracy': 0.6912751677852349}  
mnli: {'accuracy': 0.6912751677852349}  
mnli_mismatched: {'accuracy': 0.6912751677852349}  
mnli_matched: {'accuracy': 0.6912751677852349}  
cola: {'matthews_correlation': 0.0}  
stsb: {'pearson': -0.020702674026557004, 'spearmanr': -0.020702674026557004}  
mrpc: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qqp: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qnli: {'accuracy': 0.6912751677852349}  
rte: {'accuracy': 0.6912751677852349}  
wnli: {'accuracy': 0.6912751677852349}  
hans: {'accuracy': 0.6912751677852349}  

mrpc_cola_rte_0 - 2:

sst2: {'accuracy': 0.48014440433212996}  
mnli: {'accuracy': 0.49097472924187724}  
mnli_mismatched: {'accuracy': 0.49458483754512633}  
mnli_matched: {'accuracy': 0.5126353790613718}  
cola: {'matthews_correlation': 0.07237430254257324}  
stsb: {'pearson': -0.050999062943980204, 'spearmanr': -0.05099906294398018}  
mrpc: {'accuracy': 0.5703971119133574, 'f1': 0.5475285171102661}  
qqp: {'accuracy': 0.4729241877256318, 'f1': 0.44274809160305345}  
qnli: {'accuracy': 0.4981949458483754}  
rte: {'accuracy': 0.4981949458483754}  
wnli: {'accuracy': 0.4729241877256318}  
hans: {'accuracy': 0.49458483754512633}  

mrpc_rte_cola_0 - 0:

sst2: {'accuracy': 0.6764705882352942}  
mnli: {'accuracy': 0.6838235294117647}  
mnli_mismatched: {'accuracy': 0.6838235294117647}  
mnli_matched: {'accuracy': 0.6838235294117647}  
cola: {'matthews_correlation': 0.0}  
stsb: {'pearson': -0.04772486785536518, 'spearmanr': -0.04772486785536515}  
mrpc: {'accuracy': 0.6813725490196079, 'f1': 0.8104956268221574}  
qqp: {'accuracy': 0.6813725490196079, 'f1': 0.8104956268221574}  
qnli: {'accuracy': 0.6813725490196079}  
rte: {'accuracy': 0.6838235294117647}  
wnli: {'accuracy': 0.6813725490196079}  
hans: {'accuracy': 0.6838235294117647}  

mrpc_rte_cola_0 - 1:

sst2: {'accuracy': 0.5126353790613718}  
mnli: {'accuracy': 0.5487364620938628}  
mnli_mismatched: {'accuracy': 0.4729241877256318}  
mnli_matched: {'accuracy': 0.5342960288808665}  
cola: {'matthews_correlation': 0.03195325056656263}  
stsb: {'pearson': -0.08374675475288638, 'spearmanr': -0.08374675475288638}  
mrpc: {'accuracy': 0.5270758122743683, 'f1': 0.5304659498207885}  
qqp: {'accuracy': 0.5054151624548736, 'f1': 0.5054151624548736}  
qnli: {'accuracy': 0.5451263537906137}  
rte: {'accuracy': 0.4729241877256318}  
wnli: {'accuracy': 0.5306859205776173}  
hans: {'accuracy': 0.47653429602888087}  

mrpc_rte_cola_0 - 2:

sst2: {'accuracy': 0.6912751677852349}  
mnli: {'accuracy': 0.6922339405560882}  
mnli_mismatched: {'accuracy': 0.6912751677852349}  
mnli_matched: {'accuracy': 0.6912751677852349}  
cola: {'matthews_correlation': 0.0}  
stsb: {'pearson': nan, 'spearmanr': nan}  
mrpc: {'accuracy': 0.6922339405560882, 'f1': 0.8179239931934204}  
qqp: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qnli: {'accuracy': 0.6912751677852349}  
rte: {'accuracy': 0.6912751677852349}  
wnli: {'accuracy': 0.6922339405560882}  
hans: {'accuracy': 0.6912751677852349}  

cola_rte_mrpc_2 - 0:

sst2: {'accuracy': 0.6912751677852349}  
mnli: {'accuracy': 0.6912751677852349}  
mnli_mismatched: {'accuracy': 0.6912751677852349}  
mnli_matched: {'accuracy': 0.6912751677852349}  
cola: {'matthews_correlation': 0.0}  
stsb: {'pearson': nan, 'spearmanr': nan}  
mrpc: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qqp: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qnli: {'accuracy': 0.6912751677852349}  
rte: {'accuracy': 0.6903163950143816}  
wnli: {'accuracy': 0.6912751677852349}  
hans: {'accuracy': 0.6912751677852349}  

cola_rte_mrpc_2 - 1:

sst2: {'accuracy': 0.5018050541516246}  
mnli: {'accuracy': 0.49458483754512633}  
mnli_mismatched: {'accuracy': 0.49097472924187724}  
mnli_matched: {'accuracy': 0.5090252707581228}  
cola: {'matthews_correlation': -0.020748300999891413}  
stsb: {'pearson': -0.07816498104330846, 'spearmanr': -0.07816498104330842}  
mrpc: {'accuracy': 0.4584837545126354, 'f1': 0.489795918367347}  
qqp: {'accuracy': 0.5090252707581228, 'f1': 0.5310344827586206}  
qnli: {'accuracy': 0.516245487364621}  
rte: {'accuracy': 0.516245487364621}  
wnli: {'accuracy': 0.516245487364621}  
hans: {'accuracy': 0.5090252707581228}  

cola_rte_mrpc_2 - 2:

sst2: {'accuracy': 0.6838235294117647}  
mnli: {'accuracy': 0.6813725490196079}  
mnli_mismatched: {'accuracy': 0.6838235294117647}  
mnli_matched: {'accuracy': 0.6838235294117647}  
cola: {'matthews_correlation': 0.0}  
stsb: {'pearson': nan, 'spearmanr': nan}  
mrpc: {'accuracy': 0.6838235294117647, 'f1': 0.8122270742358079}  
qqp: {'accuracy': 0.6838235294117647, 'f1': 0.8122270742358079}  
qnli: {'accuracy': 0.6813725490196079}  
rte: {'accuracy': 0.6838235294117647}  
wnli: {'accuracy': 0.6838235294117647}  
hans: {'accuracy': 0.6838235294117647}  

cola_mrpc_rte_2 - 0:

sst2: {'accuracy': 0.6912751677852349}  
mnli: {'accuracy': 0.6912751677852349}  
mnli_mismatched: {'accuracy': 0.6912751677852349}  
mnli_matched: {'accuracy': 0.6912751677852349}  
cola: {'matthews_correlation': 0.0}  
stsb: {'pearson': nan, 'spearmanr': nan}  
mrpc: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qqp: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qnli: {'accuracy': 0.6912751677852349}  
rte: {'accuracy': 0.6922339405560882}  
wnli: {'accuracy': 0.6912751677852349}  
hans: {'accuracy': 0.6912751677852349}  

cola_mrpc_rte_2 - 1:

sst2: {'accuracy': 0.6813725490196079}  
mnli: {'accuracy': 0.6838235294117647}  
mnli_mismatched: {'accuracy': 0.6838235294117647}  
mnli_matched: {'accuracy': 0.6838235294117647}  
cola: {'matthews_correlation': 0.0}  
stsb: {'pearson': nan, 'spearmanr': nan}  
mrpc: {'accuracy': 0.6838235294117647, 'f1': 0.8122270742358079}  
qqp: {'accuracy': 0.6838235294117647, 'f1': 0.8122270742358079}  
qnli: {'accuracy': 0.6838235294117647}  
rte: {'accuracy': 0.6813725490196079}  
wnli: {'accuracy': 0.6838235294117647}  
hans: {'accuracy': 0.6838235294117647}  

cola_mrpc_rte_2 - 2:

sst2: {'accuracy': 0.49458483754512633}  
mnli: {'accuracy': 0.516245487364621}  
mnli_mismatched: {'accuracy': 0.48375451263537905}  
mnli_matched: {'accuracy': 0.5379061371841155}  
cola: {'matthews_correlation': -0.0810750160464632}  
stsb: {'pearson': 0.0606889200774002, 'spearmanr': 0.060688920077400274}  
mrpc: {'accuracy': 0.5126353790613718, 'f1': 0.46215139442231074}  
qqp: {'accuracy': 0.48736462093862815, 'f1': 0.4409448818897637}  
qnli: {'accuracy': 0.516245487364621}  
rte: {'accuracy': 0.5018050541516246}  
wnli: {'accuracy': 0.5234657039711191}  
hans: {'accuracy': 0.48014440433212996}  

rte_cola_mrpc_2 - 0:

sst2: {'accuracy': 0.4693140794223827}  
mnli: {'accuracy': 0.49458483754512633}  
mnli_mismatched: {'accuracy': 0.4657039711191336}  
mnli_matched: {'accuracy': 0.4548736462093863}  
cola: {'matthews_correlation': 0.012364774004760288}  
stsb: {'pearson': -0.02852724968206758, 'spearmanr': -0.02852724968206762}  
mrpc: {'accuracy': 0.48014440433212996, 'f1': 0.5294117647058824}  
qqp: {'accuracy': 0.5018050541516246, 'f1': 0.551948051948052}  
qnli: {'accuracy': 0.5306859205776173}  
rte: {'accuracy': 0.48375451263537905}  
wnli: {'accuracy': 0.49458483754512633}  
hans: {'accuracy': 0.5090252707581228}  

rte_cola_mrpc_2 - 1:

sst2: {'accuracy': 0.6903163950143816}  
mnli: {'accuracy': 0.6912751677852349}  
mnli_mismatched: {'accuracy': 0.6912751677852349}  
mnli_matched: {'accuracy': 0.6912751677852349}  
cola: {'matthews_correlation': 0.0}  
stsb: {'pearson': nan, 'spearmanr': nan}  
mrpc: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qqp: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qnli: {'accuracy': 0.6912751677852349}  
rte: {'accuracy': 0.6912751677852349}  
wnli: {'accuracy': 0.6912751677852349}  
hans: {'accuracy': 0.6912751677852349}  

rte_cola_mrpc_2 - 2:

sst2: {'accuracy': 0.678921568627451}  
mnli: {'accuracy': 0.6838235294117647}  
mnli_mismatched: {'accuracy': 0.6838235294117647}  
mnli_matched: {'accuracy': 0.6813725490196079}  
cola: {'matthews_correlation': -0.03370509448285096}  
stsb: {'pearson': nan, 'spearmanr': nan}  
mrpc: {'accuracy': 0.6813725490196079, 'f1': 0.8104956268221574}  
qqp: {'accuracy': 0.6838235294117647, 'f1': 0.8116788321167884}  
qnli: {'accuracy': 0.6838235294117647}  
rte: {'accuracy': 0.6838235294117647}  
wnli: {'accuracy': 0.6838235294117647}  
hans: {'accuracy': 0.6813725490196079}  

rte_mrpc_cola_2 - 0:

sst2: {'accuracy': 0.5451263537906137}  
mnli: {'accuracy': 0.51985559566787}  
mnli_mismatched: {'accuracy': 0.5090252707581228}  
mnli_matched: {'accuracy': 0.48736462093862815}  
cola: {'matthews_correlation': 0.030775175548196775}  
stsb: {'pearson': -0.02148058414987434, 'spearmanr': -0.021480584149874363}  
mrpc: {'accuracy': 0.5270758122743683, 'f1': 0.5676567656765676}  
qqp: {'accuracy': 0.516245487364621, 'f1': 0.5812499999999999}  
qnli: {'accuracy': 0.44404332129963897}  
rte: {'accuracy': 0.4981949458483754}  
wnli: {'accuracy': 0.5054151624548736}  
hans: {'accuracy': 0.47653429602888087}  

rte_mrpc_cola_2 - 1:

sst2: {'accuracy': 0.6838235294117647}  
mnli: {'accuracy': 0.6838235294117647}  
mnli_mismatched: {'accuracy': 0.6813725490196079}  
mnli_matched: {'accuracy': 0.6838235294117647}  
cola: {'matthews_correlation': 0.07289706481174742}  
stsb: {'pearson': nan, 'spearmanr': nan}  
mrpc: {'accuracy': 0.6838235294117647, 'f1': 0.8122270742358079}  
qqp: {'accuracy': 0.6862745098039216, 'f1': 0.8134110787172011}  
qnli: {'accuracy': 0.6838235294117647}  
rte: {'accuracy': 0.6813725490196079}  
wnli: {'accuracy': 0.6862745098039216}  
hans: {'accuracy': 0.6862745098039216}  

rte_mrpc_cola_2 - 2:

sst2: {'accuracy': 0.6922339405560882}  
mnli: {'accuracy': 0.6912751677852349}  
mnli_mismatched: {'accuracy': 0.6912751677852349}  
mnli_matched: {'accuracy': 0.6912751677852349}  
cola: {'matthews_correlation': -0.020702674026557004}  
stsb: {'pearson': 0.046355987494247186, 'spearmanr': 0.04635598749424719}  
mrpc: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qqp: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qnli: {'accuracy': 0.6922339405560882}  
rte: {'accuracy': 0.6903163950143816}  
wnli: {'accuracy': 0.6903163950143816}  
hans: {'accuracy': 0.6912751677852349}  

mrpc_cola_rte_2 - 0:

sst2: {'accuracy': 0.6838235294117647}  
mnli: {'accuracy': 0.6838235294117647}  
mnli_mismatched: {'accuracy': 0.6838235294117647}  
mnli_matched: {'accuracy': 0.6838235294117647}  
cola: {'matthews_correlation': -0.03370509448285096}  
stsb: {'pearson': 0.07289706481174732, 'spearmanr': 0.07289706481174744}  
mrpc: {'accuracy': 0.6838235294117647, 'f1': 0.8116788321167884}  
qqp: {'accuracy': 0.6838235294117647, 'f1': 0.8122270742358079}  
qnli: {'accuracy': 0.6838235294117647}  
rte: {'accuracy': 0.6838235294117647}  
wnli: {'accuracy': 0.6813725490196079}  
hans: {'accuracy': 0.678921568627451}  

mrpc_cola_rte_2 - 1:

sst2: {'accuracy': 0.6912751677852349}  
mnli: {'accuracy': 0.6912751677852349}  
mnli_mismatched: {'accuracy': 0.6912751677852349}  
mnli_matched: {'accuracy': 0.6912751677852349}  
cola: {'matthews_correlation': -0.020702674026557004}  
stsb: {'pearson': -0.020702674026556993, 'spearmanr': -0.020702674026557004}  
mrpc: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qqp: {'accuracy': 0.6893576222435283, 'f1': 0.8161180476730988}  
qnli: {'accuracy': 0.6912751677852349}  
rte: {'accuracy': 0.6903163950143816}  
wnli: {'accuracy': 0.6912751677852349}  
hans: {'accuracy': 0.6912751677852349}  

mrpc_cola_rte_2 - 2:

sst2: {'accuracy': 0.5595667870036101}  
mnli: {'accuracy': 0.48014440433212996}  
mnli_mismatched: {'accuracy': 0.5234657039711191}  
mnli_matched: {'accuracy': 0.516245487364621}  
cola: {'matthews_correlation': -0.10584312710122833}  
stsb: {'pearson': 0.0024692943692118906, 'spearmanr': 0.0024692943692118914}  
mrpc: {'accuracy': 0.5090252707581228, 'f1': 0.5036496350364963}  
qqp: {'accuracy': 0.5234657039711191, 'f1': 0.5416666666666666}  
qnli: {'accuracy': 0.4620938628158845}  
rte: {'accuracy': 0.4729241877256318}  
wnli: {'accuracy': 0.4729241877256318}  
hans: {'accuracy': 0.5451263537906137}  

mrpc_rte_cola_2 - 0:

sst2: {'accuracy': 0.6838235294117647}  
mnli: {'accuracy': 0.6838235294117647}  
mnli_mismatched: {'accuracy': 0.6838235294117647}  
mnli_matched: {'accuracy': 0.6813725490196079}  
cola: {'matthews_correlation': 0.0}  
stsb: {'pearson': 0.07289706481174736, 'spearmanr': 0.07289706481174744}  
mrpc: {'accuracy': 0.6813725490196079, 'f1': 0.8104956268221574}  
qqp: {'accuracy': 0.6813725490196079, 'f1': 0.8104956268221574}  
qnli: {'accuracy': 0.6862745098039216}  
rte: {'accuracy': 0.6838235294117647}  
wnli: {'accuracy': 0.6813725490196079}  
hans: {'accuracy': 0.6838235294117647}  

mrpc_rte_cola_2 - 1:

sst2: {'accuracy': 0.5054151624548736}  
mnli: {'accuracy': 0.4657039711191336}  
mnli_mismatched: {'accuracy': 0.48736462093862815}  
mnli_matched: {'accuracy': 0.49097472924187724}  
cola: {'matthews_correlation': -0.052496889063847384}  
stsb: {'pearson': -0.04047242992097067, 'spearmanr': -0.04047242992097073}  
mrpc: {'accuracy': 0.48736462093862815, 'f1': 0.47407407407407415}  
qqp: {'accuracy': 0.4187725631768953, 'f1': 0.4429065743944637}  
qnli: {'accuracy': 0.5342960288808665}  
rte: {'accuracy': 0.5270758122743683}  
wnli: {'accuracy': 0.5234657039711191}  
hans: {'accuracy': 0.516245487364621}  

mrpc_rte_cola_2 - 2:

sst2: {'accuracy': 0.6912751677852349}  
mnli: {'accuracy': 0.6912751677852349}  
mnli_mismatched: {'accuracy': 0.6922339405560882}  
mnli_matched: {'accuracy': 0.6912751677852349}  
cola: {'matthews_correlation': 0.0}  
stsb: {'pearson': nan, 'spearmanr': nan}  
mrpc: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qqp: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qnli: {'accuracy': 0.6912751677852349}  
rte: {'accuracy': 0.6912751677852349}  
wnli: {'accuracy': 0.6912751677852349}  
hans: {'accuracy': 0.6912751677852349}  

cola_rte_mrpc_4 - 0:

sst2: {'accuracy': 0.6912751677852349}  
mnli: {'accuracy': 0.6912751677852349}  
mnli_mismatched: {'accuracy': 0.6903163950143816}  
mnli_matched: {'accuracy': 0.6922339405560882}  
cola: {'matthews_correlation': 0.0}  
stsb: {'pearson': 0.046355987494247325, 'spearmanr': 0.04635598749424719}  
mrpc: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qqp: {'accuracy': 0.6903163950143816, 'f1': 0.8167895632444696}  
qnli: {'accuracy': 0.6912751677852349}  
rte: {'accuracy': 0.6903163950143816}  
wnli: {'accuracy': 0.6912751677852349}  
hans: {'accuracy': 0.6912751677852349}  

cola_rte_mrpc_4 - 1:

sst2: {'accuracy': 0.516245487364621}  
mnli: {'accuracy': 0.47653429602888087}  
mnli_mismatched: {'accuracy': 0.44404332129963897}  
mnli_matched: {'accuracy': 0.5451263537906137}  
cola: {'matthews_correlation': -0.03675588782019859}  
stsb: {'pearson': -0.04612852034400084, 'spearmanr': -0.04612852034400087}  
mrpc: {'accuracy': 0.49458483754512633, 'f1': 0.4615384615384615}  
qqp: {'accuracy': 0.4729241877256318, 'f1': 0.44274809160305345}  
qnli: {'accuracy': 0.5054151624548736}  
rte: {'accuracy': 0.5451263537906137}  
wnli: {'accuracy': 0.4981949458483754}  
hans: {'accuracy': 0.48736462093862815}  

cola_rte_mrpc_4 - 2:

sst2: {'accuracy': 0.6838235294117647}  
mnli: {'accuracy': 0.6838235294117647}  
mnli_mismatched: {'accuracy': 0.6838235294117647}  
mnli_matched: {'accuracy': 0.6813725490196079}  
cola: {'matthews_correlation': -0.03370509448285096}  
stsb: {'pearson': -0.033705094482850945, 'spearmanr': -0.03370509448285096}  
mrpc: {'accuracy': 0.6838235294117647, 'f1': 0.8122270742358079}  
qqp: {'accuracy': 0.6862745098039216, 'f1': 0.8134110787172011}  
qnli: {'accuracy': 0.6862745098039216}  
rte: {'accuracy': 0.6838235294117647}  
wnli: {'accuracy': 0.6838235294117647}  
hans: {'accuracy': 0.6838235294117647}  

cola_mrpc_rte_4 - 0:

sst2: {'accuracy': 0.6912751677852349}  
mnli: {'accuracy': 0.6912751677852349}  
mnli_mismatched: {'accuracy': 0.6912751677852349}  
mnli_matched: {'accuracy': 0.6912751677852349}  
cola: {'matthews_correlation': 0.0}  
stsb: {'pearson': -0.020702674026557035, 'spearmanr': -0.020702674026557004}  
mrpc: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qqp: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qnli: {'accuracy': 0.6912751677852349}  
rte: {'accuracy': 0.6912751677852349}  
wnli: {'accuracy': 0.6912751677852349}  
hans: {'accuracy': 0.6912751677852349}  

cola_mrpc_rte_4 - 1:

sst2: {'accuracy': 0.6862745098039216}  
mnli: {'accuracy': 0.6838235294117647}  
mnli_mismatched: {'accuracy': 0.6813725490196079}  
mnli_matched: {'accuracy': 0.678921568627451}  
cola: {'matthews_correlation': 0.0}  
stsb: {'pearson': -0.03370509448285092, 'spearmanr': -0.03370509448285096}  
mrpc: {'accuracy': 0.6813725490196079, 'f1': 0.8104956268221574}  
qqp: {'accuracy': 0.6838235294117647, 'f1': 0.8122270742358079}  
qnli: {'accuracy': 0.6813725490196079}  
rte: {'accuracy': 0.6838235294117647}  
wnli: {'accuracy': 0.6813725490196079}  
hans: {'accuracy': 0.6838235294117647}  

cola_mrpc_rte_4 - 2:

sst2: {'accuracy': 0.5234657039711191}  
mnli: {'accuracy': 0.47653429602888087}  
mnli_mismatched: {'accuracy': 0.44765342960288806}  
mnli_matched: {'accuracy': 0.4332129963898917}  
cola: {'matthews_correlation': 0.0061673552447269655}  
stsb: {'pearson': 0.016209499420288258, 'spearmanr': 0.016209499420288265}  
mrpc: {'accuracy': 0.4729241877256318, 'f1': 0.4895104895104895}  
qqp: {'accuracy': 0.48375451263537905, 'f1': 0.4946996466431095}  
qnli: {'accuracy': 0.49458483754512633}  
rte: {'accuracy': 0.5234657039711191}  
wnli: {'accuracy': 0.5054151624548736}  
hans: {'accuracy': 0.47653429602888087}  

rte_cola_mrpc_4 - 0:

sst2: {'accuracy': 0.51985559566787}  
mnli: {'accuracy': 0.5342960288808665}  
mnli_mismatched: {'accuracy': 0.49097472924187724}  
mnli_matched: {'accuracy': 0.5451263537906137}  
cola: {'matthews_correlation': -0.02554990052765577}  
stsb: {'pearson': -0.030740345178928558, 'spearmanr': -0.030740345178928558}  
mrpc: {'accuracy': 0.5415162454873647, 'f1': 0.4940239043824701}  
qqp: {'accuracy': 0.5090252707581228, 'f1': 0.4645669291338582}  
qnli: {'accuracy': 0.5090252707581228}  
rte: {'accuracy': 0.4729241877256318}  
wnli: {'accuracy': 0.4584837545126354}  
hans: {'accuracy': 0.4620938628158845}  

rte_cola_mrpc_4 - 1:

sst2: {'accuracy': 0.6912751677852349}  
mnli: {'accuracy': 0.6912751677852349}  
mnli_mismatched: {'accuracy': 0.6912751677852349}  
mnli_matched: {'accuracy': 0.6912751677852349}  
cola: {'matthews_correlation': 0.0}  
stsb: {'pearson': nan, 'spearmanr': nan}  
mrpc: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qqp: {'accuracy': 0.6893576222435283, 'f1': 0.8161180476730988}  
qnli: {'accuracy': 0.6912751677852349}  
rte: {'accuracy': 0.6903163950143816}  
wnli: {'accuracy': 0.6912751677852349}  
hans: {'accuracy': 0.6912751677852349}  

rte_cola_mrpc_4 - 2:

sst2: {'accuracy': 0.6838235294117647}  
mnli: {'accuracy': 0.6838235294117647}  
mnli_mismatched: {'accuracy': 0.6813725490196079}  
mnli_matched: {'accuracy': 0.6813725490196079}  
cola: {'matthews_correlation': 0.07289706481174742}  
stsb: {'pearson': nan, 'spearmanr': nan}  
mrpc: {'accuracy': 0.6838235294117647, 'f1': 0.8122270742358079}  
qqp: {'accuracy': 0.6838235294117647, 'f1': 0.8116788321167884}  
qnli: {'accuracy': 0.6838235294117647}  
rte: {'accuracy': 0.6813725490196079}  
wnli: {'accuracy': 0.6862745098039216}  
hans: {'accuracy': 0.6813725490196079}  

rte_mrpc_cola_4 - 0:

sst2: {'accuracy': 0.4981949458483754}  
mnli: {'accuracy': 0.5090252707581228}  
mnli_mismatched: {'accuracy': 0.49097472924187724}  
mnli_matched: {'accuracy': 0.49097472924187724}  
cola: {'matthews_correlation': -0.03414031470150926}  
stsb: {'pearson': 0.042769005542193886, 'spearmanr': 0.04276900554219387}  
mrpc: {'accuracy': 0.5306859205776173, 'f1': 0.5149253731343284}  
qqp: {'accuracy': 0.48736462093862815, 'f1': 0.4817518248175182}  
qnli: {'accuracy': 0.51985559566787}  
rte: {'accuracy': 0.5270758122743683}  
wnli: {'accuracy': 0.48375451263537905}  
hans: {'accuracy': 0.4729241877256318}  

rte_mrpc_cola_4 - 1:

sst2: {'accuracy': 0.6862745098039216}  
mnli: {'accuracy': 0.6813725490196079}  
mnli_mismatched: {'accuracy': 0.6838235294117647}  
mnli_matched: {'accuracy': 0.6838235294117647}  
cola: {'matthews_correlation': 0.0}  
stsb: {'pearson': nan, 'spearmanr': nan}  
mrpc: {'accuracy': 0.6838235294117647, 'f1': 0.8116788321167884}  
qqp: {'accuracy': 0.6838235294117647, 'f1': 0.8116788321167884}  
qnli: {'accuracy': 0.6838235294117647}  
rte: {'accuracy': 0.678921568627451}  
wnli: {'accuracy': 0.6838235294117647}  
hans: {'accuracy': 0.6838235294117647}  

rte_mrpc_cola_4 - 2:

sst2: {'accuracy': 0.6912751677852349}  
mnli: {'accuracy': 0.6912751677852349}  
mnli_mismatched: {'accuracy': 0.6912751677852349}  
mnli_matched: {'accuracy': 0.6912751677852349}  
cola: {'matthews_correlation': 0.0463559874942472}  
stsb: {'pearson': nan, 'spearmanr': nan}  
mrpc: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qqp: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qnli: {'accuracy': 0.6912751677852349}  
rte: {'accuracy': 0.6912751677852349}  
wnli: {'accuracy': 0.6912751677852349}  
hans: {'accuracy': 0.6912751677852349}  

mrpc_cola_rte_4 - 0:

sst2: {'accuracy': 0.6813725490196079}  
mnli: {'accuracy': 0.6813725490196079}  
mnli_mismatched: {'accuracy': 0.6862745098039216}  
mnli_matched: {'accuracy': 0.6813725490196079}  
cola: {'matthews_correlation': 0.027747016194979744}  
stsb: {'pearson': -0.04772486785536514, 'spearmanr': -0.04772486785536515}  
mrpc: {'accuracy': 0.6911764705882353, 'f1': 0.8157894736842105}  
qqp: {'accuracy': 0.678921568627451, 'f1': 0.8087591240875913}  
qnli: {'accuracy': 0.6862745098039216}  
rte: {'accuracy': 0.6813725490196079}  
wnli: {'accuracy': 0.6813725490196079}  
hans: {'accuracy': 0.6813725490196079}  

mrpc_cola_rte_4 - 1:

sst2: {'accuracy': 0.6912751677852349}  
mnli: {'accuracy': 0.6912751677852349}  
mnli_mismatched: {'accuracy': 0.6912751677852349}  
mnli_matched: {'accuracy': 0.6903163950143816}  
cola: {'matthews_correlation': 0.0}  
stsb: {'pearson': nan, 'spearmanr': nan}  
mrpc: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qqp: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qnli: {'accuracy': 0.6912751677852349}  
rte: {'accuracy': 0.6912751677852349}  
wnli: {'accuracy': 0.6903163950143816}  
hans: {'accuracy': 0.6912751677852349}  

mrpc_cola_rte_4 - 2:

sst2: {'accuracy': 0.49097472924187724}  
mnli: {'accuracy': 0.48375451263537905}  
mnli_mismatched: {'accuracy': 0.5126353790613718}  
mnli_matched: {'accuracy': 0.5126353790613718}  
cola: {'matthews_correlation': -0.044882188105855425}  
stsb: {'pearson': 0.06245110015444945, 'spearmanr': 0.062451100154449476}  
mrpc: {'accuracy': 0.5090252707581228, 'f1': 0.5}  
qqp: {'accuracy': 0.5090252707581228, 'f1': 0.5142857142857143}  
qnli: {'accuracy': 0.4981949458483754}  
rte: {'accuracy': 0.49097472924187724}  
wnli: {'accuracy': 0.5018050541516246}  
hans: {'accuracy': 0.5342960288808665}  

mrpc_rte_cola_4 - 0:

sst2: {'accuracy': 0.6813725490196079}  
mnli: {'accuracy': 0.6838235294117647}  
mnli_mismatched: {'accuracy': 0.6862745098039216}  
mnli_matched: {'accuracy': 0.6813725490196079}  
cola: {'matthews_correlation': 0.0}  
stsb: {'pearson': -0.033705094482850875, 'spearmanr': -0.03370509448285096}  
mrpc: {'accuracy': 0.6813725490196079, 'f1': 0.8099415204678363}  
qqp: {'accuracy': 0.678921568627451, 'f1': 0.8087591240875913}  
qnli: {'accuracy': 0.6813725490196079}  
rte: {'accuracy': 0.678921568627451}  
wnli: {'accuracy': 0.678921568627451}  
hans: {'accuracy': 0.6813725490196079}  

mrpc_rte_cola_4 - 1:

sst2: {'accuracy': 0.5631768953068592}  
mnli: {'accuracy': 0.516245487364621}  
mnli_mismatched: {'accuracy': 0.49097472924187724}  
mnli_matched: {'accuracy': 0.516245487364621}  
cola: {'matthews_correlation': -0.07048637879448011}  
stsb: {'pearson': 0.02001575567799852, 'spearmanr': 0.020015755677998515}  
mrpc: {'accuracy': 0.5703971119133574, 'f1': 0.4803493449781659}  
qqp: {'accuracy': 0.47653429602888087, 'f1': 0.42231075697211157}  
qnli: {'accuracy': 0.48014440433212996}  
rte: {'accuracy': 0.5018050541516246}  
wnli: {'accuracy': 0.48736462093862815}  
hans: {'accuracy': 0.4657039711191336}  

mrpc_rte_cola_4 - 2:

sst2: {'accuracy': 0.6912751677852349}  
mnli: {'accuracy': 0.6912751677852349}  
mnli_mismatched: {'accuracy': 0.6912751677852349}  
mnli_matched: {'accuracy': 0.6912751677852349}  
cola: {'matthews_correlation': 0.0}  
stsb: {'pearson': nan, 'spearmanr': nan}  
mrpc: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qqp: {'accuracy': 0.6912751677852349, 'f1': 0.8174603174603174}  
qnli: {'accuracy': 0.6912751677852349}  
rte: {'accuracy': 0.6912751677852349}  
wnli: {'accuracy': 0.6912751677852349}  
hans: {'accuracy': 0.6912751677852349}  