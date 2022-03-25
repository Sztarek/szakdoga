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

rte_mrpc_cola_0 - 0:  
rte: {'accuracy': 0.6823104693140795}  

rte_mrpc_cola_0 - 1:  
rte: {'accuracy': 0.4981949458483754}  
mrpc: {'accuracy': 0.8455882352941176, 'f1': 0.8941176470588236}  

rte_mrpc_cola_0 - 2:  
rte: {'accuracy': 0.4657039711191336}  
mrpc: {'accuracy': 0.6862745098039216, 'f1': 0.8128654970760235}  
cola: {'matthews_correlation': 0.5392823485107089}  

rte_cola_mrpc_0 - 0:  
rte: {'accuracy': 0.6714801444043321}  

rte_cola_mrpc_0 - 1:  
rte: {'accuracy': 0.5379061371841155}  
cola: {'matthews_correlation': 0.5683668297227801}  

rte_cola_mrpc_0 - 2:  
rte: {'accuracy': 0.49458483754512633}  
cola: {'matthews_correlation': 0.286990385783097}  
mrpc: {'accuracy': 0.8676470588235294, 'f1': 0.9087837837837838}  

mrpc_rte_cola_0 - 0:  
mrpc: {'accuracy': 0.8725490196078431, 'f1': 0.9097222222222222}  

mrpc_rte_cola_0 - 1:  
mrpc: {'accuracy': 0.48284313725490197, 'f1': 0.615664845173042}  
rte: {'accuracy': 0.6714801444043321}  

mrpc_rte_cola_0 - 2:  
mrpc: {'accuracy': 0.6887254901960784, 'f1': 0.8101644245142002}  
rte: {'accuracy': 0.48014440433212996}  
cola: {'matthews_correlation': 0.5703054933279827}  

mrpc_cola_rte_0 - 0:  
mrpc: {'accuracy': 0.8602941176470589, 'f1': 0.8980322003577819}  

mrpc_cola_rte_0 - 1:  
mrpc: {'accuracy': 0.7696078431372549, 'f1': 0.8535825545171339}  
cola: {'matthews_correlation': 0.5502476813761963}  

mrpc_cola_rte_0 - 2:  
mrpc: {'accuracy': 0.3137254901960784, 'f1': 0.4017094017094017}  
cola: {'matthews_correlation': 0.3901872955343718}  
rte: {'accuracy': 0.6895306859205776}  

cola_rte_mrpc_0 - 0:  
cola: {'matthews_correlation': 0.5807606001872874}  

cola_rte_mrpc_0 - 1:  
cola: {'matthews_correlation': 0.47465938074214753}  
rte: {'accuracy': 0.6462093862815884}  

cola_rte_mrpc_0 - 2:  
cola: {'matthews_correlation': 0.172517984370661}  
rte: {'accuracy': 0.5018050541516246}  
mrpc: {'accuracy': 0.8676470588235294, 'f1': 0.9072164948453608}  

cola_mrpc_rte_0 - 0:  
cola: {'matthews_correlation': 0.5573424050983508}  

cola_mrpc_rte_0 - 1:  
cola: {'matthews_correlation': 0.24798736849128378}  
mrpc: {'accuracy': 0.8921568627450981, 'f1': 0.9251700680272108}  

cola_mrpc_rte_0 - 2:  
cola: {'matthews_correlation': 0.2009402852227427}  
mrpc: {'accuracy': 0.5465686274509803, 'f1': 0.6476190476190475}  
rte: {'accuracy': 0.5848375451263538}  

rte_cola_mrpc_1 - 0:  
rte: {'accuracy': 0.6462093862815884}  

rte_cola_mrpc_1 - 1:  
rte: {'accuracy': 0.48014440433212996}  
cola: {'matthews_correlation': 0.5963273779713936}  

rte_cola_mrpc_1 - 2:  
rte: {'accuracy': 0.516245487364621}  
cola: {'matthews_correlation': 0.27308430229823}  
mrpc: {'accuracy': 0.8529411764705882, 'f1': 0.8989898989898989}  

mrpc_rte_cola_1 - 0:  
mrpc: {'accuracy': 0.8357843137254902, 'f1': 0.8850771869639793}  

mrpc_rte_cola_1 - 1:  
mrpc: {'accuracy': 0.5171568627450981, 'f1': 0.6643952299829642}  
rte: {'accuracy': 0.6606498194945848}  

mrpc_rte_cola_1 - 2:  
mrpc: {'accuracy': 0.6887254901960784, 'f1': 0.8140556368960467}  
rte: {'accuracy': 0.4729241877256318}  
cola: {'matthews_correlation': 0.5930551868478077}  

mrpc_cola_rte_1 - 0:  
mrpc: {'accuracy': 0.8529411764705882, 'f1': 0.8936170212765957}  

mrpc_cola_rte_1 - 1:  
mrpc: {'accuracy': 0.7107843137254902, 'f1': 0.8249258160237388}  
cola: {'matthews_correlation': 0.550090073200501}  

mrpc_cola_rte_1 - 2:  
mrpc: {'accuracy': 0.3872549019607843, 'f1': 0.5059288537549408}  
cola: {'matthews_correlation': 0.45285537703926815}  
rte: {'accuracy': 0.6498194945848376}  

cola_rte_mrpc_1 - 0:  
cola: {'matthews_correlation': 0.5713110471171509}  

cola_rte_mrpc_1 - 1:  
cola: {'matthews_correlation': 0.4327177593019224}  
rte: {'accuracy': 0.6498194945848376}  

