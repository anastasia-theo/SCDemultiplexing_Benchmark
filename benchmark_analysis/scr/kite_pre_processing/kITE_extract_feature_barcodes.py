######Extract feature barcodes using the NKI original dataset
###### and the linker as anchor


# from Bio import SeqIO
# from Bio.Seq import Seq

# def process_fastq(input_fastq, output_fastq, missing_linker_fastq, linker="CTTGTGGAAAGGACGAAACACCG", umi_length=15, ab_length=10):
#     with open(output_fastq, "w") as out_handle, open(missing_linker_fastq, "w") as missing_handle:
#         for record in SeqIO.parse(input_fastq, "fastq"):
#             sequence = str(record.seq)
#             quality = record.letter_annotations["phred_quality"]

#             # Find the linker position
#             linker_pos = sequence.find(linker)
            
#             if linker_pos != -1:
#                 start = linker_pos + len(linker)  # Position after the linker
#                 umi = sequence[start:start + umi_length]
#                 antibody = sequence[start + umi_length:start + umi_length + ab_length]

#                 # Extract quality scores
#                 umi_quality = quality[start:start + umi_length]
#                 antibody_quality = quality[start + umi_length:start + umi_length + ab_length]

#                 # Modify sequence and quality
#                 new_sequence = umi + antibody
#                 new_quality = umi_quality + antibody_quality

#                 # Clear letter annotations before updating the sequence
#                 record.letter_annotations.clear()

#                 # Update record
#                 record.seq = Seq(new_sequence)  # Convert to Seq object
#                 record.letter_annotations["phred_quality"] = new_quality

#                 # Write modified record
#                 SeqIO.write(record, out_handle, "fastq")
#             else:
#                 # If linker is not found, write the entire read to the missing linker file
#                 SeqIO.write(record, missing_handle, "fastq")
            

# if __name__ == "__main__":
#     process_fastq("/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/NKI/7659_1_UDI_well_G11_CCATAGACCT-GTTCTCACGG_S9_R1_001.fastq", 
#                   "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/kite/OG_linker/OG_linker_kite.fastq",
#                   "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/kite/OG_linker/OG_linker_missing_antibodies.fastq"
#     )




######Extract feature barcodes using the NKI joined dataset
###### and the linker as anchor



# from Bio import SeqIO
# from Bio.Seq import Seq

# def process_fastq(input_fastq, output_fastq, missing_linker_fastq, linker="CTTGTGGAAAGGACGAAACACCG", umi_length=15, ab_length=10):
#     with open(output_fastq, "w") as out_handle, open(missing_linker_fastq, "w") as missing_handle:
#         for record in SeqIO.parse(input_fastq, "fastq"):
#             sequence = str(record.seq)
#             quality = record.letter_annotations["phred_quality"]

#             # Find the linker position
#             linker_pos = sequence.find(linker)
            
#             if linker_pos != -1:
#                 start = linker_pos + len(linker)  # Position after the linker
#                 umi = sequence[start:start + umi_length]
#                 antibody = sequence[start + umi_length:start + umi_length + ab_length]

#                 # Extract quality scores
#                 umi_quality = quality[start:start + umi_length]
#                 antibody_quality = quality[start + umi_length:start + umi_length + ab_length]

#                 # Modify sequence and quality
#                 new_sequence = umi + antibody
#                 new_quality = umi_quality + antibody_quality

#                 # Clear letter annotations before updating the sequence
#                 record.letter_annotations.clear()

#                 # Update record
#                 record.seq = Seq(new_sequence)  # Convert to Seq object
#                 record.letter_annotations["phred_quality"] = new_quality

#                 # Write modified record
#                 SeqIO.write(record, out_handle, "fastq")
#             else:
#                 # If linker is not found, write the entire read to the missing linker file
#                 SeqIO.write(record, missing_handle, "fastq")
            

# if __name__ == "__main__":
#     process_fastq("/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/NKI/NKI_merged_join.fastq", 
#                   "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/kite/joined_linker/joined_linker_kite.fastq",
#                   "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/kite/joined_linker/joined_linker_missing_antibodies.fastq"
#     )




######Extract feature barcodes using the NKI joined dataset
###### and the ab as anchor




# from Bio import SeqIO
# from Bio.Seq import Seq

# def get_antibody_sequences(txt_file):
#     """Extract the antibody sequences from the second line of the given text file."""
#     with open(txt_file, "r") as f:
#         lines = f.readlines()
#         if len(lines) >= 2:
#             return set(lines[1].strip().split(","))  # Store as a set for fast lookup
#         return set()

# def process_fastq(input_fastq, output_fastq, missing_antibody_fastq, antibody_txt, umi_length=15):
#     """Process FASTQ file to extract UMI and antibody sequences based on known antibody sequences."""
    
#     # Load antibody sequences from the text file
#     antibody_set = get_antibody_sequences(antibody_txt)
    
