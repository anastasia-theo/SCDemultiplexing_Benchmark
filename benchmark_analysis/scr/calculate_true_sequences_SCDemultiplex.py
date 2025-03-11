#We will create a function that firstly takes the output of the demultiplexing pipeline, removes the first line
#and removes the tabs in between
# #after that it will search in the ground truth fastq for true matches and store them for statistical analysis
# import sys
# from collections import defaultdict

# def create_non_tab_separated_sequences(input_file, non_tab_file):
#     with open(input_file, 'r') as input, open(non_tab_file, 'w') as output:
#         lines = input.readlines()
#         for line in lines[1:]:  #this will skip the pattern line
#             barcodes = line.strip().split('\t')
#             read_without_UMI = ''.join(barcodes[:2] + barcodes[3:])
#             output.write(read_without_UMI + '\n')
#     print("tab extinction is done")


# def compare_sequences(ground_truth_file, non_tab_file, true_sequences_file, false_sequences_file, stats_file, read_count_file):
#     true_reads = 0
#     false_reads = 0

#     # Store ground truth sequences and their counts
#     ground_truth_dict = defaultdict(list)  # Stores list of (read_id, full_sequence)
#     ground_truth_counts = defaultdict(int)  # Stores only the count of each sequence

#     with open(ground_truth_file, 'r') as ground:
#         sequence_id = None
#         for i, line in enumerate(ground):
#             line_index = i % 4
#             if line_index == 0:
#                 sequence_id = line.strip()
#             elif line_index == 1:
#                 sequence = line.strip()
#                 processed_sequence = sequence[:31] + sequence[41:]  # Exclude bases 31 to 40 (10-base UMI)
#                 # print(processed_sequence)
#                 ground_truth_dict[processed_sequence].append((sequence_id, sequence))  # Store ID & sequence
#                 ground_truth_counts[processed_sequence] += 1  # Store count


#     with open(non_tab_file, 'r') as demultiplexed, \
#         open(true_sequences_file, 'w') as true_seq, \
#         open(false_sequences_file, 'w') as false_seq, \
#         open(read_count_file, 'w') as read_counts:

#         read_counts.write("Read_IDs\tRead_Sequence\tMapping_Count\tGroundTruth_Count\tTrue_Reads\tFalse_Reads\n")  # Header

#         total_mapped_reads= len(demultiplexed.readlines())
#         unmapped_reads = 1_000_000 - total_mapped_reads
#          # Store mapping file sequences and their counts
#         mapping_counts = defaultdict(int)

#         for dem_seq in demultiplexed:
#             dem_seq = dem_seq.strip()
#             mapping_counts[dem_seq] += 1  # Count occurrences in the mapping file
#             if dem_seq in ground_truth_dict:
#                 true_seq.write(f"{ground_truth_dict[dem_seq]}\n{dem_seq}\n")
#                 true_reads += 1
#                 # print("true")
#             else:
#                 false_seq.write(f"{dem_seq}\n")
#                 false_reads += 1
#                 # print("false")
#         # Write each sequence ID on a new line, except the last one (which gets the sequence and counts)
#             for seq_id, full_seq in seq_info[:-1]:
#                 read_counts.write(f"{seq_id}\n")  # Just ID on a new line
            
#             # Last ID writes the full info in the table
#             last_id, last_full_seq = seq_info[-1]
#             read_counts.write(f"{last_id}\t{read}\t{map_count}\t{ground_truth_count}\t{true_count}\t{false_count}\n")

#       # Accuracy (ignoring unmapped reads)
#     accuracy = (true_reads / (true_reads + false_reads)) * 100 if (true_reads + false_reads) > 0 else 0

#     # Coverage (including unmapped reads)
#     coverage = (true_reads / (true_reads + false_reads + unmapped_reads)) * 100 if (true_reads + false_reads + unmapped_reads) > 0 else 0

#     # Precision, Recall, and F1-score
#     precision = (true_reads / (true_reads + false_reads)) if (true_reads + false_reads) > 0 else 0
#     recall = (true_reads / (true_reads + unmapped_reads)) if (true_reads + unmapped_reads) > 0 else 0
#     f1_score = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

#     # Write statistics file
#     with open(stats_file, 'w') as stats:
#         stats.write(f"True Reads: {true_reads}\n")
#         stats.write(f"False Reads: {false_reads}\n")
#         stats.write(f"Unmapped Reads: {unmapped_reads}\n")
#         stats.write(f"Coverage: {coverage:.2f}%\n")  # (Previously "Accuracy including unmapped")
#         stats.write(f"Accuracy: {accuracy:.2f}%\n")  # (Previously "Accuracy ignoring unmapped")
#         stats.write(f"Precision: {precision:.2f}\n")
#         stats.write(f"Recall: {recall:.2f}\n")
#         stats.write(f"F1 Score: {f1_score:.2f}\n")