cola_rte_mrpc_1 - 2:  
cola: {'matthews_correlation': 0.3556704575157783}  
rte: {'accuracy': 0.4981949458483754}  
mrpc: {'accuracy': 0.8504901960784313, 'f1': 0.897133220910624}  

cola_mrpc_rte_1 - 0:  
cola: {'matthews_correlation': 0.5687360893544328}  

cola_mrpc_rte_1 - 1:  
cola: {'matthews_correlation': 0.19397631815298078}  
mrpc: {'accuracy': 0.8725490196078431, 'f1': 0.9106529209621993}  

cola_mrpc_rte_1 - 2:  
cola: {'matthews_correlation': -0.16662962794023017}  
mrpc: {'accuracy': 0.27941176470588236, 'f1': 0.32568807339449546}  
rte: {'accuracy': 0.6606498194945848}  

rte_mrpc_cola_2 - 0:  
rte: {'accuracy': 0.6931407942238267}  

rte_mrpc_cola_2 - 1:  
rte: {'accuracy': 0.5018050541516246}  
mrpc: {'accuracy': 0.8455882352941176, 'f1': 0.8908145580589255}  

rte_mrpc_cola_2 - 2:  
rte: {'accuracy': 0.4259927797833935}  
mrpc: {'accuracy': 0.7377450980392157, 'f1': 0.8386123680241326}  
cola: {'matthews_correlation': 0.5805514135255713}  

rte_cola_mrpc_2 - 0:  
rte: {'accuracy': 0.6534296028880866}  

rte_cola_mrpc_2 - 1:  
rte: {'accuracy': 0.4729241877256318}  
cola: {'matthews_correlation': 0.5576106804001113}  

rte_cola_mrpc_2 - 2:  
rte: {'accuracy': 0.49097472924187724}  
cola: {'matthews_correlation': 0.2555691184360863}  
mrpc: {'accuracy': 0.8676470588235294, 'f1': 0.909090909090909}  

mrpc_rte_cola_2 - 0:  
mrpc: {'accuracy': 0.8553921568627451, 'f1': 0.9005059021922428}  

mrpc_rte_cola_2 - 1:  
mrpc: {'accuracy': 0.33088235294117646, 'f1': 0.45070422535211274}  
rte: {'accuracy': 0.6859205776173285}  

mrpc_rte_cola_2 - 2:  
mrpc: {'accuracy': 0.6593137254901961, 'f1': 0.7946824224519942}  
rte: {'accuracy': 0.4729241877256318}  
cola: {'matthews_correlation': 0.5554433905906734}  

mrpc_cola_rte_2 - 0:  
mrpc: {'accuracy': 0.8504901960784313, 'f1': 0.8908765652951698}  

mrpc_cola_rte_2 - 1:  
mrpc: {'accuracy': 0.7205882352941176, 'f1': 0.8288288288288289}  
cola: {'matthews_correlation': 0.544421655829423}  

mrpc_cola_rte_2 - 2:  
mrpc: {'accuracy': 0.40931372549019607, 'f1': 0.5374280230326295}  
cola: {'matthews_correlation': 0.4418715794191063}  
rte: {'accuracy': 0.6498194945848376}  

cola_rte_mrpc_2 - 0:  
cola: {'matthews_correlation': 0.5707798240133651}  

cola_rte_mrpc_2 - 1:  
cola: {'matthews_correlation': 0.5076423377649488}  
rte: {'accuracy': 0.6931407942238267}  

cola_rte_mrpc_2 - 2:  
cola: {'matthews_correlation': 0.0}  
rte: {'accuracy': 0.5090252707581228}  
mrpc: {'accuracy': 0.8823529411764706, 'f1': 0.916083916083916}  

cola_mrpc_rte_2 - 0:  
cola: {'matthews_correlation': 0.5880544551678445}  

cola_mrpc_rte_2 - 1:  
cola: {'matthews_correlation': 0.2144031318051486}  
mrpc: {'accuracy': 0.8799019607843137, 'f1': 0.9162393162393162}  

cola_mrpc_rte_2 - 2:  
cola: {'matthews_correlation': 0.40026677748332246}  
mrpc: {'accuracy': 0.27450980392156865, 'f1': 0.22105263157894736}  
rte: {'accuracy': 0.6462093862815884}  






rte_mrpc_cola_3 - 0:  
rte: {'accuracy': 0.631768953068592}  

rte_mrpc_cola_3 - 1:  
rte: {'accuracy': 0.48375451263537905}  
mrpc: {'accuracy': 0.8725490196078431, 'f1': 0.9084507042253521}  

rte_mrpc_cola_3 - 2:  
rte: {'accuracy': 0.4151624548736462}  
mrpc: {'accuracy': 0.7181372549019608, 'f1': 0.8286140089418779}  
cola: {'matthews_correlation': 0.5578770438298012}  

rte_cola_mrpc_3 - 0:  
rte: {'accuracy': 0.6750902527075813}  

rte_cola_mrpc_3 - 1:  
rte: {'accuracy': 0.5451263537906137}  
cola: {'matthews_correlation': 0.5600900419522739}  

rte_cola_mrpc_3 - 2:  
rte: {'accuracy': 0.48014440433212996}  
cola: {'matthews_correlation': 0.285378633463526}  
mrpc: {'accuracy': 0.8529411764705882, 'f1': 0.9006622516556292}  

mrpc_rte_cola_3 - 0:  
mrpc: {'accuracy': 0.8700980392156863, 'f1': 0.9087779690189328}  

