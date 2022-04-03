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

cola_mrpc_rte_0 - 0:  
cola: {'matthews_correlation': 0.5701176712316939}  

cola_mrpc_rte_0 - 1:  
cola: {'matthews_correlation': 0.2675090780156264}  
mrpc: {'accuracy': 0.8357843137254902, 'f1': 0.8846815834767642}  

cola_mrpc_rte_0 - 2:  
cola: {'matthews_correlation': 0.15278587777861463}  
mrpc: {'accuracy': 0.4534313725490196, 'f1': 0.5862708719851578}  
rte: {'accuracy': 0.6787003610108303}  

cola_rte_mrpc_0 - 0:  
cola: {'matthews_correlation': 0.5725078939425798}  

cola_rte_mrpc_0 - 1:  
cola: {'matthews_correlation': 0.4803084441285113}  
rte: {'accuracy': 0.6462093862815884}  

cola_rte_mrpc_0 - 2:  
cola: {'matthews_correlation': 0.2859691734342701}  
rte: {'accuracy': 0.5126353790613718}  
mrpc: {'accuracy': 0.8774509803921569, 'f1': 0.9125874125874125}  

mrpc_cola_rte_0 - 0:  
mrpc: {'accuracy': 0.8627450980392157, 'f1': 0.9020979020979022}  

mrpc_cola_rte_0 - 1:  
mrpc: {'accuracy': 0.7352941176470589, 'f1': 0.8373493975903614}  
cola: {'matthews_correlation': 0.5706355604450147}  

mrpc_cola_rte_0 - 2:  
mrpc: {'accuracy': 0.2769607843137255, 'f1': 0.2992874109263658}  
cola: {'matthews_correlation': 0.4385090308874721}  
rte: {'accuracy': 0.6678700361010831}  

mrpc_rte_cola_0 - 0:  
mrpc: {'accuracy': 0.8676470588235294, 'f1': 0.9049295774647886}  

mrpc_rte_cola_0 - 1:  
mrpc: {'accuracy': 0.42892156862745096, 'f1': 0.5677179962894248}  
rte: {'accuracy': 0.6642599277978339}  

mrpc_rte_cola_0 - 2:  
mrpc: {'accuracy': 0.6862745098039216, 'f1': 0.8128654970760235}  
rte: {'accuracy': 0.47653429602888087}  
cola: {'matthews_correlation': 0.5523181756655187}  

rte_cola_mrpc_0 - 0:  
rte: {'accuracy': 0.6570397111913358}  

rte_cola_mrpc_0 - 1:  
rte: {'accuracy': 0.6498194945848376}  
cola: {'matthews_correlation': 0.5632084517291658}  

rte_cola_mrpc_0 - 2:  
rte: {'accuracy': 0.4404332129963899}  
cola: {'matthews_correlation': 0.19679414098180048}  
mrpc: {'accuracy': 0.8382352941176471, 'f1': 0.89}  

rte_mrpc_cola_0 - 0:  
rte: {'accuracy': 0.7075812274368231}  

rte_mrpc_cola_0 - 1:  
rte: {'accuracy': 0.4981949458483754}  
mrpc: {'accuracy': 0.8627450980392157, 'f1': 0.900709219858156}  

rte_mrpc_cola_0 - 2:  
rte: {'accuracy': 0.4693140794223827}  
mrpc: {'accuracy': 0.7549019607843137, 'f1': 0.84375}  
cola: {'matthews_correlation': 0.5600900419522739}  

cola_mrpc_rte_1 - 0:  
cola: {'matthews_correlation': 0.556015225978778}  

cola_mrpc_rte_1 - 1:  
cola: {'matthews_correlation': 0.2887522118255447}  
mrpc: {'accuracy': 0.8578431372549019, 'f1': 0.9023569023569024}  

cola_mrpc_rte_1 - 2:  
cola: {'matthews_correlation': -0.09017048020720095}  
mrpc: {'accuracy': 0.23039215686274508, 'f1': 0.23039215686274508}  
rte: {'accuracy': 0.6823104693140795}  

cola_rte_mrpc_1 - 0:  
cola: {'matthews_correlation': 0.5783323107334525}  

cola_rte_mrpc_1 - 1:  
cola: {'matthews_correlation': 0.5367820334111587}  
rte: {'accuracy': 0.6425992779783394}  

cola_rte_mrpc_1 - 2:  
cola: {'matthews_correlation': 0.19777081723958334}  
rte: {'accuracy': 0.5018050541516246}  
mrpc: {'accuracy': 0.8774509803921569, 'f1': 0.9146757679180888}  

mrpc_cola_rte_1 - 0:  
mrpc: {'accuracy': 0.8651960784313726, 'f1': 0.9043478260869565}  

mrpc_cola_rte_1 - 1:  
mrpc: {'accuracy': 0.7622549019607843, 'f1': 0.8514548238897397}  
cola: {'matthews_correlation': 0.5494767866076017}  

mrpc_cola_rte_1 - 2:  
mrpc: {'accuracy': 0.4583333333333333, 'f1': 0.600361663652803}  
cola: {'matthews_correlation': 0.4882441186441421}  
rte: {'accuracy': 0.6570397111913358}  

mrpc_rte_cola_1 - 0:  
mrpc: {'accuracy': 0.8725490196078431, 'f1': 0.9109589041095889}  

mrpc_rte_cola_1 - 1:  
mrpc: {'accuracy': 0.37745098039215685, 'f1': 0.5115384615384616}  
rte: {'accuracy': 0.6859205776173285}  

