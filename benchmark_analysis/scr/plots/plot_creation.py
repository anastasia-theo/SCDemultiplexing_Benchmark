import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# import sys

# Read file paths from command-line arguments
time_file_path_sc = "/home/mrhin/SCDemultiplexing_Benchmark/benchmark_analysis/results/SCDemultiplex_results/time_log.txt"
time_file_path_split = "/home/mrhin/SCDemultiplexing_Benchmark/benchmark_analysis/results/splitcode_results/time_log.txt"
memory_file_path_sc = "/home/mrhin/SCDemultiplexing_Benchmark/benchmark_analysis/results/SCDemultiplex_results/memory_log.txt"
memory_file_path_split = "/home/mrhin/SCDemultiplexing_Benchmark/benchmark_analysis/results/splitcode_results/memory_log.txt"
accuracy_file_path_sc = "/home/mrhin/SCDemultiplexing_Benchmark/benchmark_analysis/results/SCDemultiplex_results/accuracy_log.txt"
accuracy_file_path_split = "/home/mrhin/SCDemultiplexing_Benchmark/benchmark_analysis/results/splitcode_results/accuracy_log.txt" 
# filtered_percentage_file_path = sys.argv[4]
# output_plot_path = sys.argv[4]

# Read data
time_data_sc = pd.read_csv(time_file_path_sc, sep=' ', header=0)
time_data_split = pd.read_csv(time_file_path_split, sep=' ', header=0) 
memory_data_sc = pd.read_csv(memory_file_path_sc, sep=' ', header=0)
memory_data_split = pd.read_csv(memory_file_path_split, sep=' ', header=0)
accuracy_data_sc = pd.read_csv(accuracy_file_path_sc, sep=' ', header=0)
accuracy_data_split = pd.read_csv(accuracy_file_path_split, sep=' ', header=0)
# filtered_percentage_data = pd.read_csv(filtered_percentage_file_path, sep=' ', header=0)
# # Convert Filtered_Percentage to numeric values
# filtered_percentage_data['Filtered_Percentage(%)'] = filtered_percentage_data['Filtered_Percentage(%)'].str.replace('%', '').astype(float)

merged_time_data = pd.merge(time_data_sc, time_data_split, on='Mismatch', suffixes=('_SCDemultiplex', '_splitcode'))
print(merged_time_data)
merged_memory_data = pd.merge(memory_data_sc, memory_data_split, on='Mismatch', suffixes=('_SCDemultiplex', '_splitcode'))
merged_accuracy_data = pd.merge(accuracy_data_sc, accuracy_data_split, on='Mismatch', suffixes=('_SCDemultiplex', '_splitcode'))

x = merged_time_data['Mismatch']  # Mismatch values
bar_width = 0.4  # Width of each bar
x_indices = np.arange(len(x))  # Indices for the mismatches



# Create a figure with subplots for Time, Memory, and Accuracy
fig, axes = plt.subplots(1, 3, figsize=(20, 9))  # 1 row, 3 columns

color_sc = 'lightcoral'
color_split = 'lightgreen'

# Elapsed Time Plot
axes[0].bar(x_indices - bar_width/2, merged_time_data['Elapsed_Time(s)_SCDemultiplex'], bar_width, label='SCDemultiplex', color='lightcoral')
axes[0].bar(x_indices + bar_width/2, merged_time_data['Elapsed_Time(s)_splitcode'], bar_width, label='splitcode', color='lightgreen')
axes[0].set_title('Elapsed Time Comparison')
axes[0].set_xlabel('Mismatch')
axes[0].set_ylabel('Elapsed Time (seconds)')
axes[0].set_xticks(x_indices)
axes[0].set_xticklabels(x)
# axes[0].legend()

for i, value in enumerate(merged_time_data['Elapsed_Time(s)_SCDemultiplex']):
    axes[0].text(x_indices[i] - bar_width/2, value + value * 0.02, str(value), ha='center', va='bottom', fontsize=8)
for i, value in enumerate(merged_time_data['Elapsed_Time(s)_splitcode']):
    axes[0].text(x_indices[i] + bar_width/2, value + value * 0.02, str(value), ha='center', va='bottom', fontsize=8)


# Max Memory Plot
axes[1].bar(x_indices - bar_width/2, merged_memory_data['Max_Memory(KB)_SCDemultiplex'], bar_width, label='SCDemultiplex', color='lightcoral')
axes[1].bar(x_indices + bar_width/2, merged_memory_data['Max_Memory(KB)_splitcode'], bar_width, label='splitcode', color='lightgreen')
axes[1].set_title('Max Memory Comparison')
axes[1].set_xlabel('Mismatch')
axes[1].set_ylabel('Max Memory (KB)')
axes[1].set_xticks(x_indices)
axes[1].set_xticklabels(x)
# axes[1].legend()