mrpc_rte_cola_3 - 1:  
mrpc: {'accuracy': 0.26715686274509803, 'f1': 0.36247334754797444}  
rte: {'accuracy': 0.6570397111913358}  

mrpc_rte_cola_3 - 2:  
mrpc: {'accuracy': 0.6838235294117647, 'f1': 0.809453471196455}  
rte: {'accuracy': 0.48014440433212996}  
cola: {'matthews_correlation': 0.5474865115851942}  

mrpc_cola_rte_3 - 0:  
mrpc: {'accuracy': 0.8504901960784313, 'f1': 0.8904847396768403}  

mrpc_cola_rte_3 - 1:  
mrpc: {'accuracy': 0.7818627450980392, 'f1': 0.8589540412044374}  
cola: {'matthews_correlation': 0.5675730029368427}  

mrpc_cola_rte_3 - 2:  
mrpc: {'accuracy': 0.40441176470588236, 'f1': 0.5110663983903421}  
cola: {'matthews_correlation': 0.4954065497058631}  
rte: {'accuracy': 0.6642599277978339}  

cola_rte_mrpc_3 - 0:  
cola: {'matthews_correlation': 0.5640063794282216}  

cola_rte_mrpc_3 - 1:  
cola: {'matthews_correlation': 0.46794560733473306}  
rte: {'accuracy': 0.6895306859205776}  

cola_rte_mrpc_3 - 2:  
cola: {'matthews_correlation': 0.24317389695801792}  
rte: {'accuracy': 0.4693140794223827}  
mrpc: {'accuracy': 0.8578431372549019, 'f1': 0.9026845637583893}  

cola_mrpc_rte_3 - 0:  
cola: {'matthews_correlation': 0.5626727648075698}  

cola_mrpc_rte_3 - 1:  
cola: {'matthews_correlation': 0.3407791173171151}  
mrpc: {'accuracy': 0.8480392156862745, 'f1': 0.8938356164383561}  

cola_mrpc_rte_3 - 2:  
cola: {'matthews_correlation': 0.4497562563404004}  
mrpc: {'accuracy': 0.4485294117647059, 'f1': 0.5778611632270169}  
rte: {'accuracy': 0.6823104693140795}  


rte_mrpc_cola_4 - 0:  
rte: {'accuracy': 0.6606498194945848}  

rte_mrpc_cola_4 - 1:  
rte: {'accuracy': 0.516245487364621}  
mrpc: {'accuracy': 0.8602941176470589, 'f1': 0.9008695652173914}  

rte_mrpc_cola_4 - 2:  
rte: {'accuracy': 0.4693140794223827}  
mrpc: {'accuracy': 0.6838235294117647, 'f1': 0.8111273792093704}  
cola: {'matthews_correlation': 0.5881989399089292}  

rte_cola_mrpc_4 - 0:  
rte: {'accuracy': 0.6895306859205776}  

rte_cola_mrpc_4 - 1:  
rte: {'accuracy': 0.48736462093862815}  
cola: {'matthews_correlation': 0.5750821529922306}  

rte_cola_mrpc_4 - 2:  
rte: {'accuracy': 0.48736462093862815}  
cola: {'matthews_correlation': 0.17687899023802509}  
mrpc: {'accuracy': 0.8553921568627451, 'f1': 0.9005059021922428}  

mrpc_rte_cola_4 - 0:  
mrpc: {'accuracy': 0.8357843137254902, 'f1': 0.8830715532286212}  

mrpc_rte_cola_4 - 1:  
mrpc: {'accuracy': 0.38480392156862747, 'f1': 0.4803312629399586}  
rte: {'accuracy': 0.6173285198555957}  

mrpc_rte_cola_4 - 2:  
mrpc: {'accuracy': 0.6936274509803921, 'f1': 0.8114630467571644}  
rte: {'accuracy': 0.5776173285198556}  
cola: {'matthews_correlation': 0.5364243566130295}  

mrpc_cola_rte_4 - 0:  
mrpc: {'accuracy': 0.8406862745098039, 'f1': 0.8914858096828046}  

mrpc_cola_rte_4 - 1:  
mrpc: {'accuracy': 0.696078431372549, 'f1': 0.8181818181818181}  
cola: {'matthews_correlation': 0.5323002583628187}  

mrpc_cola_rte_4 - 2:  
mrpc: {'accuracy': 0.44607843137254904, 'f1': 0.5461847389558233}  
cola: {'matthews_correlation': 0.509956265936642}  
rte: {'accuracy': 0.6931407942238267}  

cola_rte_mrpc_4 - 0:  
cola: {'matthews_correlation': 0.5294768861655004}  

cola_rte_mrpc_4 - 1:  
cola: {'matthews_correlation': 0.500543339002461}  
rte: {'accuracy': 0.631768953068592}  

cola_rte_mrpc_4 - 2:  
cola: {'matthews_correlation': 0.1902493163456578}  
rte: {'accuracy': 0.48375451263537905}  
mrpc: {'accuracy': 0.8651960784313726, 'f1': 0.905982905982906}  

cola_mrpc_rte_4 - 0:  
cola: {'matthews_correlation': 0.5469075065870133}  

cola_mrpc_rte_4 - 1:  
cola: {'matthews_correlation': 0.3068048852377893}  
mrpc: {'accuracy': 0.8602941176470589, 'f1': 0.9025641025641027}  

cola_mrpc_rte_4 - 2:  
cola: {'matthews_correlation': -0.2549503043045016}  
mrpc: {'accuracy': 0.2181372549019608, 'f1': 0.15831134564643798}  
rte: {'accuracy': 0.6606498194945848}  


