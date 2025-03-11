from Bio.Seq import Seq
import csv

def reverse_complement(seq):
    return str(Seq(seq).reverse_complement())

def process_fastq(input_fastq, output_fastq):
    with open(input_fastq, 'r') as infile, open(output_fastq, 'w') as outfile:
        while True:
            header = infile.readline().strip()
            if not header:
                break
            sequence = infile.readline().strip()
            plus = infile.readline().strip()
            quality = infile.readline().strip()
            
            rev_comp_seq = reverse_complement(sequence)
            
            outfile.write(f"{header}\n{rev_comp_seq}\n{plus}\n{quality}\n")

def process_barcodes(input_txt, output_csv):
    with open(input_txt, 'r') as infile:
        lines = infile.readlines()
        if len(lines) < 2:
            raise ValueError("The barcode file does not have a second line.")
        
        barcodes = lines[1].strip().split(',')
    
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Feature Barcode name", "Feature Barcode sequence"])
        
        for i, barcode in enumerate(barcodes, start=1):
            writer.writerow([f"AB_{i}", reverse_complement(barcode) + "A"]) #add a standard "A" at the end because 
#To avoid potential pseudoalignment errors arising from inverted repeats, kallisto only accepts odd values for the k-mer length -k


if __name__ == "__main__":
    fastq_input_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/kite/joined_linker_ab/joined_linker_ab_kite.fastq"
    fastq_output_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/kite/joined_linker_ab/reverse_complement/joined_linker_ab_kite_reverse_complement.fastq"
    barcode_input_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/NKI/barcodes.txt"
    barcode_output_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/kite/joined_linker_ab_NKI/FeatureBarcodes.csv"
    
    # process_fastq(fastq_input_path, fastq_output_path)
    process_barcodes(barcode_input_path, barcode_output_path)