for i, value in enumerate(merged_memory_data['Max_Memory(KB)_SCDemultiplex']):
    axes[1].text(x_indices[i] - bar_width/2, value + value * 0.02, str(value), ha='center', va='bottom', fontsize=8)
for i, value in enumerate(merged_memory_data['Max_Memory(KB)_splitcode']):
    axes[1].text(x_indices[i] + bar_width/2, value + value * 0.02, str(value), ha='center', va='bottom', fontsize=8)

# Accuracy Plot
axes[2].bar(x_indices - bar_width/2, merged_accuracy_data['Accuracy(%)_SCDemultiplex'], bar_width, label='SCDemultiplex', color='lightcoral')
axes[2].bar(x_indices + bar_width/2, merged_accuracy_data['Accuracy(%)_splitcode'], bar_width, label='splitcode', color='lightgreen')
axes[2].set_title('Accuracy Comparison')
axes[2].set_xlabel('Mismatch')
axes[2].set_ylabel('Accuracy (%)')
axes[2].set_xticks(x_indices)
axes[2].set_xticklabels(x)
# axes[2].legend()

for i, value in enumerate(merged_accuracy_data['Accuracy(%)_SCDemultiplex']):
    axes[2].text(x_indices[i] - bar_width/2, value + value * 0.02, str(value), ha='center', va='bottom', fontsize=8)
for i, value in enumerate(merged_accuracy_data['Accuracy(%)_splitcode']):
    axes[2].text(x_indices[i] + bar_width/2, value + value * 0.02, str(value), ha='center', va='bottom', fontsize=8)

# Move the legend below the plots
axes[1].legend(['SCDemultiplexing', 'splitcode'], loc='center', bbox_to_anchor=(0.5, -0.15), ncol=2, fontsize=12)

# Adjust layout to make more space for the legend
plt.subplots_adjust(bottom=0.1)

# Remove tight_layout to avoid conflict
plt.tight_layout(pad=5)
plt.savefig("/home/mrhin/SCDemultiplexing_Benchmark/benchmark_analysis/results/SCDemultiplex_results/plots/comparison_metrics.png")
plt.show()








# # Plotting
# fig, axes = plt.subplots(2, 2, figsize=(10, 10))
# axes[1, 1].axis('off')
# colors = ['lightcoral', 'lightblue', 'lightgreen', 'peachpuff', 'plum']

# # Bar plot for Mismatch vs Elapsed Time
# axes[0, 0].bar(time_data['Mismatch'], time_data['Elapsed_Time(s)'], color=colors[:len(time_data['Mismatch'])])
# axes[0, 0].set_title('Mismatch vs Elapsed Time')
# axes[0, 0].set_xlabel('Mismatch')
# axes[0, 0].set_ylabel('Elapsed Time (seconds)')
# axes[0, 0].set_xticks(time_data['Mismatch'])  # Setting x-axis to show mismatch numbers
# for i, value in enumerate(time_data['Elapsed_Time(s)']):
#     axes[0, 0].text(time_data['Mismatch'].iloc[i], value + 0.1, str(round(value, 2)), ha='center')  # Adding text on top of bars

# # Bar plot for Mismatch vs Max Memory
# axes[0, 1].bar(memory_data['Mismatch'], memory_data['Max_Memory(KB)'], color=colors[:len(time_data['Mismatch'])])
# axes[0, 1].set_title('Mismatch vs Max Memory')
# axes[0, 1].set_xlabel('Mismatch')
# axes[0, 1].set_ylabel('Max Memory (KB)')
# axes[0, 1].set_xticks(memory_data['Mismatch'])  # Setting x-axis to show mismatch numbers
# for i, value in enumerate(memory_data['Max_Memory(KB)']):
#     axes[0, 1].text(memory_data['Mismatch'].iloc[i], value + 1000, str(value), ha='center')  # Adding text on top of bars

# # Bar plot for Mismatch vs Accuracy
# axes[1, 0].bar(accuracy_data['Mismatch'], accuracy_data['Accuracy(%)'], color=colors[:len(time_data['Mismatch'])])
# axes[1, 0].set_title('Mismatch vs Accuracy')
# axes[1, 0].set_xlabel('Mismatch')
# axes[1, 0].set_ylabel('Accuracy(%)')
# axes[1, 0].set_xticks(accuracy_data['Mismatch'])  # Setting x-axis to show mismatch numbers
# for i, value in enumerate(accuracy_data['Accuracy(%)']):
#     axes[1, 0].text(accuracy_data['Mismatch'].iloc[i], value + 0.1, str(value), ha='center')  # Adding text on top of bars