rte_mrpc_cola_5 - 0:  
rte: {'accuracy': 0.6101083032490975}  

rte_mrpc_cola_5 - 1:  
rte: {'accuracy': 0.5126353790613718}  
mrpc: {'accuracy': 0.8357843137254902, 'f1': 0.8842832469775476}  

rte_mrpc_cola_5 - 2:  
rte: {'accuracy': 0.4729241877256318}  
mrpc: {'accuracy': 0.6862745098039216, 'f1': 0.8134110787172011}  
cola: {'matthews_correlation': 0.5258978858175564}  

rte_cola_mrpc_5 - 0:  
rte: {'accuracy': 0.6462093862815884}  

rte_cola_mrpc_5 - 1:  
rte: {'accuracy': 0.6859205776173285}  
cola: {'matthews_correlation': 0.5290037338732806}  

rte_cola_mrpc_5 - 2:  
rte: {'accuracy': 0.48375451263537905}  
cola: {'matthews_correlation': 0.2817531644646134}  
mrpc: {'accuracy': 0.8406862745098039, 'f1': 0.8881239242685025}  

mrpc_rte_cola_5 - 0:  
mrpc: {'accuracy': 0.8627450980392157, 'f1': 0.903448275862069}  

mrpc_rte_cola_5 - 1:  
mrpc: {'accuracy': 0.4877450980392157, 'f1': 0.6287744227353463}  
rte: {'accuracy': 0.6750902527075813}  

mrpc_rte_cola_5 - 2:  
mrpc: {'accuracy': 0.6764705882352942, 'f1': 0.8064516129032258}  
rte: {'accuracy': 0.4981949458483754}  
cola: {'matthews_correlation': 0.5651604238862242}  

mrpc_cola_rte_5 - 0:  
mrpc: {'accuracy': 0.8480392156862745, 'f1': 0.8912280701754387}  

mrpc_cola_rte_5 - 1:  
mrpc: {'accuracy': 0.6911764705882353, 'f1': 0.8157894736842105}  
cola: {'matthews_correlation': 0.5367676459034164}  

mrpc_cola_rte_5 - 2:  
mrpc: {'accuracy': 0.5147058823529411, 'f1': 0.6526315789473685}  
cola: {'matthews_correlation': 0.4376793819287724}  
rte: {'accuracy': 0.592057761732852}  

cola_rte_mrpc_5 - 0:  
cola: {'matthews_correlation': 0.5390406008281052}  

cola_rte_mrpc_5 - 1:  
cola: {'matthews_correlation': 0.5155338105766099}  
rte: {'accuracy': 0.6859205776173285}  

cola_rte_mrpc_5 - 2:  
cola: {'matthews_correlation': 0.19600053498374753}  
rte: {'accuracy': 0.49458483754512633}  
mrpc: {'accuracy': 0.8455882352941176, 'f1': 0.8930390492359932}  

cola_mrpc_rte_5 - 0:  
cola: {'matthews_correlation': 0.5134084664186066}  

cola_mrpc_rte_5 - 1:  
cola: {'matthews_correlation': 0.3466962656536044}  
mrpc: {'accuracy': 0.8578431372549019, 'f1': 0.9023569023569024}  

cola_mrpc_rte_5 - 2:  
cola: {'matthews_correlation': 0.41167162614728725}  
mrpc: {'accuracy': 0.45098039215686275, 'f1': 0.5956678700361011}  
rte: {'accuracy': 0.6425992779783394}  

rte_mrpc_cola_6 - 0:  
rte: {'accuracy': 0.6678700361010831}  

rte_mrpc_cola_6 - 1:  
rte: {'accuracy': 0.51985559566787}  
mrpc: {'accuracy': 0.8235294117647058, 'f1': 0.875}  

rte_mrpc_cola_6 - 2:  
rte: {'accuracy': 0.4729241877256318}  
mrpc: {'accuracy': 0.696078431372549, 'f1': 0.8181818181818181}  
cola: {'matthews_correlation': 0.5037810327397391}  

rte_cola_mrpc_6 - 0:  
rte: {'accuracy': 0.6859205776173285}  

rte_cola_mrpc_6 - 1:  
rte: {'accuracy': 0.6570397111913358}  
cola: {'matthews_correlation': 0.48061177250450887}  

rte_cola_mrpc_6 - 2:  
rte: {'accuracy': 0.516245487364621}  
cola: {'matthews_correlation': 0.29025129814536477}  
mrpc: {'accuracy': 0.8088235294117647, 'f1': 0.8655172413793105}  

mrpc_rte_cola_6 - 0:  
mrpc: {'accuracy': 0.821078431372549, 'f1': 0.874354561101549}  

mrpc_rte_cola_6 - 1:  
mrpc: {'accuracy': 0.4166666666666667, 'f1': 0.5559701492537314}  
rte: {'accuracy': 0.6028880866425993}  

mrpc_rte_cola_6 - 2:  
mrpc: {'accuracy': 0.6838235294117647, 'f1': 0.8116788321167884}  
rte: {'accuracy': 0.516245487364621}  
cola: {'matthews_correlation': 0.48652176899433314}  

mrpc_cola_rte_6 - 0:  
mrpc: {'accuracy': 0.8014705882352942, 'f1': 0.8615384615384616}  

mrpc_cola_rte_6 - 1:  
mrpc: {'accuracy': 0.75, 'f1': 0.843558282208589}  
cola: {'matthews_correlation': 0.5235990316279782}  