mrpc_rte_cola_1 - 2:  
mrpc: {'accuracy': 0.6838235294117647, 'f1': 0.8122270742358079}  
rte: {'accuracy': 0.4693140794223827}  
cola: {'matthews_correlation': 0.5598395777855655}  

rte_cola_mrpc_1 - 0:  
rte: {'accuracy': 0.6714801444043321}  

rte_cola_mrpc_1 - 1:  
rte: {'accuracy': 0.4729241877256318}  
cola: {'matthews_correlation': 0.5792266130251226}  

rte_cola_mrpc_1 - 2:  
rte: {'accuracy': 0.49458483754512633}  
cola: {'matthews_correlation': 0.1852426471184827}  
mrpc: {'accuracy': 0.8725490196078431, 'f1': 0.9109589041095889}  

rte_mrpc_cola_1 - 0:  
rte: {'accuracy': 0.6787003610108303}  

rte_mrpc_cola_1 - 1:  
rte: {'accuracy': 0.5018050541516246}  
mrpc: {'accuracy': 0.875, 'f1': 0.9087656529516995}  

rte_mrpc_cola_1 - 2:  
rte: {'accuracy': 0.4729241877256318}  
mrpc: {'accuracy': 0.7107843137254902, 'f1': 0.8249258160237388}  
cola: {'matthews_correlation': 0.5367676459034164}  

cola_mrpc_rte_2 - 0:  
cola: {'matthews_correlation': 0.5523181756655187}  

cola_mrpc_rte_2 - 1:  
cola: {'matthews_correlation': 0.21199981305697901}  
mrpc: {'accuracy': 0.8578431372549019, 'f1': 0.9006849315068494}  

cola_mrpc_rte_2 - 2:  
cola: {'matthews_correlation': -0.12147716888927587}  
mrpc: {'accuracy': 0.21323529411764705, 'f1': 0.17054263565891473}  
rte: {'accuracy': 0.6534296028880866}  

cola_rte_mrpc_2 - 0:  
cola: {'matthews_correlation': 0.5885471185335819}  

cola_rte_mrpc_2 - 1:  
cola: {'matthews_correlation': 0.4869603682896572}  
rte: {'accuracy': 0.6750902527075813}  

cola_rte_mrpc_2 - 2:  
cola: {'matthews_correlation': 0.23719201614228083}  
rte: {'accuracy': 0.4981949458483754}  
mrpc: {'accuracy': 0.8480392156862745, 'f1': 0.89419795221843}  

mrpc_cola_rte_2 - 0:  
mrpc: {'accuracy': 0.8480392156862745, 'f1': 0.8927335640138409}  

mrpc_cola_rte_2 - 1:  
mrpc: {'accuracy': 0.7573529411764706, 'f1': 0.8488549618320611}  
cola: {'matthews_correlation': 0.5733495702281163}  

mrpc_cola_rte_2 - 2:  
mrpc: {'accuracy': 0.34068627450980393, 'f1': 0.4288747346072187}  
cola: {'matthews_correlation': 0.4578310517092636}  
rte: {'accuracy': 0.6823104693140795}  

mrpc_rte_cola_2 - 0:  
mrpc: {'accuracy': 0.8529411764705882, 'f1': 0.896551724137931}  

mrpc_rte_cola_2 - 1:  
mrpc: {'accuracy': 0.3014705882352941, 'f1': 0.36525612472160357}  
rte: {'accuracy': 0.6714801444043321}  

mrpc_rte_cola_2 - 2:  
mrpc: {'accuracy': 0.7034313725490197, 'f1': 0.8207407407407408}  
rte: {'accuracy': 0.5234657039711191}  
cola: {'matthews_correlation': 0.5472224847569017}  

rte_cola_mrpc_2 - 0:  
rte: {'accuracy': 0.7148014440433214}  

rte_cola_mrpc_2 - 1:  
rte: {'accuracy': 0.6173285198555957}  
cola: {'matthews_correlation': 0.5521069582827846}  

rte_cola_mrpc_2 - 2:  
rte: {'accuracy': 0.5018050541516246}  
cola: {'matthews_correlation': 0.3505598620757344}  
mrpc: {'accuracy': 0.8651960784313726, 'f1': 0.9066213921901529}  

rte_mrpc_cola_2 - 0:  
rte: {'accuracy': 0.6823104693140795}  

rte_mrpc_cola_2 - 1:  
rte: {'accuracy': 0.48736462093862815}  
mrpc: {'accuracy': 0.8431372549019608, 'f1': 0.889655172413793}  

rte_mrpc_cola_2 - 2:  
rte: {'accuracy': 0.45126353790613716}  
mrpc: {'accuracy': 0.7034313725490197, 'f1': 0.8202080237741455}  
cola: {'matthews_correlation': 0.5495609631481372}  

cola_mrpc_rte_3 - 0:  
cola: {'matthews_correlation': 0.5651604238862242}  

cola_mrpc_rte_3 - 1:  
cola: {'matthews_correlation': 0.2397048898929288}  
mrpc: {'accuracy': 0.8578431372549019, 'f1': 0.9023569023569024}  

cola_mrpc_rte_3 - 2:  
cola: {'matthews_correlation': -0.20969180477878746}  
mrpc: {'accuracy': 0.23039215686274508, 'f1': 0.0872093023255814}  
rte: {'accuracy': 0.6209386281588448}  

cola_rte_mrpc_3 - 0:  
cola: {'matthews_correlation': 0.5782027446370238}  

cola_rte_mrpc_3 - 1:  
cola: {'matthews_correlation': 0.42542948403678077}  
rte: {'accuracy': 0.7148014440433214}  

