prun_jobs.py -c "python3 efficiency_Rp_data17_13TeV_data_EGAM1.py" -mt 30  -i /home/edmar.egidio/datasets/physval/data1713TeV_physval/EGAM1/after_ts1/*/*.root
mkdir samples
mv *.root samples
prun_merge.py -i samples/*.root -o efficiency_Rp_data17_13TeV_data_EGAM1.root -mt 30