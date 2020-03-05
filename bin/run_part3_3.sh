#!/bin/bash
#$ -cwd
#$ -N p3_3
#$ -o ../output/part3_3.txt
#$ -j y
#$ -l h_data=1500M,h_rt=02:00:00,h_vmem=12000
#$ -pe shared 8
#$ -t 1-500:1

. /u/local/Modules/default/init/modules.sh
module load python/anaconda3

source activate rdkit

python ../macrocycles/run_part3.py --peptide_len 3 --num_jobs 500 --num $SGE_TASK_ID --tp_out ../output/part2_3.txt > ../output/part3_3_${SGE_TASK_ID}.txt