mrpc_cola_rte_6 - 2:  
mrpc: {'accuracy': 0.33088235294117646, 'f1': 0.3973509933774834}  
cola: {'matthews_correlation': 0.41319696759502633}  
rte: {'accuracy': 0.5992779783393501}  

cola_rte_mrpc_6 - 0:  
cola: {'matthews_correlation': 0.5200220944545176}  

cola_rte_mrpc_6 - 1:  
cola: {'matthews_correlation': 0.4071353424775658}  
rte: {'accuracy': 0.703971119133574}  

cola_rte_mrpc_6 - 2:  
cola: {'matthews_correlation': 0.1993093660511721}  
rte: {'accuracy': 0.44765342960288806}  
mrpc: {'accuracy': 0.8725490196078431, 'f1': 0.9106529209621993}  

cola_mrpc_rte_6 - 0:  
cola: {'matthews_correlation': 0.5048506698662225}  

cola_mrpc_rte_6 - 1:  
cola: {'matthews_correlation': 0.24651132722157929}  
mrpc: {'accuracy': 0.8357843137254902, 'f1': 0.8892561983471075}  

cola_mrpc_rte_6 - 2:  
cola: {'matthews_correlation': -0.12919996867279102}  
mrpc: {'accuracy': 0.23039215686274508, 'f1': 0.16489361702127656}  
rte: {'accuracy': 0.6245487364620939}  

rte_mrpc_cola_7 - 0:  
rte: {'accuracy': 0.5956678700361011}  

rte_mrpc_cola_7 - 1:  
rte: {'accuracy': 0.47653429602888087}  
mrpc: {'accuracy': 0.8088235294117647, 'f1': 0.8677966101694915}  

rte_mrpc_cola_7 - 2:  
rte: {'accuracy': 0.4368231046931408}  
mrpc: {'accuracy': 0.7058823529411765, 'f1': 0.8224852071005917}  
cola: {'matthews_correlation': 0.5155383069979991}  

rte_cola_mrpc_7 - 0:  
rte: {'accuracy': 0.6425992779783394}  

rte_cola_mrpc_7 - 1:  
rte: {'accuracy': 0.6462093862815884}  
cola: {'matthews_correlation': 0.510581671760424}  

rte_cola_mrpc_7 - 2:  
rte: {'accuracy': 0.4729241877256318}  
cola: {'matthews_correlation': 0.3452285361947951}  
mrpc: {'accuracy': 0.8333333333333334, 'f1': 0.8881578947368421}  

mrpc_rte_cola_7 - 0:  
mrpc: {'accuracy': 0.821078431372549, 'f1': 0.8756388415672913}  

mrpc_rte_cola_7 - 1:  
mrpc: {'accuracy': 0.5490196078431373, 'f1': 0.6933333333333334}  
rte: {'accuracy': 0.5884476534296029}  

mrpc_rte_cola_7 - 2:  
mrpc: {'accuracy': 0.6838235294117647, 'f1': 0.8122270742358079}  
rte: {'accuracy': 0.48014440433212996}  
cola: {'matthews_correlation': 0.5075813582663956}  

mrpc_cola_rte_7 - 0:  
mrpc: {'accuracy': 0.7990196078431373, 'f1': 0.8591065292096219}  

mrpc_cola_rte_7 - 1:  
mrpc: {'accuracy': 0.7475490196078431, 'f1': 0.8427480916030534}  
cola: {'matthews_correlation': 0.4939105407308262}  

mrpc_cola_rte_7 - 2:  
mrpc: {'accuracy': 0.34558823529411764, 'f1': 0.44490644490644493}  
cola: {'matthews_correlation': 0.4121884254314843}  
rte: {'accuracy': 0.6028880866425993}  

cola_rte_mrpc_7 - 0:  
cola: {'matthews_correlation': 0.49702553536108757}  

cola_rte_mrpc_7 - 1:  
cola: {'matthews_correlation': 0.41051204645145506}  
rte: {'accuracy': 0.6678700361010831}  

cola_rte_mrpc_7 - 2:  
cola: {'matthews_correlation': 0.26470976643888067}  
rte: {'accuracy': 0.4729241877256318}  
mrpc: {'accuracy': 0.821078431372549, 'f1': 0.8760611205432938}  

cola_mrpc_rte_7 - 0:  
cola: {'matthews_correlation': 0.5126143737721263}  

cola_mrpc_rte_7 - 1:  
cola: {'matthews_correlation': 0.4600853746935537}  
mrpc: {'accuracy': 0.803921568627451, 'f1': 0.8615916955017301}  

cola_mrpc_rte_7 - 2:  
cola: {'matthews_correlation': 0.39492313234248005}  
mrpc: {'accuracy': 0.4411764705882353, 'f1': 0.5615384615384617}  
rte: {'accuracy': 0.6137184115523465}  

rte_mrpc_cola_8 - 0:  
rte: {'accuracy': 0.628158844765343}  

rte_mrpc_cola_8 - 1:  
rte: {'accuracy': 0.41155234657039713}  
mrpc: {'accuracy': 0.8161764705882353, 'f1': 0.8743718592964823}  

rte_mrpc_cola_8 - 2:  
rte: {'accuracy': 0.33212996389891697}  
mrpc: {'accuracy': 0.7818627450980392, 'f1': 0.8589540412044374}  
cola: {'matthews_correlation': 0.48599506757965116}  

rte_cola_mrpc_8 - 0:  
rte: {'accuracy': 0.6137184115523465}  

