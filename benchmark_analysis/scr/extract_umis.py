def extract_umis(fastq_file):
    umis = []

    with open(fastq_file, 'r') as file:
        for i, line in enumerate(file):
            # Read header lines (every 4th line starting from the first)
            if i % 4 == 0:
                # Extract UMI from the header (which is the second part between underscores)
                read_name = line.strip()  # Remove any leading/trailing spaces/newlines
                # Split the read name by underscores and get the UMI (second part)
                umi = read_name.split('_')[1]
                umis.append(umi)

    return umis

# Example usage:
fastq_file = '/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/artificial/ground_truth_sequences.fastq'  # Replace with your fastq file path
umis = extract_umis(fastq_file)

# Save the UMIs to a text file
with open('/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/artificial/all_umis.txt', 'w') as output_file:
    for umi in umis:
        output_file.write(f"{umi}\n")

print(f"Extracted {len(umis)} UMIs")
