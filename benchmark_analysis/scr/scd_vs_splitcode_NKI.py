import sys
from collections import Counter

def process_scd_file(scd_filename, output_scd):
    scd_reads = []
    with open(scd_filename, 'r') as file, open(output_scd, 'w') as out:
        next(file)
        for line in file:
            columns = line.strip().split('\t')
            if len(columns) >= 10:
                combined_seq = columns[0] + columns[3] + columns[5] + columns[7] + columns[9]
                scd_reads.append(combined_seq)
                out.write(combined_seq + '\n')
    return Counter(scd_reads)

def process_split_file(split_filename, output_split):
    split_reads = []
    with open(split_filename, 'r') as file, open(output_split, 'w') as out:
        for line in file:
            columns = line.strip().split('\t')
            if len(columns) >= 3:
                sequence = columns[1].replace(',', '')  # Clean sequence by removing commas
                count = int(columns[2])
                split_reads.extend([sequence] * count)
                out.write((sequence + '\n') * count)
    return Counter(split_reads)

def compare_reads(scd_counts, split_counts, read_counts_output, reads_shared, mismatch):
    total_scd = sum(scd_counts.values())  # Total SCD reads
    total_split = sum(split_counts.values())  # Total Split reads

    # Count shared reads (those that appear in both SCD and Split)
    shared_reads = 0
    shared_details = []  # List to keep track of how many times shared reads appear in both tools
    for seq in scd_counts:
        if seq in split_counts:
            count_scd = scd_counts[seq]
            count_split = split_counts[seq]
            shared_reads += min(count_scd, count_split)
            shared_details.append((seq, count_scd, count_split))

    # Append results to output file
    with open(read_counts_output, 'a') as out:  # Open file in append mode
        out.write(f"{mismatch}\t{total_scd}\t{total_split}\t{shared_reads}\n")
        
        # Write details of shared reads and their counts in both tools
    with open(reads_shared, 'a') as out:
        for seq, count_scd, count_split in shared_details:
            out.write(f"{seq}\t{count_scd}\t{count_split}\n")

# File paths
scd_input = sys.argv[1]
split_input = sys.argv[2]
scd_output = sys.argv[3]
split_output = sys.argv[4]
read_counts_output = sys.argv[5]
reads_shared = sys.argv[6]
mismatch = sys.argv[7]

# Process files
scd_counts = process_scd_file(scd_input, scd_output)
split_counts = process_split_file(split_input, split_output)

# Compare and generate report
compare_reads(scd_counts, split_counts, read_counts_output, reads_shared, mismatch)
