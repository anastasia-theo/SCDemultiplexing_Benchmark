# File paths for your barcodes and UMIs
barcode_file = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/artificial/list_of barcodes.txt"
umi_file = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/artificial/all_umis.txt"

# Linkers (you can define them directly here, or read from a file if needed)
linkers = ["CTTGTGGAAAGGACGAAACACCG", "GTTTTAGAGCTAGAAATAGCAA"]  # Define your linkers here

# Function to read file and return lines as a list
def read_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Read barcodes and UMIs from text files
barcodes = read_file(barcode_file)
umis = read_file(umi_file)

# Prepare the FASTA content
fasta_content = []

# Add barcode sequences to the FASTA content
for i, barcode in enumerate(barcodes):
    fasta_content.append(f">barcode_{i+1}\n{barcode}")

# Add linker sequences to the FASTA content
for i, linker in enumerate(linkers):
    fasta_content.append(f">linker_{i+1}\n{linker}")

# Add UMI sequences to the FASTA content
for i, umi in enumerate(umis):
    fasta_content.append(f">umi_{i+1}\n{umi}")

# Write the FASTA content to a file
with open("/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/artificial/SDRranger/custom_transcriptome.fasta", "w") as f:
    f.write("\n".join(fasta_content))

print("Custom transcriptome FASTA file 'custom_transcriptome.fasta' has been created.")
