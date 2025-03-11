###### Merge the NKI joined dataset and the kite dataset
###### (kite from joined dataset and with linker and ab anchor)

from Bio import SeqIO

def filter_fastq_by_read_names(joined_fastq, kite_fastq, output_fastq, missing_reads_log):
    # Step 1: Load all read names from Kite dataset into a set
    print("Loading read names from Kite dataset...")
    kite_read_names = set()
    
    with open(kite_fastq, "r") as kite_file:
        for record in SeqIO.parse(kite_file, "fastq"):
            kite_read_names.add(record.id)  # Store read names (excluding '@')
    
    print(f"Loaded {len(kite_read_names)} read names from Kite dataset.")

    # Step 2: Filter Joined dataset based on Kite read names
    print("Filtering reads from Joined dataset...")
    matched_reads = 0
    missing_reads = set(kite_read_names)  # To track missing reads
    
    with open(joined_fastq, "r") as joined_file, open(output_fastq, "w") as out_file:
        for record in SeqIO.parse(joined_file, "fastq"):
            if record.id in kite_read_names:
                SeqIO.write(record, out_file, "fastq")
                matched_reads += 1
                missing_reads.discard(record.id)  # Remove found read from missing set
    
    print(f"Matched and written {matched_reads} reads to {output_fastq}.")

    # Step 3: Log missing reads
    if missing_reads:
        print(f"{len(missing_reads)} reads from Kite dataset were NOT found in Joined dataset. Logging them...")
        with open(missing_reads_log, "w") as log_file:
            for read_name in missing_reads:
                log_file.write(read_name + "\n")
        print(f"Missing read names saved in {missing_reads_log}.")
    else:
        print("All reads from Kite dataset were found in the Joined dataset.")

# Example usage from the original NKI- to joined- to kite
joined_fastq = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/NKI/NKI_merged_join.fastq"  # Large FASTQ file with 84M reads
kite_fastq = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/kite/joined_linker_ab/joined_linker_ab_kite.fastq"      # Smaller FASTQ file with 83M reads
output_fastq = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/kite/joined_linker_ab/joined_linker_ab_merged.fastq"   # Output FASTQ for matched reads
missing_reads_log = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/kite/joined_linker_ab/joined_linker_ab_merged_missing_reads.txt" # Log for missing reads


filter_fastq_by_read_names(joined_fastq, kite_fastq, output_fastq, missing_reads_log)
