#!/bin/bash
#SBATCH --job-name=repeater
#SBATCH -c 1
#SBATCH -N 1
#SBATCH -t 0-10:00              # Runtime in D-HH:MM, minimum of 10 minutes
#SBATCH -p gpu                  # Partition to submit to
#SBATCH --gres=gpu:1            # How many GPUs do you want
#SBATCH --constraint=a100
#SBATCH --mem=128GB

#SBATCH -o /n/home06/zhentingqi/slurm_out/repeater_%j.out      # File to which STDOUT will be written, %j inserts jobid
#SBATCH -e /n/home06/zhentingqi/slurm_out/repeater_%j.err      # File to which STDERR will be written, %j inserts jobid

#SBATCH --mail-type=FAIL
#SBATCH --mail-user=zhentingqi@g.harvard.edu

# --- load env here ---
module load python/3.10.12-fasrc01
source activate
source activate gcg_scratch
# ---------------------

python -c 'print("Hi Zhenting. Your job is running!")'

# --- run your code here ---
# srun -c 1 --gres=gpu:1 python main.py
llama_model="meta-llama/Llama-2-7b-chat-hf"
python carve_sigil.py name=llama2_gcg_repeat wandb.tags=[extraction] model=${llama_model} optimizer=gcg sigil.num_tokens=32 sigil=repeater optimizer.steps=400

# --------------------------

python -c 'print("Hi Zhenting. Everything is done!")'