cola_rte_mrpc_3 - 2:  
cola: {'matthews_correlation': 0.22075578481145755}  
rte: {'accuracy': 0.5054151624548736}  
mrpc: {'accuracy': 0.8676470588235294, 'f1': 0.9087837837837838}  

mrpc_cola_rte_3 - 0:  
mrpc: {'accuracy': 0.8553921568627451, 'f1': 0.8963093145869947}  

mrpc_cola_rte_3 - 1:  
mrpc: {'accuracy': 0.7401960784313726, 'f1': 0.8389057750759878}  
cola: {'matthews_correlation': 0.5392823485107089}  

mrpc_cola_rte_3 - 2:  
mrpc: {'accuracy': 0.3872549019607843, 'f1': 0.50199203187251}  
cola: {'matthews_correlation': 0.45980625479422976}  
rte: {'accuracy': 0.6462093862815884}  

mrpc_rte_cola_3 - 0:  
mrpc: {'accuracy': 0.8676470588235294, 'f1': 0.9055944055944055}  

mrpc_rte_cola_3 - 1:  
mrpc: {'accuracy': 0.30637254901960786, 'f1': 0.3464203233256351}  
rte: {'accuracy': 0.7364620938628159}  

mrpc_rte_cola_3 - 2:  
mrpc: {'accuracy': 0.5612745098039216, 'f1': 0.6950596252129473}  
rte: {'accuracy': 0.5667870036101083}  
cola: {'matthews_correlation': 0.5963273779713936}  

rte_cola_mrpc_3 - 0:  
rte: {'accuracy': 0.6389891696750902}  

rte_cola_mrpc_3 - 1:  
rte: {'accuracy': 0.5667870036101083}  
cola: {'matthews_correlation': 0.5676052483913692}  

rte_cola_mrpc_3 - 2:  
rte: {'accuracy': 0.49097472924187724}  
cola: {'matthews_correlation': 0.2859691734342701}  
mrpc: {'accuracy': 0.8602941176470589, 'f1': 0.9025641025641027}  

rte_mrpc_cola_3 - 0:  
rte: {'accuracy': 0.6642599277978339}  

rte_mrpc_cola_3 - 1:  
rte: {'accuracy': 0.48736462093862815}  
mrpc: {'accuracy': 0.8578431372549019, 'f1': 0.9006849315068494}  

rte_mrpc_cola_3 - 2:  
rte: {'accuracy': 0.47653429602888087}  
mrpc: {'accuracy': 0.7083333333333334, 'f1': 0.8226527570789866}  
cola: {'matthews_correlation': 0.5582103540932131}  

cola_mrpc_rte_4 - 0:  
cola: {'matthews_correlation': 0.550090073200501}  

cola_mrpc_rte_4 - 1:  
cola: {'matthews_correlation': 0.26795962945985796}  
mrpc: {'accuracy': 0.8382352941176471, 'f1': 0.8903654485049834}  

cola_mrpc_rte_4 - 2:  
cola: {'matthews_correlation': 0.41051204645145506}  
mrpc: {'accuracy': 0.36519607843137253, 'f1': 0.43817787418655096}  
rte: {'accuracy': 0.6642599277978339}  

cola_rte_mrpc_4 - 0:  
cola: {'matthews_correlation': 0.5756414302422657}  

cola_rte_mrpc_4 - 1:  
cola: {'matthews_correlation': 0.4890768094897263}  
rte: {'accuracy': 0.703971119133574}  

cola_rte_mrpc_4 - 2:  
cola: {'matthews_correlation': 0.26037855591345843}  
rte: {'accuracy': 0.44404332129963897}  
mrpc: {'accuracy': 0.8504901960784313, 'f1': 0.897133220910624}  

mrpc_cola_rte_4 - 0:  
mrpc: {'accuracy': 0.8480392156862745, 'f1': 0.89198606271777}  

mrpc_cola_rte_4 - 1:  
mrpc: {'accuracy': 0.7279411764705882, 'f1': 0.8330827067669173}  
cola: {'matthews_correlation': 0.5443521169935567}  

mrpc_cola_rte_4 - 2:  
mrpc: {'accuracy': 0.3553921568627451, 'f1': 0.459958932238193}  
cola: {'matthews_correlation': 0.43151604879320987}  
rte: {'accuracy': 0.6425992779783394}  

mrpc_rte_cola_4 - 0:  
mrpc: {'accuracy': 0.8651960784313726, 'f1': 0.9050086355785838}  

mrpc_rte_cola_4 - 1:  
mrpc: {'accuracy': 0.5073529411764706, 'f1': 0.5971943887775552}  
rte: {'accuracy': 0.6534296028880866}  

mrpc_rte_cola_4 - 2:  
mrpc: {'accuracy': 0.6715686274509803, 'f1': 0.8023598820058997}  
rte: {'accuracy': 0.48375451263537905}  
cola: {'matthews_correlation': 0.5598518369499322}  

rte_cola_mrpc_4 - 0:  
rte: {'accuracy': 0.6714801444043321}  

rte_cola_mrpc_4 - 1:  
rte: {'accuracy': 0.47653429602888087}  
cola: {'matthews_correlation': 0.544301235611677}  

rte_cola_mrpc_4 - 2:  
rte: {'accuracy': 0.4657039711191336}  
cola: {'matthews_correlation': 0.2819100489786119}  
mrpc: {'accuracy': 0.8651960784313726, 'f1': 0.905982905982906}  

rte_mrpc_cola_4 - 0:  
rte: {'accuracy': 0.6859205776173285}  

