

from prometheus import EventATLAS
from prometheus.enumerations import Dataframe as DataframeEnum
from Gaugi.messenger import LoggingLevel, Logger
from Gaugi import ToolSvc
import argparse
mainLogger = Logger.getModuleLogger("job")
parser = argparse.ArgumentParser(description = '', add_help = False)
parser = argparse.ArgumentParser()


parser.add_argument('-i','--inputFiles', action='store',
    dest='inputFiles', required = True, nargs='+',
    help = "The input files that will be used to generate the plots")

parser.add_argument('-o','--outputFile', action='store',
    dest='outputFile', required = False, default = None,
    help = "The output store name.")

parser.add_argument('-n','--nov', action='store',
    dest='nov', required = False, default = -1, type=int,
    help = "Number of events.")

parser.add_argument('--Zee', action='store_true',
    dest='doZee', required = False,
    help = "Do Zee collection.")

parser.add_argument('--egam7', action='store_true',
    dest='doEgam7', required = False,
    help = "The collected sample came from EGAM7 skemma.")

import sys,os
if len(sys.argv)==1:
  parser.print_help()
  sys.exit(1)

args = parser.parse_args()



acc = EventATLAS( "EventATLASLoop",
                  inputFiles = args.inputFiles,
                  treePath   = '*/HLT/Physval/Egamma/fakes' if args.doEgam7 else '*/HLT/Physval/Egamma/probes',
                  #treePath   = '*/HLT/Egamma/Egamma/fakes' if args.doEgam7 else '*/HLT/Egamma/Egamma/probes',
                  dataframe  = DataframeEnum.Electron_v1,
                  outputFile = args.outputFile,
                  level      = LoggingLevel.INFO,
                  )



from EventSelectionTool import EventSelection, SelectionType, EtCutType

evt = EventSelection('EventSelection')
evt.setCutValue( SelectionType.SelectionOnlineWithRings )
#evt.setCutValue( SelectionType.SelectionOnlineWithTrigElectrons )

# Do not change this!
if args.doEgam7:
  #pidname = '!VeryLooseLLH_DataDriven_Rel21_Run2_2018'
  pidname = '!el_lhvloose'
else:
  #pidname = 'MediumLLH_DataDriven_Rel21_Run2_2018'
  pidname = 'el_lhmedium'


evt.setCutValue( SelectionType.SelectionPID, pidname )
evt.setCutValue( EtCutType.L2CaloAbove , 15)
ToolSvc += evt


# Install ringer v6
#from TrigEgammaEmulationTool import installElectronL2CaloRingerSelector_v6
#installElectronL2CaloRingerSelector_v6()

# Install ringer v8
#from TrigEgammaEmulationTool import installElectronL2CaloRingerSelector_v8
#installElectronL2CaloRingerSelector_v8()

# Install ringer v9
from TrigEgammaEmulationTool import installElectronL2CaloRingerSelector_v9
#installElectronL2CaloRingerSelector_v9()

# Install ringer v10
from TrigEgammaEmulationTool import installElectronL2CaloRingerSelector_v10
installElectronL2CaloRingerSelector_v10()

# Install ringer v11
from TrigEgammaEmulationTool import installElectronL2CaloRingerSelector_v11
#installElectronL2CaloRingerSelector_v11()

# Install ringer v1_el
from TrigEgammaEmulationTool import installElectronL2CaloRingerSelector_v1_el
#installElectronL2CaloRingerSelector_v1_el()

# Install ringer v2_el
from TrigEgammaEmulationTool import installElectronL2CaloRingerSelector_v2_el
#installElectronL2CaloRingerSelector_v2_el()

# Install trigger e/g fastcalo cut-based selector (T2Calo)
from TrigEgammaEmulationTool import installTrigEgammaL2CaloSelectors
installTrigEgammaL2CaloSelectors()


from PileupCorrectionTools import PileupCorrectionTool, Target
alg = PileupCorrectionTool( 'PileupCorrection' , IsBackground = True if args.doEgam7 else False)

