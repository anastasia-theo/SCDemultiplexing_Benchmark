import sys
from collections import defaultdict

def compare_sequences(ground_truth_file, demultiplexed_file, true_reads_file, false_reads_file, stats_file, read_count_file):
    # Initialize counters
    true_reads = 0
    false_reads = 0

    # Store ground truth sequences and their counts
    ground_truth_dict = defaultdict(list)  # Stores list of (read_id, full_sequence)
    ground_truth_counts = defaultdict(int)  # Stores only the count of each sequence

    with open(ground_truth_file, 'r') as ground:
        sequence_id = None
        for i, line in enumerate(ground):
            line_index = i % 4
            if line_index == 0:  # Read name
                sequence_id = line.strip()
            elif line_index == 1:  # Sequence
                full_sequence = line.strip()
                processed_sequence = full_sequence[:31] + full_sequence[41:]  # Exclude bases 31-40
                ground_truth_dict[processed_sequence].append((sequence_id, full_sequence))  # Store ID & sequence
                ground_truth_counts[processed_sequence] += 1  # Store count

  
    with open(demultiplexed_file, 'r') as file:
        total_mapped_reads= len(file.readlines())
    
    unmapped_reads = 1_000_000 - total_mapped_reads
        
    # Store mapping file sequences and their counts
    mapping_counts = defaultdict(int)

    with open(demultiplexed_file, 'r') as demultiplexed:
        for dem_seq in demultiplexed:
            dem_seq = dem_seq.strip()
            mapping_counts[dem_seq] += 1  # Count occurrences in the mapping file
        

    with open(true_reads_file, 'w') as true_reads_f, \
         open(false_reads_file, 'w') as false_reads_f, \
         open(read_count_file, 'w') as read_counts:

        read_counts.write("Read_IDs\tRead_Sequence\tMapping_Count\tGroundTruth_Count\tTrue_Reads\tFalse_Reads\n")  # Header


        for read, map_count in mapping_counts.items():
            if read in ground_truth_dict:
                seq_info = ground_truth_dict[read]
                ground_truth_count = ground_truth_counts[read]

                # True Reads: Minimum of occurrences in the mapping file and ground truth
                true_count = min(map_count, ground_truth_count)
                true_reads += true_count

                # False Reads: Extra mapped occurrences beyond true reads
                false_count = max(0, map_count - ground_truth_count)
                false_reads += false_count

                # Write each sequence ID on a new line, except the last one (which gets the sequence and counts)
                for seq_id, full_seq in seq_info[:-1]:
                    read_counts.write(f"{seq_id}\n")  # Just ID on a new line
                
                # Last ID writes the full info in the table
                last_id, last_full_seq = seq_info[-1]
                read_counts.write(f"{last_id}\t{read}\t{map_count}\t{ground_truth_count}\t{true_count}\t{false_count}\n")

                # Write sequences to true reads file
                for _ in range(true_count):
                    true_reads_f.write(f"{read}\n")

        # Handle fully false reads (only in mapping, not in ground truth)
        for read, map_count in mapping_counts.items():
            if read in ground_truth_dict:
                continue  # Already processed above

            false_reads += map_count
            for _ in range(map_count):
                false_reads_f.write(f"{read}\n")


    # Accuracy (ignoring unmapped reads)
    accuracy = (true_reads / (true_reads + false_reads)) * 100 if (true_reads + false_reads) > 0 else 0

    # Coverage (including unmapped reads)
    coverage = (true_reads / (true_reads + false_reads + unmapped_reads)) * 100 if (true_reads + false_reads + unmapped_reads) > 0 else 0

    # Precision, Recall, and F1-score
    precision = (true_reads / (true_reads + false_reads)) if (true_reads + false_reads) > 0 else 0
    recall = (true_reads / (true_reads + unmapped_reads)) if (true_reads + unmapped_reads) > 0 else 0
    f1_score = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    # Write statistics file
    with open(stats_file, 'w') as stats:
        stats.write(f"True Reads: {true_reads}\n")
        stats.write(f"False Reads: {false_reads}\n")
        stats.write(f"Unmapped Reads: {unmapped_reads}\n")
        stats.write(f"Coverage: {coverage:.2f}%\n")  # (Previously "Accuracy including unmapped")
        stats.write(f"Accuracy: {accuracy:.2f}%\n")  # (Previously "Accuracy ignoring unmapped")
        stats.write(f"Precision: {precision:.2f}\n")
        stats.write(f"Recall: {recall:.2f}\n")
        stats.write(f"F1 Score: {f1_score:.2f}\n")

    # Print results
    print("Comparison complete!")
    print(f"True Reads: {true_reads}")
    print(f"False Reads: {false_reads}")
    print(f"Unmapped Reads: {unmapped_reads}")
    print(f"Coverage: {coverage:.2f}%")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1 Score: {f1_score:.2f}")

if __name__ == "__main__":
    ground_truth_file = sys.argv[1]      # FASTQ ground truth file
    demultiplexed_file = sys.argv[2]     # Mapping final file
    true_reads_file = sys.argv[3]        # Output for true reads
    false_reads_file = sys.argv[4]       # Output for false reads
    stats_file = sys.argv[5]             # Accuracy stats output
    read_count_file = sys.argv[6]        # Read counts file

    compare_sequences(ground_truth_file, demultiplexed_file, true_reads_file, false_reads_file, stats_file, read_count_file)