rte_mrpc_cola_4 - 1:  
rte: {'accuracy': 0.49458483754512633}  
mrpc: {'accuracy': 0.8529411764705882, 'f1': 0.8996655518394648}  

rte_mrpc_cola_4 - 2:  
rte: {'accuracy': 0.48375451263537905}  
mrpc: {'accuracy': 0.7205882352941176, 'f1': 0.8298507462686568}  
cola: {'matthews_correlation': 0.5410897632107913}  

cola_mrpc_rte_5 - 0:  
cola: {'matthews_correlation': 0.5469075065870133}  

cola_mrpc_rte_5 - 1:  
cola: {'matthews_correlation': 0.25450281992011237}  
mrpc: {'accuracy': 0.8504901960784313, 'f1': 0.8967851099830796}  

cola_mrpc_rte_5 - 2:  
cola: {'matthews_correlation': 0.42619630479463927}  
mrpc: {'accuracy': 0.4019607843137255, 'f1': 0.5325670498084292}  
rte: {'accuracy': 0.6245487364620939}  

cola_rte_mrpc_5 - 0:  
cola: {'matthews_correlation': 0.5401724857356367}  

cola_rte_mrpc_5 - 1:  
cola: {'matthews_correlation': 0.415988488086018}  
rte: {'accuracy': 0.6967509025270758}  

cola_rte_mrpc_5 - 2:  
cola: {'matthews_correlation': 0.350177745448582}  
rte: {'accuracy': 0.4223826714801444}  
mrpc: {'accuracy': 0.8480392156862745, 'f1': 0.8938356164383561}  

mrpc_cola_rte_5 - 0:  
mrpc: {'accuracy': 0.8235294117647058, 'f1': 0.8767123287671232}  

mrpc_cola_rte_5 - 1:  
mrpc: {'accuracy': 0.6936274509803921, 'f1': 0.8169838945827232}  
cola: {'matthews_correlation': 0.5213763355102656}  

mrpc_cola_rte_5 - 2:  
mrpc: {'accuracy': 0.5098039215686274, 'f1': 0.6389891696750902}  
cola: {'matthews_correlation': 0.4911444953794644}  
rte: {'accuracy': 0.5848375451263538}  

mrpc_rte_cola_5 - 0:  
mrpc: {'accuracy': 0.8284313725490197, 'f1': 0.8776223776223777}  

mrpc_rte_cola_5 - 1:  
mrpc: {'accuracy': 0.3897058823529412, 'f1': 0.5088757396449705}  
rte: {'accuracy': 0.6101083032490975}  

mrpc_rte_cola_5 - 2:  
mrpc: {'accuracy': 0.6838235294117647, 'f1': 0.8088888888888889}  
rte: {'accuracy': 0.48014440433212996}  
cola: {'matthews_correlation': 0.5213763355102656}  

rte_cola_mrpc_5 - 0:  
rte: {'accuracy': 0.6931407942238267}  

rte_cola_mrpc_5 - 1:  
rte: {'accuracy': 0.6823104693140795}  
cola: {'matthews_correlation': 0.5469587051515413}  

rte_cola_mrpc_5 - 2:  
rte: {'accuracy': 0.4657039711191336}  
cola: {'matthews_correlation': 0.37581385432861003}  
mrpc: {'accuracy': 0.8259803921568627, 'f1': 0.8814691151919867}  

rte_mrpc_cola_5 - 0:  
rte: {'accuracy': 0.6606498194945848}  

rte_mrpc_cola_5 - 1:  
rte: {'accuracy': 0.5090252707581228}  
mrpc: {'accuracy': 0.8553921568627451, 'f1': 0.9005059021922428}  

rte_mrpc_cola_5 - 2:  
rte: {'accuracy': 0.4657039711191336}  
mrpc: {'accuracy': 0.6887254901960784, 'f1': 0.8145985401459854}  
cola: {'matthews_correlation': 0.5179821135635028}  

cola_mrpc_rte_6 - 0:  
cola: {'matthews_correlation': 0.5303353676557755}  

cola_mrpc_rte_6 - 1:  
cola: {'matthews_correlation': 0.3142084460645202}  
mrpc: {'accuracy': 0.8455882352941176, 'f1': 0.8911917098445595}  

cola_mrpc_rte_6 - 2:  
cola: {'matthews_correlation': -0.1596079831446598}  
mrpc: {'accuracy': 0.4485294117647059, 'f1': 0.5778611632270169}  
rte: {'accuracy': 0.631768953068592}  

cola_rte_mrpc_6 - 0:  
cola: {'matthews_correlation': 0.5232849512779736}  

cola_rte_mrpc_6 - 1:  
cola: {'matthews_correlation': 0.41297184211144844}  
rte: {'accuracy': 0.6678700361010831}  

cola_rte_mrpc_6 - 2:  
cola: {'matthews_correlation': 0.21431054456499188}  
rte: {'accuracy': 0.5126353790613718}  
mrpc: {'accuracy': 0.8357843137254902, 'f1': 0.8873949579831933}  

mrpc_cola_rte_6 - 0:  
mrpc: {'accuracy': 0.8112745098039216, 'f1': 0.8723051409618573}  

mrpc_cola_rte_6 - 1:  
mrpc: {'accuracy': 0.7598039215686274, 'f1': 0.848297213622291}  
cola: {'matthews_correlation': 0.5077656617867954}  

mrpc_cola_rte_6 - 2:  
mrpc: {'accuracy': 0.34558823529411764, 'f1': 0.4355179704016914}  
cola: {'matthews_correlation': 0.433128798177375}  
rte: {'accuracy': 0.6245487364620939}  

