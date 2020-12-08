



prun_jobs.py -mt 40 -i /home/jodafons/public/cern_data/data17_13TeV/PhysVal_v2/EGAM1/ -c "python job_correction_v1_el_data17_13TeV_EGAM1_probes_lhmedium_EGAM7_vetolhvloose.py --Zee"
mkdir egam1
prun_merge.py -i output_* -o egam1.root -nm 35 -mt 20
mv *.root egam1




prun_jobs.py -mt 40 -i /home/jodafons/public/cern_data/data17_13TeV/PhysVal_v2/EGAM7/ -c "python job_correction_v1_el_data17_13TeV_EGAM1_probes_lhmedium_EGAM7_vetolhvloose.py --egam7"
mkdir egam7
prun_merge.py -i output_* -o egam7.root -nm 35 -mt 20
mv *.root egam7