rte_cola_mrpc_8 - 1:  
rte: {'accuracy': 0.6462093862815884}  
cola: {'matthews_correlation': 0.4801818467382683}  

rte_cola_mrpc_8 - 2:  
rte: {'accuracy': 0.4548736462093863}  
cola: {'matthews_correlation': 0.33781124715873906}  
mrpc: {'accuracy': 0.803921568627451, 'f1': 0.8675496688741722}  

mrpc_rte_cola_8 - 0:  
mrpc: {'accuracy': 0.7867647058823529, 'f1': 0.8507718696397941}  

mrpc_rte_cola_8 - 1:  
mrpc: {'accuracy': 0.375, 'f1': 0.45628997867803844}  
rte: {'accuracy': 0.6137184115523465}  

mrpc_rte_cola_8 - 2:  
mrpc: {'accuracy': 0.6887254901960784, 'f1': 0.8145985401459854}  
rte: {'accuracy': 0.48736462093862815}  
cola: {'matthews_correlation': 0.4747045393662238}  

mrpc_cola_rte_8 - 0:  
mrpc: {'accuracy': 0.7965686274509803, 'f1': 0.8605042016806722}  

mrpc_cola_rte_8 - 1:  
mrpc: {'accuracy': 0.7303921568627451, 'f1': 0.8307692307692308}  
cola: {'matthews_correlation': 0.4856483967190665}  

mrpc_cola_rte_8 - 2:  
mrpc: {'accuracy': 0.3137254901960784, 'f1': 0.4067796610169492}  
cola: {'matthews_correlation': -0.02031232391313516}  
rte: {'accuracy': 0.6642599277978339}  

cola_rte_mrpc_8 - 0:  
cola: {'matthews_correlation': 0.4719849910356732}  

cola_rte_mrpc_8 - 1:  
cola: {'matthews_correlation': 0.3465251853187258}  
rte: {'accuracy': 0.6462093862815884}  

cola_rte_mrpc_8 - 2:  
cola: {'matthews_correlation': 0.3016433418855528}  
rte: {'accuracy': 0.49097472924187724}  
mrpc: {'accuracy': 0.7916666666666666, 'f1': 0.8571428571428571}  

cola_mrpc_rte_8 - 0:  
cola: {'matthews_correlation': 0.47817459022785963}  

cola_mrpc_rte_8 - 1:  
cola: {'matthews_correlation': 0.30608315489070037}  
mrpc: {'accuracy': 0.8259803921568627, 'f1': 0.8794567062818336}  

cola_mrpc_rte_8 - 2:  
cola: {'matthews_correlation': -0.008194308938556785}  
mrpc: {'accuracy': 0.37745098039215685, 'f1': 0.42792792792792794}  
rte: {'accuracy': 0.6353790613718412}  

rte_mrpc_cola_9 - 0:  
rte: {'accuracy': 0.5848375451263538}  

rte_mrpc_cola_9 - 1:  
rte: {'accuracy': 0.4187725631768953}  
mrpc: {'accuracy': 0.7622549019607843, 'f1': 0.8438003220611916}  

rte_mrpc_cola_9 - 2:  
rte: {'accuracy': 0.45126353790613716}  
mrpc: {'accuracy': 0.6887254901960784, 'f1': 0.8145985401459854}  
cola: {'matthews_correlation': 0.4304260866765428}  

rte_cola_mrpc_9 - 0:  
rte: {'accuracy': 0.6173285198555957}  

rte_cola_mrpc_9 - 1:  
rte: {'accuracy': 0.6101083032490975}  
cola: {'matthews_correlation': 0.4459485588679525}  

rte_cola_mrpc_9 - 2:  
rte: {'accuracy': 0.4223826714801444}  
cola: {'matthews_correlation': 0.31657590231625093}  
mrpc: {'accuracy': 0.7867647058823529, 'f1': 0.8576104746317512}  

mrpc_rte_cola_9 - 0:  
mrpc: {'accuracy': 0.7794117647058824, 'f1': 0.8514851485148515}  

mrpc_rte_cola_9 - 1:  
mrpc: {'accuracy': 0.34558823529411764, 'f1': 0.3407407407407408}  
rte: {'accuracy': 0.6028880866425993}  

mrpc_rte_cola_9 - 2:  
mrpc: {'accuracy': 0.6862745098039216, 'f1': 0.8134110787172011}  
rte: {'accuracy': 0.48014440433212996}  
cola: {'matthews_correlation': 0.42425075806204515}  

mrpc_cola_rte_9 - 0:  
mrpc: {'accuracy': 0.7696078431372549, 'f1': 0.8464052287581698}  

mrpc_cola_rte_9 - 1:  
mrpc: {'accuracy': 0.7132352941176471, 'f1': 0.826151560178306}  
cola: {'matthews_correlation': 0.44997974461232476}  

mrpc_cola_rte_9 - 2:  
mrpc: {'accuracy': 0.27450980392156865, 'f1': 0.2952380952380952}  
cola: {'matthews_correlation': 0.06635689908148355}  
rte: {'accuracy': 0.6353790613718412}  

cola_mrpc_rte_9 - 0:  
cola: {'matthews_correlation': 0.45051784112581156}  

cola_mrpc_rte_9 - 1:  
cola: {'matthews_correlation': 0.18590205196989334}  
mrpc: {'accuracy': 0.8014705882352942, 'f1': 0.8652246256239601}  

cola_rte_mrpc_9 - 0:  
cola: {'matthews_correlation': 0.4510223816140928}  