mrpc_rte_cola_6 - 0:  
mrpc: {'accuracy': 0.8112745098039216, 'f1': 0.8683760683760684}  

mrpc_rte_cola_6 - 1:  
mrpc: {'accuracy': 0.5245098039215687, 'f1': 0.6523297491039427}  
rte: {'accuracy': 0.6173285198555957}  

mrpc_rte_cola_6 - 2:  
mrpc: {'accuracy': 0.6911764705882353, 'f1': 0.8141592920353982}  
rte: {'accuracy': 0.516245487364621}  
cola: {'matthews_correlation': 0.5073664747016221}  

rte_cola_mrpc_6 - 0:  
rte: {'accuracy': 0.6678700361010831}  

rte_cola_mrpc_6 - 1:  
rte: {'accuracy': 0.6173285198555957}  
cola: {'matthews_correlation': 0.5262420102371838}  

rte_cola_mrpc_6 - 2:  
rte: {'accuracy': 0.47653429602888087}  
cola: {'matthews_correlation': 0.2601447739717376}  
mrpc: {'accuracy': 0.8284313725490197, 'f1': 0.8844884488448845}  

rte_mrpc_cola_6 - 0:  
rte: {'accuracy': 0.6389891696750902}  

rte_mrpc_cola_6 - 1:  
rte: {'accuracy': 0.36462093862815886}  
mrpc: {'accuracy': 0.821078431372549, 'f1': 0.8760611205432938}  

rte_mrpc_cola_6 - 2:  
rte: {'accuracy': 0.37545126353790614}  
mrpc: {'accuracy': 0.7573529411764706, 'f1': 0.8483920367534455}  
cola: {'matthews_correlation': 0.5265067723079826}  

cola_mrpc_rte_7 - 0:  
cola: {'matthews_correlation': 0.5154446997281555}  

cola_mrpc_rte_7 - 1:  
cola: {'matthews_correlation': 0.28103043475860734}  
mrpc: {'accuracy': 0.8529411764705882, 'f1': 0.8996655518394648}  

cola_mrpc_rte_7 - 2:  
cola: {'matthews_correlation': -0.10138489103947196}  
mrpc: {'accuracy': 0.2696078431372549, 'f1': 0.23589743589743592}  
rte: {'accuracy': 0.5740072202166066}  

cola_rte_mrpc_7 - 0:  
cola: {'matthews_correlation': 0.4965380296929026}  

cola_rte_mrpc_7 - 1:  
cola: {'matthews_correlation': 0.41487051230490074}  
rte: {'accuracy': 0.6714801444043321}  

cola_rte_mrpc_7 - 2:  
cola: {'matthews_correlation': 0.17505457701334956}  
rte: {'accuracy': 0.4620938628158845}  
mrpc: {'accuracy': 0.7867647058823529, 'f1': 0.8532883642495784}  

mrpc_cola_rte_7 - 0:  
mrpc: {'accuracy': 0.7769607843137255, 'f1': 0.842832469775475}  

mrpc_cola_rte_7 - 1:  
mrpc: {'accuracy': 0.6936274509803921, 'f1': 0.8169838945827232}  
cola: {'matthews_correlation': 0.5157664784865402}  

mrpc_cola_rte_7 - 2:  
mrpc: {'accuracy': 0.4166666666666667, 'f1': 0.5423076923076923}  
cola: {'matthews_correlation': 0.4245984455514523}  
rte: {'accuracy': 0.631768953068592}  

mrpc_rte_cola_7 - 0:  
mrpc: {'accuracy': 0.8357843137254902, 'f1': 0.8854700854700854}  

mrpc_rte_cola_7 - 1:  
mrpc: {'accuracy': 0.42892156862745096, 'f1': 0.5578747628083491}  
rte: {'accuracy': 0.6137184115523465}  

mrpc_rte_cola_7 - 2:  
mrpc: {'accuracy': 0.6911764705882353, 'f1': 0.8157894736842105}  
rte: {'accuracy': 0.47653429602888087}  
cola: {'matthews_correlation': 0.4883991757826137}  

rte_cola_mrpc_7 - 0:  
rte: {'accuracy': 0.628158844765343}  

rte_cola_mrpc_7 - 1:  
rte: {'accuracy': 0.47653429602888087}  
cola: {'matthews_correlation': 0.49920513654867127}  

rte_cola_mrpc_7 - 2:  
rte: {'accuracy': 0.4584837545126354}  
cola: {'matthews_correlation': 0.27009610918793603}  
mrpc: {'accuracy': 0.7916666666666666, 'f1': 0.8537005163511187}  

rte_mrpc_cola_7 - 0:  
rte: {'accuracy': 0.6353790613718412}  

rte_mrpc_cola_7 - 1:  
rte: {'accuracy': 0.48014440433212996}  
mrpc: {'accuracy': 0.8063725490196079, 'f1': 0.8654173764906303}  

rte_mrpc_cola_7 - 2:  
rte: {'accuracy': 0.4620938628158845}  
mrpc: {'accuracy': 0.6985294117647058, 'f1': 0.8193832599118943}  
cola: {'matthews_correlation': 0.4695101101903524}  

cola_mrpc_rte_8 - 0:  
cola: {'matthews_correlation': 0.4775646295364916}  

cola_mrpc_rte_8 - 1:  
cola: {'matthews_correlation': 0.15815771045471538}  
mrpc: {'accuracy': 0.8284313725490197, 'f1': 0.8825503355704698}  

