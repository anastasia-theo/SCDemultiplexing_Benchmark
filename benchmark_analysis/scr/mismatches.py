import random


def add_mismatches(sequence, num_of_mismatches, sequence_id, log_file):
    seq = list(sequence)
    mismatches_log = []


    for i in range(num_of_mismatches):
        type = random.choice(['deletion', 'insertion', 'substitution'])
        position_in_seq = random.randint(0, len(seq) - 1)

        if type == 'deletion':
            deleted_base = seq.pop(position_in_seq)
            mismatches_log.append(f"deletion: position {position_in_seq}, removed {deleted_base}")

        elif type == 'insertion':
            new_base = random.choice("ACGT")
            seq.insert(position_in_seq + 1, new_base)
            mismatches_log.append(f"insertion: position {position_in_seq + 1}, added {new_base}")
        
        elif type == 'substitution':
            original = seq[position_in_seq]
            new_base = random.choice([b for b in 'ACGT' if b != original])
            seq[position_in_seq] = new_base
            mismatches_log.append(f"substitution: position {position_in_seq}, {original} -> {new_base}")

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
    output_fastq = "/home/mrhin/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/artificial/mismatched_fastq.fastq"
    log_file = "/home/mrhin/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/artificial/log_file.txt"

    
    with open(log_file, "w") as log:
        log.write("Mismatch Log\n")
        log.write("=" * 50 + "\n")

    apply_mismatches_to_file(input_fastq, output_fastq, log_file)