cola_rte_mrpc_9 - 1:  
cola: {'matthews_correlation': 0.40140645308106226}  
rte: {'accuracy': 0.6137184115523465}  

cola_rte_mrpc_9 - 2:  
cola: {'matthews_correlation': 0.2431703967304969}  
rte: {'accuracy': 0.4187725631768953}  
mrpc: {'accuracy': 0.7818627450980392, 'f1': 0.8528925619834711}  

cola_mrpc_rte_9 - 2:  
cola: {'matthews_correlation': -0.23797013415209908}  
mrpc: {'accuracy': 0.27450980392156865, 'f1': 0.21693121693121695}  
rte: {'accuracy': 0.631768953068592}  

cola_rte_mrpc_10 - 0:  
cola: {'matthews_correlation': 0.3837563526100285}  

cola_rte_mrpc_10 - 1:  
cola: {'matthews_correlation': 0.36677168221902623}  
rte: {'accuracy': 0.6064981949458483}  

cola_rte_mrpc_10 - 2:  
cola: {'matthews_correlation': 0.2302494908160266}  
rte: {'accuracy': 0.4151624548736462}  
mrpc: {'accuracy': 0.7769607843137255, 'f1': 0.8553259141494436}  

cola_mrpc_rte_10 - 0:  
cola: {'matthews_correlation': 0.3837563526100285}  

cola_mrpc_rte_10 - 1:  
cola: {'matthews_correlation': 0.32751736540831267}  
mrpc: {'accuracy': 0.7450980392156863, 'f1': 0.83596214511041}  

cola_mrpc_rte_10 - 2:  
cola: {'matthews_correlation': 0.2139258572077333}  
mrpc: {'accuracy': 0.4264705882352941, 'f1': 0.47533632286995514}  
rte: {'accuracy': 0.6209386281588448}  

rte_mrpc_cola_10 - 0:  
rte: {'accuracy': 0.5740072202166066}  

rte_mrpc_cola_10 - 1:  
rte: {'accuracy': 0.4259927797833935}  
mrpc: {'accuracy': 0.7622549019607843, 'f1': 0.8407224958949097}  

rte_mrpc_cola_10 - 2:  
rte: {'accuracy': 0.4368231046931408}  
mrpc: {'accuracy': 0.6936274509803921, 'f1': 0.8169838945827232}  
cola: {'matthews_correlation': 0.39521791340818474}  

rte_cola_mrpc_10 - 0:  
rte: {'accuracy': 0.5595667870036101}  

rte_cola_mrpc_10 - 1:  
rte: {'accuracy': 0.48014440433212996}  
cola: {'matthews_correlation': 0.4025454740592728}  

rte_cola_mrpc_10 - 2:  
rte: {'accuracy': 0.4223826714801444}  
cola: {'matthews_correlation': 0.25430833215552345}  
mrpc: {'accuracy': 0.7622549019607843, 'f1': 0.8448}  

mrpc_rte_cola_10 - 0:  
mrpc: {'accuracy': 0.75, 'f1': 0.8344155844155844}  

mrpc_rte_cola_10 - 1:  
mrpc: {'accuracy': 0.27205882352941174, 'f1': 0.10271903323262839}  
rte: {'accuracy': 0.5992779783393501}  

mrpc_rte_cola_10 - 2:  
mrpc: {'accuracy': 0.5784313725490197, 'f1': 0.7114093959731543}  
rte: {'accuracy': 0.5270758122743683}  
cola: {'matthews_correlation': 0.3927020726984416}  

mrpc_cola_rte_10 - 0:  
mrpc: {'accuracy': 0.7573529411764706, 'f1': 0.8436018957345972}  

mrpc_cola_rte_10 - 1:  
mrpc: {'accuracy': 0.7034313725490197, 'f1': 0.8212703101920238}  
cola: {'matthews_correlation': 0.40858564179092355}  

mrpc_cola_rte_10 - 2:  
mrpc: {'accuracy': 0.2696078431372549, 'f1': 0.2032085561497326}  
cola: {'matthews_correlation': -0.12595544001960396}  
rte: {'accuracy': 0.6245487364620939}  

rte_mrpc_cola_11 - 0:  
rte: {'accuracy': 0.5740072202166066}  

rte_mrpc_cola_11 - 1:  
rte: {'accuracy': 0.47653429602888087}  
mrpc: {'accuracy': 0.7205882352941176, 'f1': 0.8272727272727272}  

rte_mrpc_cola_11 - 2:  
rte: {'accuracy': 0.47653429602888087}  
mrpc: {'accuracy': 0.696078431372549, 'f1': 0.8176470588235294}  
cola: {'matthews_correlation': 0.3663821725095162}  

rte_cola_mrpc_11 - 0:  
rte: {'accuracy': 0.5703971119133574}  

rte_cola_mrpc_11 - 1:  
rte: {'accuracy': 0.4729241877256318}  
cola: {'matthews_correlation': 0.36551336091195347}  

rte_cola_mrpc_11 - 2:  
rte: {'accuracy': 0.4296028880866426}  
cola: {'matthews_correlation': 0.29222864829416634}  
mrpc: {'accuracy': 0.7156862745098039, 'f1': 0.8220858895705522}  

mrpc_rte_cola_11 - 0:  
mrpc: {'accuracy': 0.7230392156862745, 'f1': 0.8253477588871715}  

mrpc_rte_cola_11 - 1:  
mrpc: {'accuracy': 0.2965686274509804, 'f1': 0.046511627906976744}  
rte: {'accuracy': 0.6101083032490975}  