targets = [
            # set v9 to be like the legacy cutbased
            #Target( 'L2_Tight_v9' , 'T0HLTElectronRingerTight_v9' , "T0HLTElectronT2CaloTight"  ) ,
            #Target( 'L2_Medium_v9', 'T0HLTElectronRingerTight_v9' , "T0HLTElectronT2CaloMedium" ) ,
            #Target( 'L2_Loose_v9' , 'T0HLTElectronRingerTight_v9' , "T0HLTElectronT2CaloLoose"  ) ,
            #Target( 'L2_VLoose_v9', 'T0HLTElectronRingerTight_v9' , "T0HLTElectronT2CaloVLoose" ) ,
            # set v10 to be like the legacy cutbased
            Target( 'L2_Tight_v10' , 'T0HLTElectronRingerTight_v10' , "T0HLTElectronT2CaloTight"  ) ,
            Target( 'L2_Medium_v10', 'T0HLTElectronRingerTight_v10' , "T0HLTElectronT2CaloMedium" ) ,
            Target( 'L2_Loose_v10' , 'T0HLTElectronRingerTight_v10' , "T0HLTElectronT2CaloLoose"  ) ,
            Target( 'L2_VLoose_v10', 'T0HLTElectronRingerTight_v10' , "T0HLTElectronT2CaloVLoose" ) ,
            # set v10 to be like the legacy cutbased
            #Target( 'L2_Tight_v11' , 'T0HLTElectronRingerTight_v11' , "T0HLTElectronT2CaloTight"  ) ,
            #Target( 'L2_Medium_v11', 'T0HLTElectronRingerTight_v11' , "T0HLTElectronT2CaloMedium" ) ,
            #Target( 'L2_Loose_v11' , 'T0HLTElectronRingerTight_v11' , "T0HLTElectronT2CaloLoose"  ) ,
            #Target( 'L2_VLoose_v11', 'T0HLTElectronRingerTight_v11' , "T0HLTElectronT2CaloVLoose" ) ,
            ## set v10 to be like the legacy cutbased
            #Target( 'L2_Tight_v1_el' , 'T0HLTElectronRingerTight_v1_el' , "T0HLTElectronT2CaloTight"  ) ,
            #Target( 'L2_Medium_v1_el', 'T0HLTElectronRingerTight_v1_el' , "T0HLTElectronT2CaloMedium" ) ,
            #Target( 'L2_Loose_v1_el' , 'T0HLTElectronRingerTight_v1_el' , "T0HLTElectronT2CaloLoose"  ) ,
            #Target( 'L2_VLoose_v1_el', 'T0HLTElectronRingerTight_v1_el' , "T0HLTElectronT2CaloVLoose" ) ,
            ## set v10 to be like the legacy cutbased
            #Target( 'L2_Tight_v2_el' , 'T0HLTElectronRingerTight_v2_el' , "T0HLTElectronT2CaloTight"  ) ,
            #Target( 'L2_Medium_v2_el', 'T0HLTElectronRingerTight_v2_el' , "T0HLTElectronT2CaloMedium" ) ,
            #Target( 'L2_Loose_v2_el' , 'T0HLTElectronRingerTight_v2_el' , "T0HLTElectronT2CaloLoose"  ) ,
            #Target( 'L2_VLoose_v2_el', 'T0HLTElectronRingerTight_v2_el' , "T0HLTElectronT2CaloVLoose" ) ,

        ]

for t in targets:
  alg.addTarget( t )

etbins  = [15.0, 20.0, 30.0, 40.0, 50.0, 1000000.0]
etabins = [0.0, 0.8, 1.37, 1.54, 2.37, 2.50]
alg.setHistogram2DRegion( -16, 16, 0, 70, 0.02, 0.5 )
alg.setEtBinningValues( etbins   )
alg.setEtaBinningValues( etabins )

ToolSvc += alg
acc.run(args.nov)