#     # Print results
#     print("Comparison complete!")
#     print(f"True Reads: {true_reads}")
#     print(f"False Reads: {false_reads}")
#     print(f"Unmapped Reads: {unmapped_reads}")
#     print(f"Coverage: {coverage:.2f}%")
#     print(f"Accuracy: {accuracy:.2f}%")
#     print(f"Precision: {precision:.2f}")
#     print(f"Recall: {recall:.2f}")
#     print(f"F1 Score: {f1_score:.2f}")

# if __name__ == "__main__":
    


#     # with open(stats_file, 'w') as stats:
#     #     stats.write(f"True Matches: {true_reads}\n")
#     #     stats.write(f"False Matches: {false_reads}\n")
#     #     stats.write(f"Accuracy (%): {true_reads / (true_reads + false_reads) * 100:.2f}\n")

#     # print("Comparison complete!")
#     # print(f"True Matches: {true_reads}")
#     # print(f"False Matches: {false_reads}")
#     # print(f"Accuracy (%): {true_reads / (true_reads + false_reads) * 100:.2f}") 

#     input_file = sys.argv[1]
#     non_tab_file = sys.argv[2]
#     ground_truth_file = sys.argv[3]
#     true_sequences_file = sys.argv[4]
#     false_sequences_file = sys.argv[5]
#     stats_file = sys.argv[6]
#     read_count_file = sys.argv[7]

#     create_non_tab_separated_sequences(input_file, non_tab_file)

#     compare_sequences(ground_truth_file, non_tab_file, true_sequences_file, false_sequences_file, stats_file, read_count_file)



# def compare_sequences(ground_truth_file, demultiplexed_file, true_reads_file, false_reads_file, stats_file, read_count_file):
#     # Initialize counters
#     true_reads = 0
#     false_reads = 0

#     # Store ground truth sequences and their counts
#     ground_truth_dict = defaultdict(list)  # Stores list of (read_id, full_sequence)
#     ground_truth_counts = defaultdict(int)  # Stores only the count of each sequence

#     with open(ground_truth_file, 'r') as ground:
#         sequence_id = None
#         for i, line in enumerate(ground):
#             line_index = i % 4
#             if line_index == 0:  # Read name
#                 sequence_id = line.strip()
#             elif line_index == 1:  # Sequence
#                 full_sequence = line.strip()
#                 processed_sequence = full_sequence[:31] + full_sequence[41:]  # Exclude bases 31-40
#                 ground_truth_dict[processed_sequence].append((sequence_id, full_sequence))  # Store ID & sequence
#                 ground_truth_counts[processed_sequence] += 1  # Store count

  
#     with open(demultiplexed_file, 'r') as file:
#         total_mapped_reads= len(file.readlines())
    
#     unmapped_reads = 1_000_000 - total_mapped_reads
        
#     # Store mapping file sequences and their counts
#     mapping_counts = defaultdict(int)

#     with open(demultiplexed_file, 'r') as demultiplexed:
#         for dem_seq in demultiplexed:
#             dem_seq = dem_seq.strip()
#             mapping_counts[dem_seq] += 1  # Count occurrences in the mapping file
        

#     with open(true_reads_file, 'w') as true_reads_f, \
#          open(false_reads_file, 'w') as false_reads_f, \
#          open(read_count_file, 'w') as read_counts:

#         read_counts.write("Read_IDs\tRead_Sequence\tMapping_Count\tGroundTruth_Count\tTrue_Reads\tFalse_Reads\n")  # Header


#         for read, map_count in mapping_counts.items():
#             if read in ground_truth_dict:
#                 seq_info = ground_truth_dict[read]
#                 ground_truth_count = ground_truth_counts[read]

#                 # True Reads: Minimum of occurrences in the mapping file and ground truth
#                 true_count = min(map_count, ground_truth_count)
#                 true_reads += true_count

#                 # False Reads: Extra mapped occurrences beyond true reads
#                 false_count = max(0, map_count - ground_truth_count)
#                 false_reads += false_count

#                 # Write each sequence ID on a new line, except the last one (which gets the sequence and counts)
#                 for seq_id, full_seq in seq_info[:-1]:
#                     read_counts.write(f"{seq_id}\n")  # Just ID on a new line
                
#                 # Last ID writes the full info in the table
#                 last_id, last_full_seq = seq_info[-1]
#                 read_counts.write(f"{last_id}\t{read}\t{map_count}\t{ground_truth_count}\t{true_count}\t{false_count}\n")

