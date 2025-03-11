# THESE CALCULATE THE NUMBER OF PROTEINS PER CELL

# from collections import defaultdict

# # Step 1: Load the file and skip the header
# input_file_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/SCDemultiplex_results/processing/ABABCOUNT.tsv"
# with open(input_file_path, "r") as input_file:
#     lines = input_file.readlines()[1:]  # Skip the header row

# # Step 2: Count occurrences of each value in the second column
# second_column_counts = defaultdict(int)

# for line in lines:
#     line = line.strip()  # Remove leading/trailing whitespace
#     if not line:  # Skip empty lines
#         continue

#     columns = line.split("\t")  # Split the line by tabs
#     if len(columns) >= 3:  # Ensure there are at least 3 columns
#         value = columns[1]  # Second column: SingleCell_BARCODE
#         try:
#             count = int(columns[2])  # Third column: AB_COUNT
#             second_column_counts[value] += count
#         except ValueError:
#             print(f"Warning: Invalid count in line: {line}")
#     else:
#         print(f"Warning: Skipping malformed line: {line}")

# # Step 3: Save the results to a file
# output_file_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/kite_vs_scd_processing/sc_counts_scd.tsv"
# with open(output_file_path, "w") as output_file:
#     for value, count in second_column_counts.items():
#         output_file.write(f"{value}\t{count}\n")

# print(f"Processing complete. Results saved to {output_file_path}")



# from collections import defaultdict

# # Step 1: Load the file
# input_file_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/kite_vs_scd_processing/cells_x_features_with_indices_and_ab.mtx"
# with open(input_file_path, "r") as input_file:
#     lines = input_file.readlines()

# # Step 2: Count occurrences of each value in the second column
# second_column_counts = defaultdict(int)

# for line in lines:
#     line = line.strip()  # Remove leading/trailing whitespace
#     if not line:  # Skip empty lines
#         continue

#     # Split the line by spaces, but handle spaces within antibody names
#     columns = line.split()
#     if len(columns) >= 3:  # Ensure there are at least 3 columns
#         # The second column is the x.y.z index
#         value = columns[-2]  # Second-to-last column
#         try:
#             count = int(columns[-1])  # Last column: count
#             second_column_counts[value] += count
#         except ValueError:
#             print(f"Warning: Invalid count in line: {line}")
#     else:
#         print(f"Warning: Skipping malformed line: {line}")

# # Step 3: Save the results to a file
# output_file_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/kite_vs_scd_processing/cell_per_protein_count_kite.tsv"  # Replace with the actual path
# with open(output_file_path, "w") as output_file:
#     for value, count in second_column_counts.items():
#         output_file.write(f"{value}\t{count}\n")

# print(f"Processing complete. Results saved to {output_file_path}")












# THESE CALCULATE ALL

from collections import Counter

# Step 1: Load the file
input_file_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/kite_vs_scd_processing/cells_x_features_with_indices_and_ab.mtx"
with open(input_file_path, "r") as input_file:
    lines = [line.strip().split("\t") for line in input_file]

# Step 2: Skip the header row
# lines = lines[1:]  # Skip the first line (header)

# Step 3: Count occurrences of each single-cell barcode (column 2)
single_cell_counts = Counter(line[0] for line in lines if len(line) >= 2)

# Step 4: Save the results to a file
output_file_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/kite_vs_scd_processing/single_cell_counts_kite.txt"
with open(output_file_path, "w") as output_file:
    for single_cell, count in single_cell_counts.items():
        output_file.write(f"{single_cell}\t{count}\n")

print(f"Processing complete. Results saved to {output_file_path}")