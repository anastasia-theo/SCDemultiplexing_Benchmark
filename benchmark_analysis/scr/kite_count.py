# # Step 1: Read the barcodes.txt file
# with open("/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/tape_data/barcodes_tape_only_bcs.txt", "r") as barcode_file:
#     barcodes = [line.strip().split(",") for line in barcode_file]  # Split by comma

# # Separate the barcodes into three lists
# barcodes_line1 = [barcode.strip().upper() for barcode in barcodes[0]]  # First line of barcodes
# barcodes_line2 = [barcode.strip().upper() for barcode in barcodes[1]]  # Second line of barcodes
# barcodes_line3 = [barcode.strip().upper() for barcode in barcodes[2]]  # Third line of barcodes

# # Print the first few barcodes to verify
# print("Barcodes Line 1:", barcodes_line1[:5])
# print("Barcodes Line 2:", barcodes_line2[:5])
# print("Barcodes Line 3:", barcodes_line3[:5])

# # Step 2: Read the gene sequences file
# with open("/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/tape_data/cells_x_features_barcodes_reverse_complements.txt", "r") as gene_file:
#     gene_sequences = [line.strip().upper() for line in gene_file]

# # Step 3: Map each subsequence to its index in the barcode lists
# results = []
# for sequence in gene_sequences:
#     # Split the 24-base sequence into three 8-base subsequences
#     barcode1 = sequence[:8]
#     barcode2 = sequence[8:16]
#     barcode3 = sequence[16:24]

#     try:
#         # Find the indices of the barcodes in the corresponding lists
#         index1 = barcodes_line1.index(barcode1)
#         index2 = barcodes_line2.index(barcode2)
#         index3 = barcodes_line3.index(barcode3)

#         # Format the result as x.y.z
#         results.append(f"{index1}.{index2}.{index3}")
#     except ValueError as e:
#         print(f"Error: {e}. Barcode not found in list.")
#         print(f"Sequence: {sequence}")
#         print(f"Barcode1: {barcode1}, Barcode2: {barcode2}, Barcode3: {barcode3}")
#         print(f"Barcodes Line 1: {barcodes_line1}")
#         print(f"Barcodes Line 2: {barcodes_line2}")
#         print(f"Barcodes Line 3: {barcodes_line3}")
#         break  # Stop execution to debug

# # Step 4: Output the results
# with open("/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/kite/tape_dataset/genes_to_ids.txt", "w") as output_file:
#     for result in results:
#         output_file.write(result + "\n")

# print("Processing complete. Results saved to output.txt.")







# # Step 1: Load the x.y.z indices from the genes_to_ids.txt file
# with open("/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/kite/tape_dataset/genes_to_ids.txt", "r") as genes_file:
#     gene_indices = [line.strip() for line in genes_file]

# # Step 2: Load the file with repetitive indices
# input_file_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/tape_data/cells_x_features.mtx"  # Replace with the actual path
# with open(input_file_path, "r") as input_file:
#     lines = [line.strip().split() for line in input_file]

# # Step 3: Replace the first column with the corresponding x.y.z index
# updated_lines = []
# for line in lines:
#     gene_id = int(line[0]) - 1  # Convert to 0-based index
#     xyz_index = gene_indices[gene_id]  # Get the corresponding x.y.z index
#     updated_line = [xyz_index] + line[1:]  # Replace the first column
#     updated_lines.append(updated_line)

# # Step 4: Save the updated file
# output_file_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/tape_data/cells_x_features_with_indices.mtx"  # Replace with the actual path
# with open(output_file_path, "w") as output_file:
#     for updated_line in updated_lines:
#         output_file.write(" ".join(updated_line) + "\n")

# print("Processing complete. Updated file saved to output_file.txt.")




# Step 1: Load the antibody names
antibody_names = [
    "Rat_IgG_Control", "CD44 (v4)", "pP120-Catenin [T310]", "pRB [S807/811] (v1)",
    "me2 Histone H3 [K4]", "cCaspase 3 [D175] (v2)", "Mouse_IgG_Control",
    "pPDPK1 [S241]", "pMKK4/SEK1 [S257]", "pBTK [Y551] (1) (v2)",
    "p4E-BP1 [T37/46] (v2)", "pAKT [T308]", "pNF-κB p65 [S529]",
    "pP38 MAPK [T180/Y182] (v2)", "pHistone H2A.X [S139] (3)", "pS6 [S240/S244] (2)",
    "Pan-CK", "CK18", "Vimentin", "Cyclin B1 (2)", "pNDRG1 [T346]",
    "pHistone H3 [Ser28] (v3)", "Rabbit_IgG_Control"
]

# Step 2: Load the file with x.y.z indices and antibody numbers
input_file_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/kite_vs_scd_processing/cells_x_features_with_indices_tab_separated.mtx"  
with open(input_file_path, "r") as input_file:
    lines = [line.strip().split('\t') for line in input_file]

# Step 3: Replace the second column with the corresponding antibody name and swap columns
updated_lines = []
for line in lines:
    antibody_number = int(line[1]) - 1  # Convert to 0-based index
    antibody_name = antibody_names[antibody_number]  # Get the corresponding antibody name
    updated_line = [line[0], antibody_name] + line[2:]  # Keep the original order
    updated_lines.append(updated_line)

# Step 4: Save the updated file
output_file_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/kite_vs_scd_processing/cells_x_features_with_indices_and_ab.mtx"  
with open(output_file_path, "w") as output_file:
    for updated_line in updated_lines:
        output_file.write("\t".join(updated_line) + "\n")

print("Processing complete. Updated file saved to output_file.txt.")



