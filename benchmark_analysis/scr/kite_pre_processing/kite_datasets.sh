#!/bin/bash
#SBATCH --job-name=kite_datasets
#SBATCH --error=/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/kite/kite_datasets_%A%a.err  # Error file location
#SBATCH --output=/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/kite/kite_datasets_%A%a.out # Output file location
#SBATCH --partition=binf
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16              # Number of CPU cores per task
#SBATCH --time=60:00:00
#SBATCH --mail-user=theodosiadou.ana@gmail.com  # Email
#SBATCH --mail-type=END,FAIL               # Email notification on job end or fail

echo "Running first script..."
python /scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/scr/kITE_merge_by_name_OG_linker.py

echo "Running second script..."
python /scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/scr/kITE_merge_by_name_linker.py

echo "Running third script..."
python /scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/scr/kITE_merge_by_name_ab.py


echo "Running fourth script..."
python /scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/scr/kITE_merge_by_name_linker_ab.py

echo "DONE"
