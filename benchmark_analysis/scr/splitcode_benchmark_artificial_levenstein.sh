#!/bin/bash
#SBATCH --job-name=splitcode_benchmark_artificial_levenstein
#SBATCH --error=/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/splitcode_results/artificial_levenstein/splitcode_benchmark_artificial_levenstein_%A%a.err  # Error file location
#SBATCH --output=/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/splitcode_results/artificial_levenstein/splitcode_benchmark_artificial_levenstein_%A%a.out # Output file location
#SBATCH --partition=binf
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16              # Number of CPU cores per task
#SBATCH --time=60:00:00
#SBATCH --mail-user=theodosiadou.ana@gmail.com  # Email
#SBATCH --mail-type=END,FAIL               # Email notification on job end or fail


# Create the input and output paths and variables
TOOL_PATH="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/tools/splitcode/build/src/splitcode" 
CONFIG_FILE="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/splitcode/config_artificial.txt" #configuration file with allowed subsequences
TEMP_CONFIG="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/splitcode/temp_config_artificial.txt" 
FASTQ_FILE="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/artificial/levenstein/mismatched_fastq_levenstein.fastq" #fastq file that contains the mismatched reads after subs, and indels
RESULTS_DIR="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/splitcode_results/artificial_levenstein" 


#Logs files
TIME_LOG="$RESULTS_DIR/time_log.txt"
MEMORY_LOG="$RESULTS_DIR/memory_log.txt"
ACCURACY_LOG="$RESULTS_DIR/accuracy_log.txt"
FILTERED_PERCENT_LOG="$RESULTS_DIR/filtered_percentage_log.txt"

mkdir -p "$RESULTS_DIR" # We want to ensure that this directory exists

# Function to update mismatches in config file
update_mismatches_in_config() {
    local mismatch=$1
    cp "$CONFIG_FILE" "$TEMP_CONFIG"
    awk -v mismatch="$mismatch" 'NR >= 3 {$3 = mismatch} 1' "$TEMP_CONFIG" > "$TEMP_CONFIG.tmp" && mv "$TEMP_CONFIG.tmp" "$TEMP_CONFIG"
}

#Creates the headers in the log files
echo "Mismatch Elapsed_Time(s) User_time(s) System_time(s) Total_CPU_time(s)" > "$TIME_LOG"
echo "Mismatch Max_Memory(KB)" > "$MEMORY_LOG"
echo "Mismatch True_reads False_reads Unmapped_reads Coverage(%) Accuracy(%) Precision Recall F1_score" > "$ACCURACY_LOG"
echo "Mismatch Reads_in_mapping Reads_in_filtered_mapping Filtered_Percentage(%)" > "$FILTERED_PERCENT_LOG"

# Loop through mismatch values (1 to 5)
for mismatch in {1..5}; do
    echo "Running splitcode for mismatch=$mismatch..."
    
    # Update config file for current mismatch
    update_mismatches_in_config "$mismatch"
    
    # Define output file paths
    SPLITCODE_OUTPUT="$RESULTS_DIR/output_mismatch_${mismatch}.fastq"
    UNASSIGNED_OUTPUT="$RESULTS_DIR/unassigned_mismatch_${mismatch}.fastq"
    BARCODE_OUTPUT="$RESULTS_DIR/final_barcodes_mismatch_${mismatch}.fastq"
    MAPPING_OUTPUT="$RESULTS_DIR/mapping_mismatch_${mismatch}.txt"
    SUMMARY_OUTPUT="$RESULTS_DIR/summary_mismatch_${mismatch}.txt"
    RESOURCE_LOG="$RESULTS_DIR/resource_mismatch_${mismatch}.log"
        
    # Run the tool and measure time/memory
    start_time=$(date +%s%N)

    /usr/bin/time -v "$TOOL_PATH" \
        -c "$TEMP_CONFIG" \
        --nFastqs=1 \
        --assign \
        -o "$SPLITCODE_OUTPUT" \
        --unassigned="$UNASSIGNED_OUTPUT" \
        --outb="$BARCODE_OUTPUT" \
        --mapping="$MAPPING_OUTPUT" \
        --summary="$SUMMARY_OUTPUT" \
        "$FASTQ_FILE" \
        2> "$RESOURCE_LOG"

    end_time=$(date +%s%N)
    elapsed_time=$(( ($end_time - $start_time) / 1000000000 ))
    echo $(( ($end_time - $start_time) / 1000000000 ))

   
    
    if [ $? -ne 0 ]; then
        echo "Error: splitcode terminated unexpectedly for mismatch $mismatch. Potential memory issue or other failure."
        # Check if the resource file exists and try to extract partial data
        if [ -f "$RESOURCE_LOG" ]; then
            max_memory=$(grep "Maximum resident set size" "$RESOURCE_LOG" | awk '{print $NF}')
            # Assign defaults if metrics are missing
            max_memory=${max_memory:-0}
        else
            max_memory=0
            elapsed_time=0
        fi
        # Log the available or default data
        echo "$mismatch $max_memory" >> "$MEMORY_LOG"
        continue
    fi