# # # Bar plot for Mismatch vs Filtered Percentage
# # axes[1, 1].bar(filtered_percentage_data['Mismatch'], filtered_percentage_data['Filtered_Percentage(%)'], color=colors[:len(time_data['Mismatch'])])
# # axes[1, 1].set_title('Mismatch vs Filtered Percentage')
# # axes[1, 1].set_xlabel('Mismatch')
# # axes[1, 1].set_ylabel('Filtered Percentage (%)')
# # axes[1, 1].set_xticks(filtered_percentage_data['Mismatch'])  # Setting x-axis to show mismatch numbers
# # for i, value in enumerate(filtered_percentage_data['Filtered_Percentage(%)']):
# #     axes[1, 1].text(filtered_percentage_data['Mismatch'].iloc[i], value + 0.05, str(round(value, 2)), ha='center')  # Adding text on top of bars

# plt.tight_layout()
# plt.savefig("/home/mrhin/SCDemultiplexing_Benchmark/benchmark_analysis/results/SCDemultiplex_results/plots/metrics_scdemultiplex.png")







# # Read data
# time_data = pd.read_csv(time_file_path, sep=' ', header=0)
# memory_data = pd.read_csv(memory_file_path, sep=' ', header=0)
# accuracy_data = pd.read_csv(accuracy_file_path, sep=' ', header=0)
# # filtered_percentage_data = pd.read_csv(filtered_percentage_file_path, sep=' ', header=0)
# # # Convert Filtered_Percentage to numeric values
# # filtered_percentage_data['Filtered_Percentage(%)'] = filtered_percentage_data['Filtered_Percentage(%)'].str.replace('%', '').astype(float)

# # Plotting
# fig, axes = plt.subplots(2, 2, figsize=(10, 10))
# axes[1, 1].axis('off')
# colors = ['lightcoral', 'lightblue', 'lightgreen', 'peachpuff', 'plum']

# # Bar plot for Mismatch vs Elapsed Time
# axes[0, 0].bar(time_data['Mismatch'], time_data['Elapsed_Time(s)'], color=colors[:len(time_data['Mismatch'])])
# axes[0, 0].set_title('Mismatch vs Elapsed Time')
# axes[0, 0].set_xlabel('Mismatch')
# axes[0, 0].set_ylabel('Elapsed Time (seconds)')
# axes[0, 0].set_xticks(time_data['Mismatch'])  # Setting x-axis to show mismatch numbers
# for i, value in enumerate(time_data['Elapsed_Time(s)']):
#     axes[0, 0].text(time_data['Mismatch'].iloc[i], value + 0.1, str(round(value, 2)), ha='center')  # Adding text on top of bars

# # Bar plot for Mismatch vs Max Memory
# axes[0, 1].bar(memory_data['Mismatch'], memory_data['Max_Memory(KB)'], color=colors[:len(time_data['Mismatch'])])
# axes[0, 1].set_title('Mismatch vs Max Memory')
# axes[0, 1].set_xlabel('Mismatch')
# axes[0, 1].set_ylabel('Max Memory (KB)')
# axes[0, 1].set_xticks(memory_data['Mismatch'])  # Setting x-axis to show mismatch numbers
# for i, value in enumerate(memory_data['Max_Memory(KB)']):
#     axes[0, 1].text(memory_data['Mismatch'].iloc[i], value + 1000, str(value), ha='center')  # Adding text on top of bars

# # Bar plot for Mismatch vs Accuracy
# axes[1, 0].bar(accuracy_data['Mismatch'], accuracy_data['Accuracy(%)'], color=colors[:len(time_data['Mismatch'])])
# axes[1, 0].set_title('Mismatch vs Accuracy')
# axes[1, 0].set_xlabel('Mismatch')
# axes[1, 0].set_ylabel('Accuracy(%)')
# axes[1, 0].set_xticks(accuracy_data['Mismatch'])  # Setting x-axis to show mismatch numbers
# for i, value in enumerate(accuracy_data['Accuracy(%)']):
#     axes[1, 0].text(accuracy_data['Mismatch'].iloc[i], value + 0.1, str(value), ha='center')  # Adding text on top of bars

# # # Bar plot for Mismatch vs Filtered Percentage
# # axes[1, 1].bar(filtered_percentage_data['Mismatch'], filtered_percentage_data['Filtered_Percentage(%)'], color=colors[:len(time_data['Mismatch'])])
# # axes[1, 1].set_title('Mismatch vs Filtered Percentage')
# # axes[1, 1].set_xlabel('Mismatch')
# # axes[1, 1].set_ylabel('Filtered Percentage (%)')
# # axes[1, 1].set_xticks(filtered_percentage_data['Mismatch'])  # Setting x-axis to show mismatch numbers
# # for i, value in enumerate(filtered_percentage_data['Filtered_Percentage(%)']):
# #     axes[1, 1].text(filtered_percentage_data['Mismatch'].iloc[i], value + 0.05, str(round(value, 2)), ha='center')  # Adding text on top of bars

# plt.tight_layout()
# plt.savefig("/home/mrhin/SCDemultiplexing_Benchmark/benchmark_analysis/results/SCDemultiplex_results/plots/metrics_scdemultiplex.png")

