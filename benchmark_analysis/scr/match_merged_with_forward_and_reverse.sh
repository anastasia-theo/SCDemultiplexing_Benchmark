#!/bin/bash
#SBATCH --job-name=match_merged
#SBATCH --error=/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/NKI/match_merged_%A%a.err
#SBATCH --output=/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/NKI/match_merged_%A%a.out
#SBATCH --partition=binf
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --time=60:00:00
#SBATCH --mail-user=theodosiadou.ana@gmail.com
#SBATCH --mail-type=END,FAIL

#!/bin/bash

# Input files
merged_headers="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/NKI/merged_headers.txt"
merged_headers_reverse="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/NKI/merged_headers_reverse.txt"
forward_fastq="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/NKI/forward.fastq"
reverse_fastq="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/NKI/reverse.fastq"
merged_fastq="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/NKI/NKI_merged.fastq"

# Output files
forward_filtered="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/NKI/forward_filtered.fastq"
reverse_filtered="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/NKI/reverse_filtered.fastq"

# Logging function
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

# Step 1: Filter forward file
log "Starting to filter forward file..."
awk 'NR==FNR {headers[$0]; next} /^@/ {header=$0; getline seq; getline plus; getline qual; if (header in headers) {print header; print seq; print plus; print qual}}' "$merged_headers" "$forward_fastq" > "$forward_filtered"
if [ $? -eq 0 ]; then
    log "Forward file filtering completed successfully."
else
    log "Error: Failed to filter forward file."
    exit 1
fi

# Step 2: Filter reverse file
log "Starting to filter reverse file..."
awk 'NR==FNR {headers[$0]; next} /^@/ {header=$0; getline seq; getline plus; getline qual; if (header in headers) {print header; print seq; print plus; print qual}}' "$merged_headers_reverse" "$reverse_fastq" > "$reverse_filtered"
if [ $? -eq 0 ]; then
    log "Reverse file filtering completed successfully."
else
    log "Error: Failed to filter reverse file."
    exit 1
fi

# Step 3: Verify results
log "Verifying results..."
merged_reads=$(grep -c '^@' "$merged_fastq")
forward_filtered_reads=$(grep -c '^@' "$forward_filtered")
reverse_filtered_reads=$(grep -c '^@' "$reverse_filtered")

log "Merged reads: $merged_reads"
log "Forward filtered reads: $forward_filtered_reads"
log "Reverse filtered reads: $reverse_filtered_reads"

if [ "$merged_reads" -eq "$forward_filtered_reads" ] && [ "$merged_reads" -eq "$reverse_filtered_reads" ]; then
    log "Verification successful: Filtered files match the merged file."
else
    log "Error: Filtered files do not match the merged file."
    exit 1
fi

log "Script completed successfully."


# grep '^@' NKI_merged.fastq | cut -d' ' -f1 | sed 's/@//' > merged_ids.txt
# grep '^@' NKI_merged.fastq > merged_headers.txt
# grep -A 3 -Ff merged_headers.txt 7659_1_UDI_well_G11_CCATAGACCT-GTTCTCACGG_S9_R1_001.fastq | sed '/^--$/d' > filtered_forward.fastq


