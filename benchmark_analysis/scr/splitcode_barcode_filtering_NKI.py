import sys

# Function to match barcodes in the mapping file
def match_barcodes(mapping_file, barcode_file):
    with open(barcode_file, 'r') as f:
        # Read the barcode file lines into a list
        barcode_lines = f.readlines()

    # Split each line into barcodes
    barcodes = [line.strip().split(',') for line in barcode_lines]

    # Predefined linkers
    # linkers = [
    #     "CTTGTGGAAAGGACGAAACACCG",  # linker1
    #     "GTTTTAGAGCTAGAAATAGCAA",    # linker2
    #     "CGAATGCTCTGGCCTCTCAAGCACGTGGAT",  # linker3
    #     "AGTCGTACGCCGATGCGAAACATCGGCCAC"   # linker4
    # ]

    # Process the mapping file and filter out reads that don't match the pattern
    filtered_reads = []
    with open(mapping_file, 'r') as f:
        for line in f:
            columns = line.strip().split('\t')
            subsequences = columns[1].split(',')

            # Skip if there are fewer than 5 subsequences (we need at least 5 barcodes)
            if len(subsequences) < 5:
                continue

            # Initialize a set to keep track of barcodes found in the subsequences
            found_barcodes = set()

            match = True
            for seq in subsequences:
                # Check if this subsequence is a barcode
                found_barcode = False
                for i in range(5):
                    if seq in barcodes[i]:
                        found_barcodes.add(seq)
                        found_barcode = True
                        break

                # # If it's not a barcode, check if it's one of the predefined linkers
                # if not found_barcode:
                #     if seq not in linkers:
                #         match = False
                #         break

            # If all 5 barcodes are found, we will consider this read as valid
            if len(found_barcodes) == 5:
                filtered_reads.append(line.strip())

    return filtered_reads


def main():
    # Check for input arguments
    if len(sys.argv) != 4:
        print("Usage: python filter_barcodes.py <mapping_file> <barcode_file> <output_file>")
        sys.exit(1)

    mapping_file = sys.argv[1]
    barcode_file = sys.argv[2]
    output_file = sys.argv[3]

    # Get the filtered reads
    filtered_reads = match_barcodes(mapping_file, barcode_file)

    # Write the filtered reads to the output file
    with open(output_file, 'w') as f:
        for read in filtered_reads:
            f.write(f"{read}\n")

    print(f"Filtered reads written to {output_file}")


if __name__ == "__main__":
    main()




