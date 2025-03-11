#!/bin/bash
#SBATCH --job-name=SCDemultiplex_benchmark_artificial_levenstein
#SBATCH --error=/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/SCDemultiplex_results/artificial_levenstein/0_umi/SCDemultiplex_benchmark_artificial_levenstein_%A%a.err  # Error file location
#SBATCH --output=/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/SCDemultiplex_results/artificial_levenstein/0_umi/SCDemultiplex_benchmark_artificial_levenstein_%A%a.out # Output file location
#SBATCH --partition=binf
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16              # Number of CPU cores per task
#SBATCH --time=60:00:00
#SBATCH --mail-user=theodosiadou.ana@gmail.com  # Email
#SBATCH --mail-type=END,FAIL               # Email notification on job end or fail

# create the input and output paths and variables

TOOL_PATH="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/tools/SCDemultiplexingPipeline/bin/demultiplexing"
FASTQ_FILE="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/artificial/levenstein/mismatched_fastq_levenstein.fastq"
BARCODE_FILE="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/artificial/possible_barcodes.txt"
RESULTS_DIR="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/SCDemultiplex_results/artificial_levenstein/0_umi"


TIME_LOG="$RESULTS_DIR/time_log.txt"
MEMORY_LOG="$RESULTS_DIR/memory_log.txt"
ACCURACY_LOG="$RESULTS_DIR/accuracy_log.txt"

mkdir -p "$RESULTS_DIR" # we want to ensure that this directory exists

#Creates the headers in the log files
echo "Mismatch Elapsed_Time(s) User_time(s) System_time(s) Total_CPU_time(s)" > "$TIME_LOG"
echo "Mismatch Max_Memory(KB)" > "$MEMORY_LOG"
echo "Mismatch True_reads False_reads Unmapped_reads Coverage(%) Accuracy(%) Precision Recall F1_score" > "$ACCURACY_LOG"

# Define pattern and thread count
PATTERN="[NNNNNNNN][CTTGTGGAAAGGACGAAACACCG][XXXXXXXXXX][NNNNNNNN][GTTTTAGAGCTAGAAATAGCAA][NNNNNNNN]"
# THREAD_COUNT=16

# Loop through mismatch values (e.g., from 0 to 5)
for mismatch in {1..5}; do
    echo "Running demultiplexing for mismatch=$mismatch..."

    # Output paths for each mismatch
    OUTPUT_MAPPING="$RESULTS_DIR/MAPPING_${mismatch}.tsv"
    OUTPUT_FILE="$RESULTS_DIR/Demultiplexed_MAPPING_${mismatch}.tsv"
    RESOURCE_LOG="$RESULTS_DIR/resource_mismatch_${mismatch}.log"

    start_time=$(date +%s%N)

    /usr/bin/time -v "$TOOL_PATH" \
        -i "$FASTQ_FILE" \
        -o "$OUTPUT_MAPPING" \
        -p "$PATTERN" \
        -b "$BARCODE_FILE" \
        -m "$mismatch,$mismatch,9,$mismatch,$mismatch,$mismatch" \
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

    
    COMPARISON_SCRIPT="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/scr/calculate_true_sequences_SCDemultiplex.py"
    GROUND_TRUTH_FILE="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/artificial/ground_truth_sequences.fastq"
    NON_TAB_OUTPUT="$RESULTS_DIR/demultiplexed_output_non_tab_${mismatch}.txt"
    TRUE_SEQUENCES_FILE="$RESULTS_DIR/true_sequences_scdemultiplex_mismatch_${mismatch}.fastq"
    FALSE_SEQUENCES_FILE="$RESULTS_DIR/false_sequences_scdemultiplex_mismatch_${mismatch}.fastq"
    STATS_FILE="$RESULTS_DIR/stats_mismatch_${mismatch}.txt"
    READ_COUNTS_FILE="$RESULTS_DIR/read_counts_mismatch_${mismatch}.txt"
    SUMMARY_LOG="$RESULTS_DIR/true_false_summary_${mismatch}.txt"

    python3 "$COMPARISON_SCRIPT" \
        "$OUTPUT_FILE" \
        "$NON_TAB_OUTPUT" \
        "$GROUND_TRUTH_FILE" \
        "$TRUE_SEQUENCES_FILE" \
        "$FALSE_SEQUENCES_FILE" \
        "$STATS_FILE" \
        "$READ_COUNTS_FILE" \
        >> "$SUMMARY_LOG"


    true_reads=$(grep "True Reads" "$STATS_FILE" | awk '{print $NF}')
    false_reads=$(grep "False Reads" "$STATS_FILE" | awk '{print $NF}')
    unmapped_reads=$(grep "Unmapped Reads" "$STATS_FILE" | awk '{print $NF}')
    coverage=$(grep "Coverage" "$STATS_FILE" | awk '{print $NF}')
    accuracy=$(grep "Accuracy" "$STATS_FILE" | awk '{print $NF}')
    precision=$(grep "Precision" "$STATS_FILE" | awk '{print $NF}')
    recall=$(grep "Recall" "$STATS_FILE" | awk '{print $NF}')
    f1_score=$(grep "F1 Score" "$STATS_FILE" | awk '{print $NF}')


    # Log these metrics in the new format
    echo "$mismatch $true_reads $false_reads $unmapped_reads $coverage $accuracy $precision $recall $f1_score" >> "$ACCURACY_LOG"

    # Print values
    echo "Mismatch: $mismatch"
    echo "True Reads: $true_reads"
    echo "False Reads: $false_reads"
    echo "Unmapped Reads: $unmapped_reads"
    echo "Coverage: $coverage%"
    echo "Accuracy: $accuracy%"
    echo "Precision: $precision"
    echo "Recall: $recall"
    echo "F1-score: $f1_score"
    
done

# analysis notification
echo "Analysis complete! Results are stored in the $RESULTS_DIR directory."


