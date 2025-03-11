import random
import os

#Create a list of all available barcodes from the txt file
def load_barcodes(filename):
    with open('SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/artificial/possible_barcodes.txt', 'r') as file:
        barcodes_list = file.readline().strip().split(',')
        # print("Barcodes list:", barcodes_list)
    return barcodes_list

#From the list that contains the barcodes, we will choose each time one random one
def generate_barcode(barcodes_list):
    return random.choice(barcodes_list)


#Define the Linker sequences
linker1 = 'CTTGTGGAAAGGACGAAACACCG'
linker2 = 'GTTTTAGAGCTAGAAATAGCAA'

#Generate the UMI sequence, that has to be random each time
def generate_umi():
    length = 10
    bases = ['A','T','C','G']
    probabilities = [0.1, 0.1, 0.4, 0.4]

    umi = ''.join(random.choices(bases, probabilities, k = length))
    return umi

# randomumi= generate_umi()
# print(f"random umi: {randomumi}")

#this prints one random barcode out of the list:
print(generate_barcode(load_barcodes('SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/artificial/possible_barcodes.txt')))


def generate_fastq(barcodes_list, num_sequences, output_directory):
    #Output directory
    output_directory = "SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/artificial"

    with open(os.path.join(output_directory, "ground_truth_sequences.fastq"), "w") as f:
        for i in range(num_sequences):
            barcode1 = generate_barcode(barcodes_list)
            barcode2 = generate_barcode(barcodes_list)
            barcode3 = generate_barcode(barcodes_list)
            umi = generate_umi()

        # read = f'{barcode1}{linker1}{umi}{barcode2}{linker2}{barcode3}
            read = barcode1 + linker1 + umi + barcode2 + linker2 + barcode3

        #The quality check number will be 40, so in ASCII that is the letter "I"
            quality_scores = 'I' * len(read)

            f.write(f"@{barcode1}_{umi}_{i + 1}\n")
            f.write(f"{read}\n")
            f.write("+\n")
            f.write(f"{quality_scores}\n")
    

    

if __name__ == "__main__":
    barcodes_file = 'SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/artificial/possible_barcodes.txt'
    barcodes_list = load_barcodes(barcodes_file)

    num_sequences = 1000000
    output_directory = "SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/artificial"

    generate_fastq(barcodes_list, num_sequences, output_directory)