#     with open(output_fastq, "w") as out_handle, open(missing_antibody_fastq, "w") as missing_handle:
#         for index, record in enumerate(SeqIO.parse(input_fastq, "fastq")):
#             sequence = str(record.seq)
#             quality = record.letter_annotations["phred_quality"]
            
#             found = False
#             for i in range(47, 69 - 10 + 1):  # Loop from position 47 to 58 (ensuring full 10 bases fit)
#                 candidate_antibody = sequence[i:i+10]
#                 if candidate_antibody in antibody_set:
#                     umi = sequence[i-umi_length:i]  # Extract UMI (15 bases before antibody)
#                     umi_quality = quality[i-umi_length:i]
#                     antibody_quality = quality[i:i+10]
                    
#                     # Modify sequence and quality
#                     new_sequence = umi + candidate_antibody
#                     new_quality = umi_quality + antibody_quality
                    
#                     # Clear letter annotations before updating the sequence
#                     record.letter_annotations.clear()
                    
#                     # Update record
#                     record.seq = Seq(new_sequence)
#                     record.letter_annotations["phred_quality"] = new_quality
                    
#                     # Write modified record
#                     SeqIO.write(record, out_handle, "fastq")
#                     found = True
#                     break  # Stop after the first match
            
#             if not found:
#                 SeqIO.write(record, missing_handle, "fastq")
#             if (index + 1) % 1000000 == 0:
#                 print(f"Processed {index + 1} reads.")
    
#     print("Processing complete!")
            

# if __name__ == "__main__":
#     process_fastq(
#         "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/NKI/NKI_merged_join.fastq", 
#         "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/kite/joined_ab/joined_ab_kite.fastq", 
#         "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/kite/joined_ab/joined_ab_missing_antibodies.fastq", 
#         "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/NKI/barcodes.txt"
#     )






######Extract feature barcodes using the NKI joined dataset
###### and the linker AND ab as anchor


from Bio import SeqIO
from Bio.Seq import Seq

def get_antibody_sequences(txt_file):
    """Extract the antibody sequences from the second line of the given text file."""
    with open(txt_file, "r") as f:
        lines = f.readlines()
        if len(lines) >= 2:
            return set(lines[1].strip().split(","))  # Store as a set for fast lookup
        return set()

def process_fastq(input_fastq, output_fastq, missing_fastq, antibody_txt, linker="CTTGTGGAAAGGACGAAACACCG", umi_length=15, ab_length=10):
    """Process FASTQ file to extract UMI and antibody sequences based on the linker or known antibody sequences."""
    
    # Load antibody sequences from the text file
    antibody_set = get_antibody_sequences(antibody_txt)
    
    with open(output_fastq, "w") as out_handle, open(missing_fastq, "w") as missing_handle:
        for index, record in enumerate(SeqIO.parse(input_fastq, "fastq")):
            sequence = str(record.seq)
            quality = record.letter_annotations["phred_quality"]
            
            found = False
            
            # Search for the linker first
            linker_pos = sequence.find(linker)
            if linker_pos != -1:
                start = linker_pos + len(linker)  # Position after the linker
                umi = sequence[start:start + umi_length]
                antibody = sequence[start + umi_length:start + umi_length + ab_length]
                
                # Extract quality scores
                umi_quality = quality[start:start + umi_length]
                antibody_quality = quality[start + umi_length:start + umi_length + ab_length]
                
                # Modify sequence and quality
                new_sequence = umi + antibody
                new_quality = umi_quality + antibody_quality
                
                found = True
            else:
                # If linker is not found, search for antibody in the 47-68 base range
                for i in range(47, 69 - 10 + 1):  # Loop from position 47 to 59
                    candidate_antibody = sequence[i:i+10]
                    if candidate_antibody in antibody_set:
                        umi = sequence[i-umi_length:i]  # Extract UMI (15 bases before antibody)
                        umi_quality = quality[i-umi_length:i]
                        antibody_quality = quality[i:i+10]
                        
                        # Modify sequence and quality
                        new_sequence = umi + candidate_antibody
                        new_quality = umi_quality + antibody_quality
                        
                        found = True
                        break  # Stop after the first match
            
            if found:
                # Clear letter annotations before updating the sequence
                record.letter_annotations.clear()
                
                # Update record
                record.seq = Seq(new_sequence)
                record.letter_annotations["phred_quality"] = new_quality
                
                # Write modified record
                SeqIO.write(record, out_handle, "fastq")
            else:
                SeqIO.write(record, missing_handle, "fastq")
            
            # Print progress every 10,000 reads
            if (index + 1) % 1000000 == 0:
                print(f"Processed {index + 1} reads.")
    
    print("Processing complete!")

if __name__ == "__main__":
    process_fastq(
        "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/NKI/NKI_merged_join.fastq", 
        "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/kite/joined_linker_ab/joined_linker_ab_kite.fastq", 
        "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/kite/joined_linker_ab/joined_linker_ab_missing_antibodies.fastq", 
        "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/NKI/barcodes.txt"
    )



