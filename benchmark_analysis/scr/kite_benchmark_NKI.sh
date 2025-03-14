#!/bin/bash
#SBATCH --job-name=kite_benchmark_NKI
#SBATCH --error=/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/kite/NKI/kite_benchmark_NKI_%A%a.err  # Error file location
#SBATCH --output=/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/kite/NKI/kite_benchmark_NKI_%A%a.out # Output file location
#SBATCH --partition=binf
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16              # Number of CPU cores per task
#SBATCH --time=60:00:00
#SBATCH --mail-user=theodosiadou.ana@gmail.com  # Email
#SBATCH --mail-type=END,FAIL               # Email notification on job end or fail

# Activate the Conda environment
source /scistor/informatica/ath100/miniconda3/bin/activate kallisto_bus_env  

# Set paths

FASTQ_DIR="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/NKI/"
RESULTS_DIR="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/kite/NKI"
FEATURES_SCRIPT="/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/scr/kITE_features_creation_NKI.py"
TIME_LOG="$RESULTS_DIR/time_log.txt"
MEMORY_LOG="$RESULTS_DIR/memory_log.txt"
OUTPUT_LOG=""$RESULTS_DIR/output_log.txt""
RESOURCE_LOG="$RESULTS_DIR/resource_kite.log"

#Creates the headers in the log files
echo "Elapsed_Time(s) User_time(s) System_time(s) Total_CPU_time(s)" > "$TIME_LOG"
echo "Max_Memory(KB)" > "$MEMORY_LOG"

# Start benchmarking with time and memory tracking
start_time=$(date +%s%N)

/usr/bin/time -v bash -c "

  echo 'Starting Kallisto KITE workflow...' | tee -a $OUTPUT_LOG

  # Step 1: Run Python script to process barcodes and generate feature file
  python $FEATURES_SCRIPT | tee -a $OUTPUT_LOG

  # Step 2: Generate the Kallisto index with mismatches allowed
  kb ref -i $RESULTS_DIR/mismatch.idx \
         -f1 $RESULTS_DIR/mismatch.fa \
         -g $RESULTS_DIR/t2g.txt \
         --workflow kite $RESULTS_DIR/features.tsv --overwrite | tee -a $OUTPUT_LOG

  # Step 3: Run kallisto-bustools pipeline to generate count matrix
  kb count --h5ad \
           -i $RESULTS_DIR/mismatch.idx \
           -o $RESULTS_DIR/ \
           -w $RESULTS_DIR/whitelist_reverse_complemented.txt \
           -g $RESULTS_DIR/t2g.txt \
           -x 0,0,20,1,0,8,1,38,46,1,76,84:0,32,58:0,0,0 \
           --workflow kite -t 4 --keep-tmp --overwrite \
           $FASTQ_DIR/forward_filtered.fastq \
           $FASTQ_DIR/reverse_filtered.fastq | tee -a $OUTPUT_LOG
           

  # Step 4: Convert BUS files to text format (optional for debugging)
  bustools text -o $RESULTS_DIR/bus_text_raw.txt $RESULTS_DIR/output.bus | tee -a $OUTPUT_LOG
  bustools text -o $RESULTS_DIR/bus_text_pp.txt $RESULTS_DIR/output.unfiltered.bus | tee -a $OUTPUT_LOG

  echo 'Workflow completed!' | tee -a $OUTPUT_LOG
" 2> "$RESOURCE_LOG"

# End time
end_time=$(date +%s%N)
elapsed_time=$(( ($end_time - $start_time) / 1000000000 ))  # Convert nanoseconds to seconds

# Extract resource usage
if [ -f "$RESOURCE_LOG" ]; then
    max_memory=$(grep "Maximum resident set size" "$RESOURCE_LOG" | awk '{print $NF}')
    user_time=$(grep "User time" "$RESOURCE_LOG" | awk '{print $NF}')
    system_time=$(grep "System time" "$RESOURCE_LOG" | awk '{print $NF}')
    total_cpu_time=$(echo "$user_time + $system_time" | bc)  # Compute total CPU time
else
    max_memory=0
    user_time=0
    system_time=0
    total_cpu_time=0
fi

# Log results
echo "Elapsed time: $elapsed_time sec" | tee -a "$OUTPUT_LOG"
echo "Max memory usage: $max_memory KB" | tee -a "$OUTPUT_LOG"
echo "User time: $user_time sec" | tee -a "$OUTPUT_LOG"
echo "System time: $system_time sec" | tee -a "$OUTPUT_LOG"
echo "Total CPU time: $total_cpu_time sec" | tee -a "$OUTPUT_LOG"

echo "$elapsed_time $user_time $system_time $total_cpu_time" >> "$TIME_LOG"
echo "$max_memory" >> "$MEMORY_LOG"


echo "Benchmarking completed. Check $OUTPUT_LOG for details."