#                 # Write sequences to true reads file
#                 for _ in range(true_count):
#                     true_reads_f.write(f"{read}\n")

#         # Handle fully false reads (only in mapping, not in ground truth)
#         for read, map_count in mapping_counts.items():
#             if read in ground_truth_dict:
#                 continue  # Already processed above

#             false_reads += map_count
#             for _ in range(map_count):
#                 false_reads_f.write(f"{read}\n")


#     # Accuracy (ignoring unmapped reads)
#     accuracy = (true_reads / (true_reads + false_reads)) * 100 if (true_reads + false_reads) > 0 else 0

#     # Coverage (including unmapped reads)
#     coverage = (true_reads / (true_reads + false_reads + unmapped_reads)) * 100 if (true_reads + false_reads + unmapped_reads) > 0 else 0

#     # Precision, Recall, and F1-score
#     precision = (true_reads / (true_reads + false_reads)) if (true_reads + false_reads) > 0 else 0
#     recall = (true_reads / (true_reads + unmapped_reads)) if (true_reads + unmapped_reads) > 0 else 0
#     f1_score = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

#     # Write statistics file
#     with open(stats_file, 'w') as stats:
#         stats.write(f"True Reads: {true_reads}\n")
#         stats.write(f"False Reads: {false_reads}\n")
#         stats.write(f"Unmapped Reads: {unmapped_reads}\n")
#         stats.write(f"Coverage: {coverage:.2f}%\n")  # (Previously "Accuracy including unmapped")
#         stats.write(f"Accuracy: {accuracy:.2f}%\n")  # (Previously "Accuracy ignoring unmapped")
#         stats.write(f"Precision: {precision:.2f}\n")
#         stats.write(f"Recall: {recall:.2f}\n")
#         stats.write(f"F1 Score: {f1_score:.2f}\n")

#     # Print results
#     print("Comparison complete!")
#     print(f"True Reads: {true_reads}")
#     print(f"False Reads: {false_reads}")
#     print(f"Unmapped Reads: {unmapped_reads}")
#     print(f"Coverage: {coverage:.2f}%")
#     print(f"Accuracy: {accuracy:.2f}%")
#     print(f"Precision: {precision:.2f}")
#     print(f"Recall: {recall:.2f}")
#     print(f"F1 Score: {f1_score:.2f}")

# if __name__ == "__main__":
#     input_file = sys.argv[1]
#     non_tab_file = sys.argv[2]
#     ground_truth_file = sys.argv[3]
#     true_sequences_file = sys.argv[4]
#     false_sequences_file = sys.argv[5]
#     stats_file = sys.argv[6]
#     read_count_file = sys.argv[7]

#     create_non_tab_separated_sequences(input_file, non_tab_file)

#     compare_sequences(ground_truth_file, non_tab_file, true_sequences_file, false_sequences_file, stats_file, read_count_file)






# import sys
# from collections import defaultdict

# def create_non_tab_separated_sequences(input_file, non_tab_file):
#     with open(input_file, 'r') as input, open(non_tab_file, 'w') as output:
#         lines = input.readlines()
#         for line in lines[1:]:  # Skip the header line
#             barcodes = line.strip().split('\t')
#             read_without_UMI = ''.join(barcodes[:2] + barcodes[3:])  # Remove the UMI (3rd column)
#             output.write(read_without_UMI + '\n')
#     print("Tab extinction is done")

# def compare_sequences(ground_truth_file, non_tab_file, true_sequences_file, false_sequences_file, stats_file, read_count_file):
#     true_reads = 0
#     false_reads = 0

#     # Store ground truth sequences and their counts
#     ground_truth_dict = {}
#     with open(ground_truth_file, 'r') as ground:
#         for i, line in enumerate(ground):
#             line_index = i % 4
#             if line_index == 0:
#                 sequence_id = line.strip()
#             elif line_index == 1:
#                 sequence = line.strip()
#                 processed_sequence = sequence[:31] + sequence[41:]  # Exclude bases 31 to 40 (10-base UMI)
#                 ground_truth_dict[processed_sequence] = sequence_id

#     # Store the counts of sequences in the demultiplexed file
#     demultiplexed_counts = defaultdict(int)
#     with open(non_tab_file, 'r') as demultiplexed:
#         for dem_seq in demultiplexed:
#             dem_seq = dem_seq.strip()  # Clean the sequence
#             demultiplexed_counts[dem_seq] += 1  # Count occurrences of each read

