#!/bin/bash
#SBATCH --job-name=SCDemultiplex_benchmark_processing_NKI
#SBATCH --error=/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/SCDemultiplex_results/processing/NKI/SCDemultiplex_benchmark_processing_NKI_%A%a.err  # Error file location
#SBATCH --output=/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/SCDemultiplex_results/processing/NKI/SCDemultiplex_benchmark_processing_NKI_%A%a.out # Output file location
#SBATCH --partition=binf
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16              # Number of CPU cores per task
#SBATCH --time=60:00:00
#SBATCH --mail-user=theodosiadou.ana@gmail.com  # Email
#SBATCH --mail-type=END,FAIL               # Email notification on job end or fail


# create the input and output paths and variables

TOOL_PATH="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/tools/SCDemultiplexingPipeline/bin/processing"
FASTQ_FILE="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/SCDemultiplex_results/processing/NKI/Demultiplexed_MAPPING_1.tsv.gz"
BARCODE_FILE="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/NKI/barcodes.txt"
ANTIBODY_FILE="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/NKI/antibodies.txt"
RESULTS_DIR="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/SCDemultiplex_results/processing/NKI"
THREAD_COUNT=60
OUTPUT_FILE="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/SCDemultiplex_results/processing/NKI/ABCOUNT.tsv"
RESOURCE_LOG="$RESULTS_DIR/resource_log.log"

TIME_LOG="$RESULTS_DIR/time_log.txt"
MEMORY_LOG="$RESULTS_DIR/memory_log.txt"

echo "Elapsed_Time(s) User_time(s) System_time(s) Total_CPU_time(s)" > "$TIME_LOG"
echo "Max_Memory(KB)" > "$MEMORY_LOG"

start_time=$(date +%s%N)

    /usr/bin/time -v "$TOOL_PATH" \
        -i "$FASTQ_FILE" \
        -o "$OUTPUT_FILE" \
        -b "$BARCODE_FILE" \
        -a "$ANTIBODY_FILE" \
        -x 1 \
        -c 0,2,3,4 \
        -u 0 \
        -t "$THREAD_COUNT" \
        2> "$RESOURCE_LOG"

    end_time=$(date +%s%N)
    elapsed_time=$(( ($end_time - $start_time) / 1000000000 ))
    echo $(( ($end_time - $start_time) / 1000000000 ))


# Extract resource usage from the log
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
echo "$elapsed_time $user_time $system_time $total_cpu_time" >> "$TIME_LOG"
echo " $max_memory" >> "$MEMORY_LOG"

# Check if the tool ran successfully
if [ $? -ne 0 ]; then
    echo "Error: Tool failed. Check the resource log for details."
    exit 1
fi

# Analysis notification
echo "Analysis complete! Results are stored in the $RESULTS_DIR directory."