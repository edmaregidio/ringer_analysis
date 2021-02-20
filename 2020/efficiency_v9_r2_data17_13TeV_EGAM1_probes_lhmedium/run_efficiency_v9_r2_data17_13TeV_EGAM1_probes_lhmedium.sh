prun_jobs.py -c "python3 job_efficiency_v9_r2_data17_13TeV_EGAM1_probes_lhmedium.py" -mt 30  -i /home/edmar.egidio/datasets/physval/data1713TeV_physval/EGAM1/*/*/*.root
mkdir samples
mv *.root samples
prun_merge.py -i samples/*.root -o efficiency_v9_r2_data17_13TeV_EGAM1_probes_lhmedium.root -mt 30