#     # Open files for true and false sequences, and for read counts
#     with open(true_sequences_file, 'w') as true_seq, \
#          open(false_sequences_file, 'w') as false_seq, \
#          open(read_count_file, 'w') as read_counts:

#         # Write the header for the read counts file
#         read_counts.write("Read_IDs\tRead_Sequence\tMapping_Count\tGroundTruth_Count\tTrue_Reads\tFalse_Reads\n")

#         # Track sequence info for the last entry
#         seq_info = []

#         # Iterate through demultiplexed counts
#         for dem_seq, count in demultiplexed_counts.items():
#             if dem_seq in ground_truth_dict:
#                 # If the read exists in the ground truth, count the true reads
#                 ground_truth_count = 1  # Each sequence in ground truth is unique
#                 true_count = min(count, ground_truth_count)  # True reads: the minimum of counts
#                 true_reads += true_count
#                 # Store true sequence information for output later
#                 seq_info.append((ground_truth_dict[dem_seq], dem_seq, count, ground_truth_count, true_count, 0))

#                 # Write the true sequences to the output file
#                 for _ in range(true_count):
#                     true_seq.write(f"{dem_seq}\n")

#             else:
#                 # If the read does not exist in the ground truth, store it in false reads
#                 false_reads += count
#                 seq_info.append(("NA", dem_seq, count, 0, 0, count))
#                 for _ in range(count):
#                     false_seq.write(f"{dem_seq}\n")

#         # Write sequence IDs and counts
#         for seq_id, full_seq, map_count, ground_truth_count, true_count, false_count in seq_info[:-1]:
#             read_counts.write(f"{seq_id}\n")  # Just ID on a new line
        
#         # Last ID writes the full info in the table
#         last_id, last_full_seq, last_map_count, last_ground_truth_count, last_true_count, last_false_count = seq_info[-1]
#         read_counts.write(f"{last_id}\t{last_full_seq}\t{last_map_count}\t{last_ground_truth_count}\t{last_true_count}\t{last_false_count}\n")

#     # Accuracy (ignoring unmapped reads)
#     accuracy = (true_reads / (true_reads + false_reads)) * 100 if (true_reads + false_reads) > 0 else 0

#     # Coverage (including unmapped reads)
#     unmapped_reads = 1_000_000 - (true_reads + false_reads)  # Assuming 1 million total reads
#     coverage = (true_reads / (true_reads + false_reads + unmapped_reads)) * 100 if (true_reads + false_reads + unmapped_reads) > 0 else 0

#     # Precision, Recall, and F1-score
#     precision = (true_reads / (true_reads + false_reads)) if (true_reads + false_reads) > 0 else 0
#     recall = (true_reads / (true_reads + unmapped_reads)) if (true_reads + unmapped_reads) > 0 else 0
#     f1_score = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

#     # Write statistics to file
#     with open(stats_file, 'w') as stats:
#         stats.write(f"True Reads: {true_reads}\n")
#         stats.write(f"False Reads: {false_reads}\n")
#         stats.write(f"Unmapped Reads: {unmapped_reads}\n")
#         stats.write(f"Coverage: {coverage:.2f}%\n")
#         stats.write(f"Accuracy: {accuracy:.2f}%\n")
#         stats.write(f"Precision: {precision:.2f}\n")
#         stats.write(f"Recall: {recall:.2f}\n")
#         stats.write(f"F1 Score: {f1_score:.2f}\n")

#     # Print results
#     print("Comparison complete!")
#     print(f"True Reads: {true_reads}")
#     print(f"False Reads: {false_reads}")
#     print(f"Unmapped Reads: {unmapped_reads}")
#     print(f"Coverage: {coverage:.2f}%")
#     print(f"Accuracy: {accuracy:.2f}%")
#     print(f"Precision: {precision:.2f}")
#     print(f"Recall: {recall:.2f}")
#     print(f"F1 Score: {f1_score:.2f}")

# if __name__ == "__main__":
#     input_file = sys.argv[1]           # Demultiplexed input file
#     non_tab_file = sys.argv[2]         # Output file for sequences without tabs
#     ground_truth_file = sys.argv[3]    # Ground truth FASTQ file
#     true_sequences_file = sys.argv[4]  # Output file for true sequences
#     false_sequences_file = sys.argv[5] # Output file for false sequences
#     stats_file = sys.argv[6]           # Output file for statistics
#     read_count_file = sys.argv[7]      # Output file for read counts

#     # Step 1: Convert demultiplexed file (remove tabs and UMIs)
#     create_non_tab_separated_sequences(input_file, non_tab_file)

#     # Step 2: Compare the sequences and generate results
#     compare_sequences(ground_truth_file, non_tab_file, true_sequences_file, false_sequences_file, stats_file, read_count_file)






