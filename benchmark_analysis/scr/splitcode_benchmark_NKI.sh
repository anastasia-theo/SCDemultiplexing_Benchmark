#!/bin/bash
#SBATCH --job-name=splitcode_benchmark_NKI
#SBATCH --error=/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/splitcode_results/NKI_dataset/splitcode_benchmark_NKI_%A%a.err  # Error file location
#SBATCH --output=/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/splitcode_results/NKI_dataset/splitcode_benchmark_NKI_%A%a.out # Output file location
#SBATCH --partition=binf
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16              # Number of CPU cores per task
#SBATCH --time=60:00:00
#SBATCH --mail-user=theodosiadou.ana@gmail.com  # Email
#SBATCH --mail-type=END,FAIL               # Email notification on job end or fail

# create the input and output paths and variables
TOOL_PATH="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/tools/splitcode/build/src/splitcode"
CONFIG_FILE="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/splitcode/config_NKI.txt"
TEMP_CONFIG="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/splitcode/temp_config_NKI.txt"
FASTQ_FILE="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/NKI/NKI_merged.fastq"
RESULTS_DIR="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/splitcode_results/NKI_dataset"

TIME_LOG="$RESULTS_DIR/time_log.txt"
MEMORY_LOG="$RESULTS_DIR/memory_log.txt"
FILTERED_PERCENT_LOG="$RESULTS_DIR/filtered_percentage_log.txt"

mkdir -p "$RESULTS_DIR" # we want to ensure that this directory exists


# Function to update mismatches in config file
#In this case we want the linker to have a standard mismatch
update_mismatches_in_config() {
    local mismatch=$1
    cp "$CONFIG_FILE" "$TEMP_CONFIG"
    awk -v mismatch="$mismatch" '
        BEGIN {OFS=FS="\t"} 
        # If the line starts with "linker", keep it unchanged
        /^linker/ {print; next}
        # Otherwise, update the third column with mismatch value
        NR >= 3 { $3 = mismatch } 
        { print }' "$TEMP_CONFIG" > "$TEMP_CONFIG.tmp" && mv "$TEMP_CONFIG.tmp" "$TEMP_CONFIG"
}


echo "Mismatch Elapsed_Time(s) User_time(s) System_time(s) Total_CPU_time(s)" > "$TIME_LOG"
echo "Mismatch Max_Memory(KB)" > "$MEMORY_LOG"
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
    BARCODES_FILE="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/NKI/barcodes.txt"
    MAPPING_FILTERED="$RESULTS_DIR/mapping_filtered_${mismatch}.txt"
    FILTERING_SCRIPT="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/scr/splitcode_barcode_filtering_NKI.py"
    SUMMARY_LOG="$RESULTS_DIR/true_false_summary_${mismatch}.txt"
    
    # we first want to keep only the finds that contain all 5 variable barcodes so we will call a python script to check
     python3 "$FILTERING_SCRIPT" \
        "$MAPPING_FILE" \
        "$BARCODES_FILE" \
        "$MAPPING_FILTERED" \
        >> "$SUMMARY_LOG"


    if [ ! -s "$MAPPING_FILTERED" ]; then
        echo "No sequences with all 5 variable barcodes found for mismatch $mismatch. Skipping to the next mismatch."
        echo "$mismatch 0 0 0" >> "$FILTERED_PERCENT_LOG"
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


    echo "Processing complete for mismatch $mismatch! Filtered mapping written to '$MAPPING_FILTERED'."
done

# analysis notification
echo "Analysis complete! Results are stored in the $RESULTS_DIR directory."


