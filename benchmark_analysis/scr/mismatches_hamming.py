import random

def add_mismatches(sequence, num_of_mismatches, sequence_id, log_file):
    seq = list(sequence)
    mismatches_log = []
    used_positions = set() # I need this so it wont add a mismatch on the same position more than once
    
    for i in range(num_of_mismatches):
        
        position_in_seq = random.randint(0, len(seq) - 1)
        while position_in_seq in used_positions:
            position_in_seq = random.randint(0, len(seq) - 1)
        original = seq[position_in_seq]
        new_base = random.choice([b for b in 'ACGT' if b != original])
        seq[position_in_seq] = new_base
        mismatches_log.append(f"substitution: position {position_in_seq}, {original} -> {new_base}")

        used_positions.add(position_in_seq)

    # We will write the mismatch type and the position each time, and store it in this file
    with open(log_file, "a") as log:
        for i in mismatches_log:
            log.write(f"{sequence_id}: {i}\n")

    return ''.join(seq)

def apply_mismatches_to_file(input_fastq, output_fastq, log_file):
    with open(input_fastq, "r") as original_file, open(output_fastq, "w") as mismatched_file:
        for i, line in enumerate(original_file):
            line_index = i % 4

            if line_index == 0:
                sequence_id = line.strip()
                mismatched_file.write(line)
            
            elif line_index == 1:
                sequence = line.strip()
                # We know need to find the group for the specific sequence, meaning how many mismatches will be applied
                group = i // (4 * 100_000)
                mismatched_sequence =  add_mismatches(sequence, group, sequence_id, log_file)
                mismatched_file.write(mismatched_sequence +"\n")

            elif line_index == 2:
                mismatched_file.write(line)

            elif line_index == 3:
                mismatched_quality_scores = 'I' * len(mismatched_sequence)
                mismatched_file.write(mismatched_quality_scores + "\n")


if __name__ == "__main__":
    input_fastq = "/home/mrhin/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/artificial/ground_truth_sequences.fastq"
    output_fastq = "/home/mrhin/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/artificial/hamming/mismatched_fastq_hamming.fastq"
    log_file = "/home/mrhin/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/artificial/hamming/log_file_hamming.txt"

    
    with open(log_file, "w") as log:
        log.write("Mismatch Log\n")
        log.write("=" * 50 + "\n")

    apply_mismatches_to_file(input_fastq, output_fastq, log_file)