import sys
from collections import defaultdict

def create_non_tab_separated_sequences(input_file, non_tab_file):
    with open(input_file, 'r') as input, open(non_tab_file, 'w') as output:
        lines = input.readlines()
        for line in lines[1:]:  # Skip the header line
            barcodes = line.strip().split('\t')
            read_without_UMI = ''.join(barcodes[:2] + barcodes[3:])  # Remove the UMI (3rd column)
            output.write(read_without_UMI + '\n')
    print("Tab extinction is done")

def compare_sequences(ground_truth_file, non_tab_file, true_sequences_file, false_sequences_file, stats_file, read_count_file):
    true_reads = 0
    false_reads = 0

    # Store ground truth sequences and their counts
    ground_truth_dict = defaultdict(list)  # Stores list of (read_id, full_sequence)
    ground_truth_counts = defaultdict(int)  # Stores only the count of each sequence

    with open(ground_truth_file, 'r') as ground:
        for i, line in enumerate(ground):
            line_index = i % 4
            if line_index == 0:
                sequence_id = line.strip()
            elif line_index == 1:
                full_sequence = line.strip()
                processed_sequence = full_sequence[:31] + full_sequence[41:]  # Exclude bases 31-40
                ground_truth_dict[processed_sequence].append((sequence_id, full_sequence))  # Store ID & sequence
                ground_truth_counts[processed_sequence] += 1  # Store count

    # Store the counts of sequences in the demultiplexed file
    demultiplexed_counts = defaultdict(int)
    with open(non_tab_file, 'r') as demultiplexed:
        for dem_seq in demultiplexed:
            dem_seq = dem_seq.strip()  # Clean the sequence
            demultiplexed_counts[dem_seq] += 1  # Count occurrences of each read

    # Open files for true and false sequences, and for read counts
    with open(true_sequences_file, 'w') as true_seq, \
         open(false_sequences_file, 'w') as false_seq, \
         open(read_count_file, 'w') as read_counts:

        # Write the header for the read counts file
        read_counts.write("Read_IDs\tRead_Sequence\tMapping_Count\tGroundTruth_Count\tTrue_Reads\tFalse_Reads\n")

        # Track sequence info for the last entry
     

        # Iterate through demultiplexed counts
        for read, map_count in demultiplexed_counts.items():
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
                    true_seq.write(f"{read}\n")

        # Handle fully false reads (only in mapping, not in ground truth)
        for read, map_count in demultiplexed_counts.items():
            if read in ground_truth_dict:
                continue  # Already processed above

            false_reads += map_count
            for _ in range(map_count):
                false_seq.write(f"{read}\n")

    # Accuracy (ignoring unmapped reads)
    accuracy = (true_reads / (true_reads + false_reads)) * 100 if (true_reads + false_reads) > 0 else 0

    # Coverage (including unmapped reads)
    unmapped_reads = 1_000_000 - (true_reads + false_reads)  # Assuming 1 million total reads
    coverage = (true_reads / (true_reads + false_reads + unmapped_reads)) * 100 if (true_reads + false_reads + unmapped_reads) > 0 else 0

    # Precision, Recall, and F1-score
    precision = (true_reads / (true_reads + false_reads)) if (true_reads + false_reads) > 0 else 0
    recall = (true_reads / (true_reads + unmapped_reads)) if (true_reads + unmapped_reads) > 0 else 0
    f1_score = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    # Write statistics to file
    with open(stats_file, 'w') as stats:
        stats.write(f"True Reads: {true_reads}\n")
        stats.write(f"False Reads: {false_reads}\n")
        stats.write(f"Unmapped Reads: {unmapped_reads}\n")
        stats.write(f"Coverage: {coverage:.2f}%\n")
        stats.write(f"Accuracy: {accuracy:.2f}%\n")
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
    input_file = sys.argv[1]           # Demultiplexed input file
    non_tab_file = sys.argv[2]         # Output file for sequences without tabs
    ground_truth_file = sys.argv[3]    # Ground truth FASTQ file
    true_sequences_file = sys.argv[4]  # Output file for true sequences
    false_sequences_file = sys.argv[5] # Output file for false sequences
    stats_file = sys.argv[6]           # Output file for statistics
    read_count_file = sys.argv[7]      # Output file for read counts

    # Step 1: Convert demultiplexed file (remove tabs and UMIs)
    create_non_tab_separated_sequences(input_file, non_tab_file)

    # Step 2: Compare the sequences and generate results
    compare_sequences(ground_truth_file, non_tab_file, true_sequences_file, false_sequences_file, stats_file, read_count_file)
