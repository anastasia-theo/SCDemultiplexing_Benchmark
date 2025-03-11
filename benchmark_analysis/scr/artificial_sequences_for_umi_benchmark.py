import random
import os
from collections import defaultdict

#Create a list of all available barcodes from the txt file
def load_barcodes(filename):
    with open('/home/mrhin/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/artificial/UMI_benchmark/possible_barcodes_for_UMI_benchmark_50_barcodes.txt', 'r') as file:
        barcodes_list = file.readline().strip().split(',')
    return barcodes_list

#From the list that contains the barcodes, we will choose each time one random one
def generate_barcode(barcodes_list):
    return random.choice(barcodes_list)


#Define the Linker sequences
linker1 = 'CTTGTGGAAAGGACGAAACACCG'
linker2 = 'GTTTTAGAGCTAGAAATAGCAA'

#Generate the UMI sequence, that has to be random each time
def generate_umi():
    length = 10
    bases = ['A','T','C','G']
    probabilities = [0.1, 0.1, 0.4, 0.4]

    umi = ''.join(random.choices(bases, probabilities, k = length))
    return umi


def generate_first_reads(barcodes_list, num_sequences):
    reads = []
    for i in range(num_sequences):
        barcode1 = generate_barcode(barcodes_list)
        barcode2 = generate_barcode(barcodes_list)
        barcode3 = generate_barcode(barcodes_list)
        umi = generate_umi()
        read = barcode1 + linker1 + umi + barcode2 + linker2 + barcode3
        read_name = f"@{barcode1}_{umi}_{i + 1}"
        reads.append((read_name, read))
    return reads

# Write reads to the fastq file and also dublicate the reads to check for the umis
def write_reads_with_duplicates(reads, total_sequences, output_directory, log_file_path):
    output_fastq = os.path.join(output_directory, "ground_truth_sequences_UMI.fastq")
    duplicated_reads_log = []
    duplication_counts = defaultdict(int)

    with open(output_fastq, "w") as fastq_file, \
         open(log_file_path, "w") as log_file, \
         open(duplication_count_log_path, "w") as count_log_file:

        # Write headers for logs
        log_file.write("Duplicated Reads Log\n")
        log_file.write("=" * 50 + "\n")
        count_log_file.write("Read Duplication Counts\n")
        count_log_file.write("=" * 50 + "\n")

        # Write the first 100,000 reads
        for read_name, read in reads:
            quality_scores = 'I' * len(read)  # Create quality scores for the read
            fastq_file.write(f"{read_name}\n{read}\n+\n{quality_scores}\n")
            duplication_counts[read_name] = 1  # Original read count is 1

        # Duplicate reads randomly to reach the desired total number
        current_count = len(reads)
        while current_count < total_sequences:
            original_read_name, original_read = random.choice(reads)
            new_read_name = f"{original_read_name}_dup_{current_count + 1}"
            quality_scores = 'I' * len(original_read)  # Create quality scores for the duplicate

            # Write the duplicated read
            fastq_file.write(f"{new_read_name}\n{original_read}\n+\n{quality_scores}\n")
            duplicated_reads_log.append((new_read_name, original_read_name))
            duplication_counts[original_read_name] += 1  # Increment duplication count for the original read

            # Log the duplication
            log_file.write(f"Duplicated: {new_read_name} (from {original_read_name})\n")

            current_count += 1

        # Write the duplication count log
        for read_name, count in duplication_counts.items():
            count_log_file.write(f"{read_name}: {count} times\n")

# Main function
if __name__ == "__main__":
    barcodes_file = '/home/mrhin/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/artificial/UMI_benchmark/possible_barcodes_for_UMI_benchmark_50_barcodes.txt'
    output_directory = '/home/mrhin/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/artificial/UMI_benchmark'
    log_file_path = os.path.join(output_directory, "duplication_log.txt")
    duplication_count_log_path = os.path.join(output_directory, "duplication_count_log.txt")

    # Load barcodes and generate initial reads
    barcodes_list = load_barcodes(barcodes_file)
    initial_reads = generate_first_reads(barcodes_list, 100000)

    # Write reads and duplicates to the FASTQ file
    total_sequences = 1000000
    write_reads_with_duplicates(initial_reads, total_sequences, output_directory, log_file_path)