mrpc_rte_cola_11 - 2:  
mrpc: {'accuracy': 0.6764705882352942, 'f1': 0.8029850746268656}  
rte: {'accuracy': 0.5126353790613718}  
cola: {'matthews_correlation': 0.3456014554543514}  

mrpc_cola_rte_11 - 0:  
mrpc: {'accuracy': 0.7303921568627451, 'f1': 0.8297213622291022}  

mrpc_cola_rte_11 - 1:  
mrpc: {'accuracy': 0.6887254901960784, 'f1': 0.8145985401459854}  
cola: {'matthews_correlation': 0.3556451144819016}  

mrpc_cola_rte_11 - 2:  
mrpc: {'accuracy': 0.37254901960784315, 'f1': 0.34693877551020413}  
cola: {'matthews_correlation': 0.31951574880896005}  
rte: {'accuracy': 0.6389891696750902}  

cola_rte_mrpc_11 - 0:  
cola: {'matthews_correlation': 0.3865296474948357}  

cola_rte_mrpc_11 - 1:  
cola: {'matthews_correlation': 0.3245964204558575}  
rte: {'accuracy': 0.592057761732852}  

cola_rte_mrpc_11 - 2:  
cola: {'matthews_correlation': 0.1949585962172032}  
rte: {'accuracy': 0.4584837545126354}  
mrpc: {'accuracy': 0.7352941176470589, 'f1': 0.8301886792452831}  

cola_mrpc_rte_11 - 0:  
cola: {'matthews_correlation': 0.3443831021173783}  

cola_mrpc_rte_11 - 1:  
cola: {'matthews_correlation': 0.23055877745040174}  
mrpc: {'accuracy': 0.7181372549019608, 'f1': 0.8233486943164363}  

cola_mrpc_rte_11 - 2:  
cola: {'matthews_correlation': 0.35016321987632565}  
mrpc: {'accuracy': 0.5833333333333334, 'f1': 0.6942446043165468}  
rte: {'accuracy': 0.5884476534296029}  

rte_cola_mrpc_12 - 0:  
rte: {'accuracy': 0.5631768953068592}  

rte_cola_mrpc_12 - 1:  
rte: {'accuracy': 0.4729241877256318}  
cola: {'matthews_correlation': 0.22092729492191307}  

rte_cola_mrpc_12 - 2:  
rte: {'accuracy': 0.4548736462093863}  
cola: {'matthews_correlation': 0.09450316316043533}  
mrpc: {'accuracy': 0.6887254901960784, 'f1': 0.8145985401459854}  

mrpc_rte_cola_12 - 0:  
mrpc: {'accuracy': 0.6911764705882353, 'f1': 0.8157894736842105}  

mrpc_rte_cola_12 - 1:  
mrpc: {'accuracy': 0.32107843137254904, 'f1': 0.041522491349480974}  
rte: {'accuracy': 0.5379061371841155}  

mrpc_rte_cola_12 - 2:  
mrpc: {'accuracy': 0.6838235294117647, 'f1': 0.8122270742358079}  
rte: {'accuracy': 0.4729241877256318}  
cola: {'matthews_correlation': 0.2228532415409462}  

mrpc_cola_rte_12 - 0:  
mrpc: {'accuracy': 0.6887254901960784, 'f1': 0.8145985401459854}  

mrpc_cola_rte_12 - 1:  
mrpc: {'accuracy': 0.6838235294117647, 'f1': 0.8122270742358079}  
cola: {'matthews_correlation': 0.2685388119872844}  

mrpc_cola_rte_12 - 2:  
mrpc: {'accuracy': 0.3161764705882353, 'f1': 0.04123711340206186}  
cola: {'matthews_correlation': 0.2880531281790735}  
rte: {'accuracy': 0.5379061371841155}  

cola_rte_mrpc_12 - 0:  
cola: {'matthews_correlation': 0.24509369897354713}  

cola_rte_mrpc_12 - 1:  
cola: {'matthews_correlation': 0.2894166011790952}  
rte: {'accuracy': 0.5667870036101083}  

cola_rte_mrpc_12 - 2:  
cola: {'matthews_correlation': 0.11109958477894548}  
rte: {'accuracy': 0.4584837545126354}  
mrpc: {'accuracy': 0.6862745098039216, 'f1': 0.8128654970760235}  

rte_mrpc_cola_12 - 0:  
rte: {'accuracy': 0.5523465703971119}  

rte_mrpc_cola_12 - 1:  
rte: {'accuracy': 0.4584837545126354}  
mrpc: {'accuracy': 0.6838235294117647, 'f1': 0.8122270742358079}  

rte_mrpc_cola_12 - 2:  
rte: {'accuracy': 0.4729241877256318}  
mrpc: {'accuracy': 0.6838235294117647, 'f1': 0.8122270742358079}  
cola: {'matthews_correlation': 0.2688165879920979}  

cola_mrpc_rte_12 - 0:  
cola: {'matthews_correlation': 0.21580374087877008}  

cola_mrpc_rte_12 - 1:  
cola: {'matthews_correlation': 0.03589254563226399}  
mrpc: {'accuracy': 0.6887254901960784, 'f1': 0.8140556368960467}  

cola_mrpc_rte_12 - 2:  
cola: {'matthews_correlation': 0.4043536936696055}  
mrpc: {'accuracy': 0.32598039215686275, 'f1': 0.0924092409240924}  
rte: {'accuracy': 0.5342960288808665}  

