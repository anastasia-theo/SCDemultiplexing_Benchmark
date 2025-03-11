#!/bin/bash
#SBATCH --job-name=SCDemultiplex_benchmark_tape
#SBATCH --error=/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/SCDemultiplex_results/tape_dataset/SCDemultiplex_benchmark_tape_%A%a.err  # Error file location
#SBATCH --output=/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/SCDemultiplex_results/tape_dataset/SCDemultiplex_benchmark_tape_%A%a.out # Output file location
#SBATCH --partition=binf
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16              # Number of CPU cores per task
#SBATCH --time=60:00:00
#SBATCH --mail-user=theodosiadou.ana@gmail.com  # Email
#SBATCH --mail-type=END,FAIL               # Email notification on job end or fail

# create the input and output paths and variables

TOOL_PATH="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/tools/SCDemultiplexingPipeline/bin/demultiplexing"
FASTQ_FILE_F="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/tape_data/filtered_SRR28056728_1.fastq"
FASTQ_FILE_R="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/tape_data/filtered_SRR28056728_2.fastq"
BARCODE_FILE="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/tape_data/barcodes_tape.txt"
RESULTS_DIR="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/SCDemultiplex_results/tape_dataset"
TIME_LOG="$RESULTS_DIR/time_log.txt"
MEMORY_LOG="$RESULTS_DIR/memory_log.txt"


mkdir -p "$RESULTS_DIR" # we want to ensure that this directory exists

echo "Mismatch Elapsed_Time(s) User_time(s) System_time(s) Total_CPU_time(s)" > "$TIME_LOG"
echo "Mismatch Max_Memory(KB)" > "$MEMORY_LOG"

# Define pattern and thread count
PATTERN="[NNNNNNNNNNNNNNN][*][NNNNNNNN][CCACAGTCTCAAGCACGTGGAT][NNNNNNNN][AGTCGTACGCCGATGCGAAACATCGGCCAC][NNNNNNNN][XXXXXXXXXX]"
THREAD_COUNT=60

# Loop through mismatch values (e.g., from 0 to 5)
for mismatch in {1..5}; do
    echo "Running demultiplexing for mismatch=$mismatch..."

    # Output paths for each mismatch
    OUTPUT_MAPPING="$RESULTS_DIR/MAPPING_${mismatch}.tsv"
    OUTPUT_FILE="$RESULTS_DIR/Demultiplexed_MAPPING_${mismatch}.tsv"
    RESOURCE_LOG="$RESULTS_DIR/resource_mismatch_${mismatch}.log"
    STATS_FILE="$RESULTS_DIR/stats_mismatch_${mismatch}.txt"
    SUMMARY_LOG="$RESULTS_DIR/true_false_summary_${mismatch}.txt"

    start_time=$(date +%s%N)

    /usr/bin/time -v "$TOOL_PATH" \
        -i "$FASTQ_FILE_F" \
        -r "$FASTQ_FILE_R" \
        -o "$OUTPUT_MAPPING" \
        -p "$PATTERN" \
        -b "$BARCODE_FILE" \
        -m "5,0,$mismatch,$mismatch,$mismatch,$mismatch,$mismatch,0" \
        -t "$THREAD_COUNT" \
        -q true \
        -f true \
        2> "$RESOURCE_LOG"

    end_time=$(date +%s%N)
    elapsed_time=$(( ($end_time - $start_time) / 1000000000 ))
    echo $(( ($end_time - $start_time) / 1000000000 ))


    if [ -f "$RESOURCE_LOG" ]; then
        max_memory=$(grep "Maximum resident set size" "$RESOURCE_LOG" | awk '{print $NF}')
        user_time=$(grep "User time" "$RESOURCE_LOG" | awk '{print $NF}')  # CPU time spent in user mode
        system_time=$(grep "System time" "$RESOURCE_LOG" | awk '{print $NF}')  # CPU time spent in kernel mode
        total_cpu_time=$(echo "$user_time + $system_time" | bc)  # Total CPU time
    else
        max_memory=0
        total_cpu_time=0
    fi

    # Log time and memory
    echo "$mismatch $elapsed_time $user_time $system_time $total_cpu_time" >> "$TIME_LOG"
    echo "$mismatch $max_memory" >> "$MEMORY_LOG"

    # Check if the tool ran successfully
    if [ $? -ne 0 ]; then
        echo "Error: Tool failed for mismatch $mismatch. Skipping further analysis."
        continue
    fi
    
done

# analysis notification
echo "Analysis complete! Results are stored in the $RESULTS_DIR directory."