cola_mrpc_rte_8 - 2:  
cola: {'matthews_correlation': -0.27535643529039394}  
mrpc: {'accuracy': 0.20833333333333334, 'f1': 0.16966580976863754}  
rte: {'accuracy': 0.6678700361010831}  

cola_rte_mrpc_8 - 0:  
cola: {'matthews_correlation': 0.480402445933886}  

cola_rte_mrpc_8 - 1:  
cola: {'matthews_correlation': 0.36689045725372754}  
rte: {'accuracy': 0.6173285198555957}  

cola_rte_mrpc_8 - 2:  
cola: {'matthews_correlation': 0.19338822496976396}  
rte: {'accuracy': 0.4223826714801444}  
mrpc: {'accuracy': 0.8333333333333334, 'f1': 0.8855218855218856}  

mrpc_cola_rte_8 - 0:  
mrpc: {'accuracy': 0.8063725490196079, 'f1': 0.8685524126455907}  

mrpc_cola_rte_8 - 1:  
mrpc: {'accuracy': 0.75, 'f1': 0.8440366972477065}  
cola: {'matthews_correlation': 0.4582069079338325}  

mrpc_cola_rte_8 - 2:  
mrpc: {'accuracy': 0.375, 'f1': 0.4608879492600423}  
cola: {'matthews_correlation': 0.2541842563618766}  
rte: {'accuracy': 0.5884476534296029}  

mrpc_rte_cola_8 - 0:  
mrpc: {'accuracy': 0.7916666666666666, 'f1': 0.8585690515806987}  

mrpc_rte_cola_8 - 1:  
mrpc: {'accuracy': 0.33088235294117646, 'f1': 0.40780911062906733}  
rte: {'accuracy': 0.6895306859205776}  

mrpc_rte_cola_8 - 2:  
mrpc: {'accuracy': 0.6274509803921569, 'f1': 0.7689969604863223}  
rte: {'accuracy': 0.6064981949458483}  
cola: {'matthews_correlation': 0.4861356803540783}  

rte_cola_mrpc_8 - 0:  
rte: {'accuracy': 0.6209386281588448}  

rte_cola_mrpc_8 - 1:  
rte: {'accuracy': 0.6570397111913358}  
cola: {'matthews_correlation': 0.5236201884746546}  

rte_cola_mrpc_8 - 2:  
rte: {'accuracy': 0.4548736462093863}  
cola: {'matthews_correlation': 0.29004509558107944}  
mrpc: {'accuracy': 0.7696078431372549, 'f1': 0.8443708609271523}  

rte_mrpc_cola_8 - 0:  
rte: {'accuracy': 0.6462093862815884}  

rte_mrpc_cola_8 - 1:  
rte: {'accuracy': 0.4296028880866426}  
mrpc: {'accuracy': 0.7965686274509803, 'f1': 0.8641571194762684}  

rte_mrpc_cola_8 - 2:  
rte: {'accuracy': 0.4404332129963899}  
mrpc: {'accuracy': 0.7671568627450981, 'f1': 0.8499210110584519}  
cola: {'matthews_correlation': 0.4832593692802084}  

cola_mrpc_rte_9 - 0:  
cola: {'matthews_correlation': 0.3711969872541337}  

cola_mrpc_rte_9 - 1:  
cola: {'matthews_correlation': 0.2979908488120295}  
mrpc: {'accuracy': 0.7720588235294118, 'f1': 0.848780487804878}  

cola_mrpc_rte_9 - 2:  
cola: {'matthews_correlation': 0.058936921430734465}  
mrpc: {'accuracy': 0.5686274509803921, 'f1': 0.7114754098360656}  
rte: {'accuracy': 0.6028880866425993}  

cola_rte_mrpc_9 - 0:  
cola: {'matthews_correlation': 0.4385781021525937}  

cola_rte_mrpc_9 - 1:  
cola: {'matthews_correlation': 0.27897770658318977}  
rte: {'accuracy': 0.5992779783393501}  

cola_rte_mrpc_9 - 2:  
cola: {'matthews_correlation': 0.23948417069535177}  
rte: {'accuracy': 0.4187725631768953}  
mrpc: {'accuracy': 0.8161764705882353, 'f1': 0.8764415156507415}  

mrpc_cola_rte_9 - 0:  
mrpc: {'accuracy': 0.7867647058823529, 'f1': 0.8552412645590682}  

mrpc_cola_rte_9 - 1:  
mrpc: {'accuracy': 0.7205882352941176, 'f1': 0.8303571428571428}  
cola: {'matthews_correlation': 0.42602448983421265}  

mrpc_cola_rte_9 - 2:  
mrpc: {'accuracy': 0.42401960784313725, 'f1': 0.48801742919389984}  
cola: {'matthews_correlation': 0.3346018596839432}  
rte: {'accuracy': 0.6173285198555957}  

mrpc_rte_cola_9 - 0:  
mrpc: {'accuracy': 0.7843137254901961, 'f1': 0.8585209003215434}  

mrpc_rte_cola_9 - 1:  
mrpc: {'accuracy': 0.3553921568627451, 'f1': 0.33753148614609574}  
rte: {'accuracy': 0.6498194945848376}  

mrpc_rte_cola_9 - 2:  
mrpc: {'accuracy': 0.6372549019607843, 'f1': 0.7716049382716049}  
rte: {'accuracy': 0.6101083032490975}  
cola: {'matthews_correlation': 0.4388929111721164}  

rte_cola_mrpc_9 - 0:  
rte: {'accuracy': 0.5631768953068592}  

rte_cola_mrpc_9 - 1:  
rte: {'accuracy': 0.6137184115523465}  
cola: {'matthews_correlation': 0.43090580601943307}  

