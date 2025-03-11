#!/bin/bash
#SBATCH --job-name=compare_scd_split_tape
#SBATCH --error=/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/scd_vs_splitcode_tape/compare_scd_split_tape_%A%a.err
#SBATCH --output=/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/scd_vs_splitcode_tape/compare_scd_split_tape_%A%a.out
#SBATCH --partition=binf
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16              # Number of CPU cores per task
#SBATCH --time=60:00:00
#SBATCH --mail-user=theodosiadou.ana@gmail.com  # Email
#SBATCH --mail-type=END,FAIL               # Email notification on job end or fail


gzip ./RESULTS/Demultiplexed_MAPPING_1_1.tsv
gzip ./RESULTS/Demultiplexed_MAPPING_1_2.tsv
gzip ./RESULTS/Demultiplexed_MAPPING_1_3.tsv
gzip ./RESULTS/Demultiplexed_MAPPING_1_4.tsv
gzip ./RESULTS/Demultiplexed_MAPPING_1_5.tsv
gzip ./RESULTS/Demultiplexed_MAPPING_1_6.tsv

/scistor/informatica/ath100/SCDemultiplexing_Benchmark/tools/SCDemultiplexingPipeline/bin/processing -i ./Demultiplexed_TAPE_RESULT.tsv.gz -o ./ABCOUNT.tsv -b /scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/tape_data/barcodes_tape.txt -a /scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/tape_data/antibodies.txt -x 0 -c 1,2,3 -u 0 -t 60