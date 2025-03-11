def find_min_max_mean_excluding_outliers(file_path):
    # Initialize the min, max, sums, and counts for each column
    min_vals = [float('inf'), float('inf'), float('inf')]  # Min values for column 1, column 2, column 3
    max_vals = [float('-inf'), float('-inf'), float('-inf')]  # Max values for column 1, column 2, column 3
    sums = [0, 0, 0]  # Sums for column 1, column 2, column 3
    counts = [0, 0, 0]  # Counts for column 1, column 2, column 3
    
    # Open and read the file
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into values based on commas
            row = line.strip().split(',')
            
            # Check if the row contains exactly 3 values
            if len(row) == 3:
                # Convert the values to integers
                values = [int(val) for val in row]
                
                # Skip the row if any value is greater than 100
                if any(val > 45 for val in values):
                    continue  # Skip this line if condition is met
                
                # Debug print to check the current row being processed
                print(f"Processing row: {values}")
                
                # Update the min, max, sums, and counts for each column
                for i in range(3):
                    min_vals[i] = min(min_vals[i], values[i])
                    max_vals[i] = max(max_vals[i], values[i])
                    sums[i] += values[i]
                    counts[i] += 1

    # Calculate the mean for each column
    means = [sums[i] / counts[i] if counts[i] > 0 else 0 for i in range(3)]
    
    # Print the final min, max, and mean values for each column
    print(f"\nMin values: {min_vals}")
    print(f"Max values: {max_vals}")
    print(f"Mean values: {means}")

# Provide the path to your file
file_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/raw_data/tape_data/polyA_results_new.txt"  # Replace with the actual path to your text file
find_min_max_mean_excluding_outliers(file_path)

