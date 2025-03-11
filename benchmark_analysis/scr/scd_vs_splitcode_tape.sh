#!/bin/bash
#SBATCH --job-name=compare_scd_split_tape
#SBATCH --error=/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/scd_vs_splitcode_tape/trial/compare_scd_split_tape_%A%a.err
#SBATCH --output=/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/scd_vs_splitcode_tape/trial/compare_scd_split_tape_%A%a.out
#SBATCH --partition=binf
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16              # Number of CPU cores per task
#SBATCH --time=60:00:00
#SBATCH --mail-user=theodosiadou.ana@gmail.com  # Email
#SBATCH --mail-type=END,FAIL               # Email notification on job end or fail

# Directories
SCD_DIR="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/SCDemultiplex_results/tape_dataset"
SPLIT_DIR="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/splitcode_results/tape_dataset"
RESULTS_DIR="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/scd_vs_splitcode_tape/trial"

# Ensure results directory exists
mkdir -p "$RESULTS_DIR"

# Output file
READ_COUNTS_FILE="$RESULTS_DIR/read_counts.txt"
READS_SHARED_FILE="$RESULTS_DIR/reads_shared.txt"
echo -e "Mismatch\tSCD_Reads\tSplit_Reads\tCommon_Reads" > "$READ_COUNTS_FILE"

# Path to Python script
COMPARE_SCRIPT="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/scr/scd_vs_splitcode_tape.py"

# Loop through mismatch values
for mismatch in {1..5}; do
    echo "Processing mismatch=$mismatch..."
    
    # Define file paths
    SCD_FILE="$SCD_DIR/Demultiplexed_MAPPING_${mismatch}.tsv"
    SPLIT_FILE="$SPLIT_DIR/mapping_filtered_${mismatch}.txt"
    SCD_OUTPUT="$RESULTS_DIR/scd_reads_${mismatch}.txt"
    SPLITCODE_OUTPUT="$RESULTS_DIR/splitcode_reads_${mismatch}.txt"
    
    # Check if both files exist
    if [[ -f "$SCD_FILE" && -f "$SPLIT_FILE" ]]; then
        echo "Found both files for mismatch=$mismatch. Running comparison..."
        
        # Run Python script to process and compare
        python3 "$COMPARE_SCRIPT" "$SCD_FILE" "$SPLIT_FILE" "$SCD_OUTPUT" "$SPLITCODE_OUTPUT" "$READ_COUNTS_FILE" "$READS_SHARED_FILE" "$mismatch"
    else
        echo "Mismatch=$mismatch: One or both files missing. Skipping..."
        echo -e "$mismatch\t0\t0\t0" >> "$READ_COUNTS_FILE"
    fi
    
    echo "Done with mismatch=$mismatch."
done

echo "All mismatches processed! Results saved in $READ_COUNTS_FILE."
