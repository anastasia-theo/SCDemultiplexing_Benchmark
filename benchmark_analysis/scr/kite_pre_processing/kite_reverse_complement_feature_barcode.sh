#!/bin/bash
#SBATCH --job-name=kite_reverse_complement_feature_barcode
#SBATCH --error=/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/kite/joined_linker_ab_NKI/kite_reverse_complement_feature_barcode_%A%a.err  # Error file location
#SBATCH --output=/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/kite/joined_linker_ab_NKI/kite_reverse_complement_feature_barcode_%A%a.out # Output file location
#SBATCH --partition=binf
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16              # Number of CPU cores per task
#SBATCH --time=60:00:00
#SBATCH --mail-user=theodosiadou.ana@gmail.com  # Email
#SBATCH --mail-type=END,FAIL               # Email notification on job end or fail

echo "Running reverse complement script..."
python /scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/scr/kITE_reverse_complement.py

echo "ANALYSIS DONE"