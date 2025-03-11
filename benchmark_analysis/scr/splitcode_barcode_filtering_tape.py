import sys

# Define the two known linkers
LINKERS = {"CCACAGTCTCAAGCACGTGGAT", "AGTCGTACGCCGATGCGAAACATCGGCCAC"}

def load_barcodes(barcode_file):
    """Reads the barcode file and returns a list of barcode groups (one group per line)."""
    with open(barcode_file, 'r') as f:
        barcode_groups = [set(line.strip().split(',')) for line in f]

    print("\nLoaded barcode groups:")
    for i, group in enumerate(barcode_groups):
        print(f"Group {i + 1}: {group}")
    
    return barcode_groups

def extract_barcodes(mapping_file, barcode_groups):
    """Matches sequences in mapping_file to barcode groups in order."""
    filtered_lines = []

    with open(mapping_file, 'r') as f:
        for line in f:
            columns = line.strip().split('\t')
            if len(columns) < 2:
                continue  # Skip invalid lines

            print(f"\nProcessing line: {line.strip()}")  # Print the full line

            subsequences = columns[1].split(',')
            print(f"Subsequences: {subsequences}")  # Print parsed subsequences

            # Track found barcodes
            found_barcodes = []
            barcode_index = 0  # Track which group we are looking for

            for seq in subsequences:
                if seq in LINKERS:
                    print(f"Ignored linker: {seq}")  # Print when a linker is ignored
                    continue  # Skip linkers

                if barcode_index < len(barcode_groups) and seq in barcode_groups[barcode_index]:
                    found_barcodes.append(seq)
                    print(f"Matched barcode {barcode_index + 1}: {seq}")  # Print when a barcode is found
                    barcode_index += 1  # Move to the next barcode group
                
                if len(found_barcodes) == 4:
                    break  # Stop when exactly 4 barcodes are found

            print(f"Final found barcodes: {found_barcodes}")  # Print the final list of barcodes found

            if len(found_barcodes) == 4:
                filtered_lines.append(line.strip())  # Store full line
    print(f"Filtered lines to be written: {filtered_lines}", file=sys.stderr)
    return filtered_lines

def main():
    if len(sys.argv) != 4:
        print("Usage: python filter_barcodes.py <mapping_file> <barcode_file> <output_file>")
        sys.exit(1)

    mapping_file = sys.argv[1]
    barcode_file = sys.argv[2]
    output_file = sys.argv[3]

    # Load barcode groups (each line in barcode_file is a group)
    barcode_groups = load_barcodes(barcode_file)

    # Extract and filter barcodes
    filtered_lines = extract_barcodes(mapping_file, barcode_groups)

    # Write output
    with open(output_file, 'w') as f:
        for line in filtered_lines:
            f.write(f"{line}\n")

    print(f"\nFiltered lines written to {output_file}")

if __name__ == "__main__":
    main()
