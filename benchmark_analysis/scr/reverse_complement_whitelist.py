from itertools import product

# Function to reverse complement a DNA sequence
def reverse_complement(sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([complement[base] for base in reversed(sequence)])

# Read the barcodes from the file
with open("/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/NKI/barcodes.txt", "r") as file:
    lines = file.readlines()

# Extract barcodes from the relevant lines (1st, 3rd, 4th, and 5th lines)
line1 = lines[0].strip().split(',')  # First line
line3 = lines[2].strip().split(',')  # Third line
line4 = lines[3].strip().split(',')  # Fourth line
line5 = lines[4].strip().split(',')  # Fifth line

# Generate all possible combinations of one barcode from each line
combinations = list(product(line1, line3, line4, line5))

# Save the original whitelist (without reverse complementing)
with open("/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/kite/NKI/whitelist_original.txt", "w") as original_file:
    for combo in combinations:
        original_file.write(''.join(combo) + '\n')

# Reverse complement each barcode in the combinations
reverse_complemented_combinations = []
for combo in combinations:
    reverse_combo = [reverse_complement(barcode) for barcode in combo]
    reverse_complemented_combinations.append(reverse_combo)

# Save the reverse-complemented whitelist
with open("/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/kite/NKI/whitelist_reverse_complemented.txt", "w") as reverse_file:
    for combo in reverse_complemented_combinations:
        reverse_file.write(''.join(combo) + '\n')

print("Whitelist files have been created!")