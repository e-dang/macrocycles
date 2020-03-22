#!/bin/bash
#$ -cwd
#$ -o ../output/rb.txt
#$ -j y
#$ -l h_data=1000M,h_rt=02:00:00,h_vmem=8000M
#$ -pe shared 8
#$ -t 1-1000:1

. /u/local/Modules/default/init/modules.sh
module load python/anaconda3

source activate rdkit

python ../macrocycles/run_descriptors.py --rb --peptide_len 4 --num_jobs 1000 --num ${SGE_TASK_ID} --macrocycle_output ../output/ > ../output/rb4_${SGE_TASK_ID}.txt