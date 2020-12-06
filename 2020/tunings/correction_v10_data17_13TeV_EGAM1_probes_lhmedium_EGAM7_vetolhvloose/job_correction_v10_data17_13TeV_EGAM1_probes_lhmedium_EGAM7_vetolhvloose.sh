


command_1="python job_correction_v9_data17_13TeV_EGAM1_probes_lhmedium_EGAM7_vetolhvloose.py --Zee"
command_2="python job_correction_v9_data17_13TeV_EGAM1_probes_lhmedium_EGAM7_vetolhvloose.py --egam7"


BASEPATH_EGAM1='/home/jodafons/public/cern_data/data17_13TeV/PhysVal_v2/EGAM1'
BASEPATH_EGAM7='/home/jodafons/public/cern_data/data17_13TeV/PhysVal_v2/EGAM7'


#prun_jobs.py -i $BASEPATH_EGAM1 -c $command_1 -mt 40
prun_jobs.py -mt 40 -i /home/jodafons/public/cern_data/data17_13TeV/PhysVal_v2/EGAM1/ -c "python job_correction_v10_data17_13TeV_EGAM1_probes_lhmedium_EGAM7_vetolhvloose.py --Zee"
mkdir egam1
prun_merge.py -i output_* -o egam1.root -nm 35 -mt 20
mv *.root egam1




prun_jobs.py -mt 40 -i /home/jodafons/public/cern_data/data17_13TeV/PhysVal_v2/EGAM7/ -c "python job_correction_v10_data17_13TeV_EGAM1_probes_lhmedium_EGAM7_vetolhvloose.py --egam7"
mkdir egam7
prun_merge.py -i output_* -o egam1.root -nm 35 -mt 20
mv *.root egam7