# If the tool runs successfully, extract time/memory usage
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


    # the output of the mapping file is not in a format that can be directly interpreted by the SCDemultiplex tool, so we first need to edit the file
    MAPPING_FILE="$RESULTS_DIR/mapping_mismatch_${mismatch}.txt"
    MAPPING_FILTERED="$RESULTS_DIR/mapping_filtered_${mismatch}.txt"
    MAPPING_FINAL="$RESULTS_DIR/mapping_final_${mismatch}.txt"


    awk -F'\t' '{
    split($2, a, ","); 
    count = 0;
    for (i = 1; i <= length(a); i++) {
        if (length(a[i]) == 8) count++;
    } 
    if (count == 3) print $0
    }' "$MAPPING_FILE" > "$MAPPING_FILTERED"

    if [ ! -s "$MAPPING_FILTERED" ]; then
        echo "No sequences with all 3 variable barcodes found for mismatch $mismatch. Skipping to the next mismatch."
        echo "$mismatch 0 0 0" >> "$FILTERED_PERCENT_LOG"
        echo "$mismatch 0 0 0 0 0 0 0 0" >> "$ACCURACY_LOG"
        continue
    fi

    # then we also want to check the percentage of the full sequences in comparison to the full number of reads the tool found
    sum_mapping=$(awk -F'\t' '{sum += $3} END {print sum}' "$MAPPING_FILE")
    sum_filtered=$(awk -F'\t' '{sum += $3} END {print sum}' "$MAPPING_FILTERED")

    if [ -z "$sum_filtered" ] || [ "$sum_filtered" -eq 0 ]; then
        echo "Filtered sum is zero for mismatch $mismatch. Skipping further processing."
        continue
    fi

    percentage_filtered=$(awk "BEGIN {printf \"%.2f\", ($sum_filtered / $sum_mapping) * 100}")

    echo "$mismatch Original sum of the reads: $sum_mapping"
    echo "$mismatch Filtered sum of the reads: $sum_filtered"
    echo "$mismatch $sum_mapping $sum_filtered $percentage_filtered%" >> "$FILTERED_PERCENT_LOG"

    # the output will be the 5 reads separated by commas so we need to concatenate by excluding the commas
    awk -F'\t' '{
        gsub(",", "", $2); 
        for (i = 0; i < $3; i++) {
            print $2;
        }
    }' "$MAPPING_FILTERED" > "$MAPPING_FINAL"

    if [ ! -f "$MAPPING_FINAL" ]; then
        echo "Concatenated file missing for mismatch $mismatch. Skipping further processing."
        continue
    fi

    echo "Processing complete for mismatch $mismatch! Filtered mapping written to '$MAPPING_FILTERED'."
    echo "Concatenated 2nd column written to '$MAPPING_FINAL'."

    COMPARISON_SCRIPT="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/scr/calculate_true_sequences_splitcode.py"
    GROUND_TRUTH_FILE="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/artificial/ground_truth_sequences.fastq"
    TRUE_SEQUENCES_FILE="$RESULTS_DIR/true_sequences_splitcode_mismatch_${mismatch}.fastq"
    FALSE_SEQUENCES_FILE="$RESULTS_DIR/false_sequences_splitcode_mismatch_${mismatch}.fastq"
    UNMAPPED_SEQUENCES_FILE="$RESULTS_DIR/unmapped_sequences_mismatch_${mismatch}.fastq"
    STATS_FILE="$RESULTS_DIR/stats_mismatch_${mismatch}.txt"
    READ_COUNTS_FILE="$RESULTS_DIR/read_counts_mismatch_${mismatch}.txt"
    SUMMARY_LOG="$RESULTS_DIR/true_false_summary_${mismatch}.txt"

    # Call Python script to compare with ground truth
    python3 "$COMPARISON_SCRIPT" \
        "$GROUND_TRUTH_FILE" \
        "$MAPPING_FINAL" \
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