rte_cola_mrpc_9 - 2:  
rte: {'accuracy': 0.47653429602888087}  
cola: {'matthews_correlation': 0.3969979313457839}  
mrpc: {'accuracy': 0.7843137254901961, 'f1': 0.8503401360544217}  

rte_mrpc_cola_9 - 0:  
rte: {'accuracy': 0.5956678700361011}  

rte_mrpc_cola_9 - 1:  
rte: {'accuracy': 0.38267148014440433}  
mrpc: {'accuracy': 0.7941176470588235, 'f1': 0.8636363636363636}  

rte_mrpc_cola_9 - 2:  
rte: {'accuracy': 0.4620938628158845}  
mrpc: {'accuracy': 0.7254901960784313, 'f1': 0.8328358208955223}  
cola: {'matthews_correlation': 0.4256708585820189}  

cola_mrpc_rte_10 - 0:  
cola: {'matthews_correlation': 0.41844170047016394}  

cola_mrpc_rte_10 - 1:  
cola: {'matthews_correlation': 0.14425904763364952}  
mrpc: {'accuracy': 0.7671568627450981, 'f1': 0.848966613672496}  

cola_mrpc_rte_10 - 2:  
cola: {'matthews_correlation': 0.2710150084163296}  
mrpc: {'accuracy': 0.6495098039215687, 'f1': 0.7265774378585086}  
rte: {'accuracy': 0.6101083032490975}  

cola_rte_mrpc_10 - 0:  
cola: {'matthews_correlation': 0.41297184211144844}  

cola_rte_mrpc_10 - 1:  
cola: {'matthews_correlation': 0.29065642768956923}  
rte: {'accuracy': 0.6028880866425993}  

cola_rte_mrpc_10 - 2:  
cola: {'matthews_correlation': 0.27145259521558346}  
rte: {'accuracy': 0.45126353790613716}  
mrpc: {'accuracy': 0.7745098039215687, 'f1': 0.8525641025641025}  

mrpc_cola_rte_10 - 0:  
mrpc: {'accuracy': 0.7598039215686274, 'f1': 0.8434504792332268}  

mrpc_cola_rte_10 - 1:  
mrpc: {'accuracy': 0.7083333333333334, 'f1': 0.8237037037037037}  
cola: {'matthews_correlation': 0.40756536011513605}  

mrpc_cola_rte_10 - 2:  
mrpc: {'accuracy': 0.3480392156862745, 'f1': 0.4166666666666667}  
cola: {'matthews_correlation': 0.15230980268138064}  
rte: {'accuracy': 0.6173285198555957}  

mrpc_rte_cola_10 - 0:  
mrpc: {'accuracy': 0.7671568627450981, 'f1': 0.846029173419773}  

mrpc_rte_cola_10 - 1:  
mrpc: {'accuracy': 0.7205882352941176, 'f1': 0.8272727272727272}  
rte: {'accuracy': 0.5631768953068592}  

mrpc_rte_cola_10 - 2:  
mrpc: {'accuracy': 0.7009803921568627, 'f1': 0.8205882352941176}  
rte: {'accuracy': 0.49458483754512633}  
cola: {'matthews_correlation': 0.42827863284737194}  

rte_cola_mrpc_10 - 0:  
rte: {'accuracy': 0.5776173285198556}  

rte_cola_mrpc_10 - 1:  
rte: {'accuracy': 0.5703971119133574}  
cola: {'matthews_correlation': 0.3456014554543514}  

rte_cola_mrpc_10 - 2:  
rte: {'accuracy': 0.4368231046931408}  
cola: {'matthews_correlation': 0.33955120211045303}  
mrpc: {'accuracy': 0.7696078431372549, 'f1': 0.8517350157728708}  

rte_mrpc_cola_10 - 0:  
rte: {'accuracy': 0.5740072202166066}  

rte_mrpc_cola_10 - 1:  
rte: {'accuracy': 0.51985559566787}  
mrpc: {'accuracy': 0.7598039215686274, 'f1': 0.8414239482200647}  

rte_mrpc_cola_10 - 2:  
rte: {'accuracy': 0.4729241877256318}  
mrpc: {'accuracy': 0.6887254901960784, 'f1': 0.8145985401459854}  
cola: {'matthews_correlation': 0.3578937157927108}  

cola_mrpc_rte_11 - 0:  
cola: {'matthews_correlation': 0.35438435663325374}  

cola_mrpc_rte_11 - 1:  
cola: {'matthews_correlation': 0.40876295717276734}  
mrpc: {'accuracy': 0.7426470588235294, 'f1': 0.8367029548989114}  

cola_mrpc_rte_11 - 2:  
cola: {'matthews_correlation': 0.2845045651100063}  
mrpc: {'accuracy': 0.35294117647058826, 'f1': 0.24571428571428575}  
rte: {'accuracy': 0.5848375451263538}  

cola_rte_mrpc_11 - 0:  
cola: {'matthews_correlation': 0.37750627539529985}  

cola_rte_mrpc_11 - 1:  
cola: {'matthews_correlation': 0.2934528241562536}  
rte: {'accuracy': 0.5740072202166066}  

cola_rte_mrpc_11 - 2:  
cola: {'matthews_correlation': 0.42245216492948245}  
rte: {'accuracy': 0.4368231046931408}  
mrpc: {'accuracy': 0.7352941176470589, 'f1': 0.8317757009345794}  

mrpc_cola_rte_11 - 0:  
mrpc: {'accuracy': 0.7426470588235294, 'f1': 0.8341232227488151}  

mrpc_cola_rte_11 - 1:  
mrpc: {'accuracy': 0.6887254901960784, 'f1': 0.8145985401459854}  
cola: {'matthews_correlation': 0.36040233309888925}  

mrpc_cola_rte_11 - 2:  
mrpc: {'accuracy': 0.678921568627451, 'f1': 0.808199121522694}  
cola: {'matthews_correlation': 0.2756601711602064}  
rte: {'accuracy': 0.5703971119133574}  

mrpc_rte_cola_11 - 0:  
mrpc: {'accuracy': 0.7279411764705882, 'f1': 0.8183306055646481}  

mrpc_rte_cola_11 - 1:  
mrpc: {'accuracy': 0.5220588235294118, 'f1': 0.5714285714285714}  
rte: {'accuracy': 0.6064981949458483}  

mrpc_rte_cola_11 - 2:  
mrpc: {'accuracy': 0.6985294117647058, 'f1': 0.8183161004431315}  
rte: {'accuracy': 0.4981949458483754}  
cola: {'matthews_correlation': 0.3659239525121057}  

rte_cola_mrpc_11 - 0:  
rte: {'accuracy': 0.5812274368231047}  

rte_cola_mrpc_11 - 1:  
rte: {'accuracy': 0.48375451263537905}  
cola: {'matthews_correlation': 0.3626982030225937}  

rte_cola_mrpc_11 - 2:  
rte: {'accuracy': 0.41155234657039713}  
cola: {'matthews_correlation': 0.2153640632671545}  
mrpc: {'accuracy': 0.7205882352941176, 'f1': 0.8256880733944955}  

rte_mrpc_cola_11 - 0:  
rte: {'accuracy': 0.5848375451263538}  

rte_mrpc_cola_11 - 1:  
rte: {'accuracy': 0.4296028880866426}  
mrpc: {'accuracy': 0.7352941176470589, 'f1': 0.8312499999999999}  

rte_mrpc_cola_11 - 2:  
rte: {'accuracy': 0.4729241877256318}  
mrpc: {'accuracy': 0.6911764705882353, 'f1': 0.8157894736842105}  
cola: {'matthews_correlation': 0.3738775071170718}  

cola_mrpc_rte_12 - 0:  
cola: {'matthews_correlation': 0.23086580985196306}  

cola_mrpc_rte_12 - 1:  
cola: {'matthews_correlation': 0.020702674026557004}  
mrpc: {'accuracy': 0.6887254901960784, 'f1': 0.8140556368960467}  

cola_mrpc_rte_12 - 2:  
cola: {'matthews_correlation': 0.409237984741568}  
mrpc: {'accuracy': 0.6838235294117647, 'f1': 0.8122270742358079}  
rte: {'accuracy': 0.516245487364621}  

cola_rte_mrpc_12 - 0:  
cola: {'matthews_correlation': 0.21965351926652088}  

cola_rte_mrpc_12 - 1:  
cola: {'matthews_correlation': 0.08036809130702588}  
rte: {'accuracy': 0.555956678700361}  

cola_rte_mrpc_12 - 2:  
cola: {'matthews_correlation': 0.09017048020720095}  
rte: {'accuracy': 0.5270758122743683}  
mrpc: {'accuracy': 0.6862745098039216, 'f1': 0.8128654970760235}  

mrpc_cola_rte_12 - 0:  
mrpc: {'accuracy': 0.6838235294117647, 'f1': 0.8122270742358079}  

mrpc_cola_rte_12 - 1:  
mrpc: {'accuracy': 0.6838235294117647, 'f1': 0.8122270742358079}  
cola: {'matthews_correlation': 0.23086580985196306}  

mrpc_cola_rte_12 - 2:  
mrpc: {'accuracy': 0.6838235294117647, 'f1': 0.8122270742358079}  
cola: {'matthews_correlation': 0.11382192951310593}  
rte: {'accuracy': 0.5234657039711191}  

mrpc_rte_cola_12 - 0:  
mrpc: {'accuracy': 0.6911764705882353, 'f1': 0.8157894736842105}  

mrpc_rte_cola_12 - 1:  
mrpc: {'accuracy': 0.6838235294117647, 'f1': 0.8122270742358079}  
rte: {'accuracy': 0.5270758122743683}  

mrpc_rte_cola_12 - 2:  
mrpc: {'accuracy': 0.6838235294117647, 'f1': 0.8122270742358079}  
rte: {'accuracy': 0.4729241877256318}  
cola: {'matthews_correlation': 0.23267650715203794}  

rte_cola_mrpc_12 - 0:  
rte: {'accuracy': 0.5595667870036101}  

rte_cola_mrpc_12 - 1:  
rte: {'accuracy': 0.5740072202166066}  
cola: {'matthews_correlation': 0.23449620132890608}  

rte_cola_mrpc_12 - 2:  
rte: {'accuracy': 0.5270758122743683}  
cola: {'matthews_correlation': 0.020702674026557004}  
mrpc: {'accuracy': 0.6862745098039216, 'f1': 0.8128654970760235}  

rte_mrpc_cola_12 - 0:  
rte: {'accuracy': 0.555956678700361}  

rte_mrpc_cola_12 - 1:  
rte: {'accuracy': 0.5270758122743683}  
mrpc: {'accuracy': 0.6887254901960784, 'f1': 0.8145985401459854}  

rte_mrpc_cola_12 - 2:  
rte: {'accuracy': 0.48375451263537905}  
mrpc: {'accuracy': 0.6838235294117647, 'f1': 0.8122270742358079}  
cola: {'matthews_correlation': 0.2557834132889666}  

