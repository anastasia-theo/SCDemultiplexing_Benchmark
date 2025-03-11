# LOG




# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np

# # Sample data for elapsed time (in seconds)
# elapsed_times_tool1 = [
#     [8, 9, 9, 25, 381],  # Dataset 1
#     [7, 7, 8, 22, 335],  # Dataset 2
#     [274, 271, 268, 472, 2097],  # Dataset 3
#     [505, 545, 595, 879, 2453]  # Dataset 4
# ]

# elapsed_times_tool2 = [
#     [278, 241, 213, 201, 198],  # Dataset 1
#     [289, 259, 236, 227, 223],  # Dataset 2
#     [3558, 2244, 1812, 1782, 1764],  # Dataset 3
#     [15756, 12858, 13844, 13900, 13040]  # Dataset 4
# ]

# # Convert Dataset 3 and Dataset 4 elapsed times from seconds to hours
# elapsed_times_tool1[2] = [x / 60 for x in elapsed_times_tool1[2]]  # Dataset 3
# elapsed_times_tool1[3] = [x / 60 for x in elapsed_times_tool1[3]]  # Dataset 4
# elapsed_times_tool2[2] = [x / 60 for x in elapsed_times_tool2[2]]  # Dataset 3
# elapsed_times_tool2[3] = [x / 60 for x in elapsed_times_tool2[3]]  # Dataset 4

# # Sample data for max memory (in KB)
# max_memory_tool1 = [
#     [92908, 120544, 161556, 1336172, 20921848],  # Dataset 1
#     [68984, 74064, 136844, 1335988, 20921760],  # Dataset 2
#     [1612732, 1612732, 1612732, 1612732, 88501428],  # Dataset 3
#     [304288, 413896, 902972, 5637436, 47136372]  # Dataset 4
# ]

# max_memory_tool2 = [
#     [79416, 117356, 140480, 152012, 154928],  # Dataset 1
#     [61826, 97152, 118268, 128428, 134524],  # Dataset 2
#     [1630900, 1733932, 1750920, 1767988, 1773036],  # Dataset 3
#     [18100248, 18389944, 18397660, 18400248, 18399488]  # Dataset 4
# ]

# # Convert memory from KB to GB
# max_memory_tool1 = np.array(max_memory_tool1) / 1e6  # Convert KB to GB
# max_memory_tool2 = np.array(max_memory_tool2) / 1e6  # Convert KB to GB

# # Dataset names
# datasets = ["Artificial Subs", "Artificial Subs+Indels", "SIGNAL_seq", "NKI"]
# mismatches = np.array([1, 2, 3, 4, 5])

# # Colors and line styles
# tool_colors = sns.color_palette("tab10", 2)  # Blue and orange for the two tools
# kite_color = "lightgreen"
# dataset_line_styles = ["-", "--", "-.", ":"]  # Line styles for datasets

# # Create a 3x2 grid of subplots
# fig, axes = plt.subplots(3, 2, figsize=(14, 18))

# # Increase font size for all text
# plt.rcParams.update({'font.size': 12})

# # Function to log-scale the y-axis while keeping original tick labels
# def log_scale_with_original_labels(ax, data):
#     ax.set_yscale('log')  # Apply log scaling
#     # Set y-ticks to original values
#     y_ticks = np.unique(np.round(np.log10(data), decimals=2))
#     ax.set_yticks(10**y_ticks)
#     ax.set_yticklabels([f"{int(10**y)}" for y in y_ticks])

# # Plot elapsed time for the first two datasets (top-left)
# for i in range(2):  # First two datasets
#     axes[0, 0].plot(mismatches, elapsed_times_tool1[i], label=f"{datasets[i]} - splitcode", 
#                     color=tool_colors[0], linestyle=dataset_line_styles[i], linewidth=2)
#     axes[0, 0].plot(mismatches, elapsed_times_tool2[i], label=f"{datasets[i]} - SCDemultiplexing Pipeline", 
#                     color=tool_colors[1], linestyle=dataset_line_styles[i], linewidth=2)

# axes[0, 0].set_xlabel("Number of Mismatches", fontsize=12)
# axes[0, 0].set_ylabel("Elapsed Time (s)", fontsize=12)
# axes[0, 0].set_title("Elapsed Time: Artificial Subs & Artificial Subs+Indels", fontsize=14)
# axes[0, 0].grid(True, linestyle="--", alpha=0.6)
# axes[0, 0].legend(loc='upper left', fontsize=10)
# axes[0, 0].set_xticks(mismatches)
# axes[0, 0].set_xticklabels([str(m) for m in mismatches], fontsize=10)
# log_scale_with_original_labels(axes[0, 0], np.concatenate((elapsed_times_tool1[0], elapsed_times_tool2[0])))

# # Plot elapsed time for the last two datasets (top-right)
# for i in range(2, 4):  # Last two datasets
#     axes[0, 1].plot(mismatches, elapsed_times_tool1[i], label=f"{datasets[i]} - splitcode", 
#                     color=tool_colors[0], linestyle=dataset_line_styles[i], linewidth=2)
#     axes[0, 1].plot(mismatches, elapsed_times_tool2[i], label=f"{datasets[i]} - SCDemultiplexing Pipeline", 
#                     color=tool_colors[1], linestyle=dataset_line_styles[i], linewidth=2)

# axes[0, 1].set_xlabel("Number of Mismatches", fontsize=12)
# axes[0, 1].set_ylabel("Elapsed Time (m)", fontsize=12)  # Updated y-axis label
# axes[0, 1].set_title("Elapsed Time: SIGNAL_seq & NKI", fontsize=14)
# axes[0, 1].grid(True, linestyle="--", alpha=0.6)
# axes[0, 1].legend(loc='upper left', fontsize=10)
# axes[0, 1].set_xticks(mismatches)
# axes[0, 1].set_xticklabels([str(m) for m in mismatches], fontsize=10)
# log_scale_with_original_labels(axes[0, 1], np.concatenate((elapsed_times_tool1[2], elapsed_times_tool2[2])))

# # Plot max memory for the first two datasets (middle-left)
# for i in range(2):  # First two datasets
#     axes[1, 0].plot(mismatches, max_memory_tool1[i], label=f"{datasets[i]} - splitcode", 
#                     color=tool_colors[0], linestyle=dataset_line_styles[i], linewidth=2)
#     axes[1, 0].plot(mismatches, max_memory_tool2[i], label=f"{datasets[i]} - SCDemultiplexing Pipeline", 
#                     color=tool_colors[1], linestyle=dataset_line_styles[i], linewidth=2)

# axes[1, 0].set_xlabel("Number of Mismatches", fontsize=12)
# axes[1, 0].set_ylabel("Max Memory (GB)", fontsize=12)
# axes[1, 0].set_title("Max Memory: Artificial Subs & Artificial Subs+Indels", fontsize=14)
# axes[1, 0].grid(True, linestyle="--", alpha=0.6)
# axes[1, 0].legend(loc='upper left', fontsize=10)
# axes[1, 0].set_xticks(mismatches)
# axes[1, 0].set_xticklabels([str(m) for m in mismatches], fontsize=10)
# log_scale_with_original_labels(axes[1, 0], np.concatenate((max_memory_tool1[0], max_memory_tool2[0])))

# # Plot max memory for the last two datasets (middle-right)
# for i in range(2, 4):  # Last two datasets
#     axes[1, 1].plot(mismatches, max_memory_tool1[i], label=f"{datasets[i]} - splitcode", 
#                     color=tool_colors[0], linestyle=dataset_line_styles[i], linewidth=2)
#     axes[1, 1].plot(mismatches, max_memory_tool2[i], label=f"{datasets[i]} - SCDemultiplexing Pipeline", 
#                     color=tool_colors[1], linestyle=dataset_line_styles[i], linewidth=2)

# axes[1, 1].set_xlabel("Number of Mismatches", fontsize=12)
# axes[1, 1].set_ylabel("Max Memory (GB)", fontsize=12)
# axes[1, 1].set_title("Max Memory: SIGNAL_seq & NKI", fontsize=14)
# axes[1, 1].grid(True, linestyle="--", alpha=0.6)
# axes[1, 1].legend(loc='upper left', fontsize=10)
# axes[1, 1].set_xticks(mismatches)
# axes[1, 1].set_xticklabels([str(m) for m in mismatches], fontsize=10)
# log_scale_with_original_labels(axes[1, 1], np.concatenate((max_memory_tool1[2], max_memory_tool2[2])))

# # Add new subplot for elapsed time (bottom-left) - Bar Plot
# tools = ["kite", "SCDemultiplexing"]
# elapsed_times_new = [304, 132]  # Elapsed times in seconds
# axes[2, 0].bar(tools, elapsed_times_new, color=[kite_color, tool_colors[1]], alpha=0.7)
# axes[2, 0].set_xlabel("Tool", fontsize=12)
# axes[2, 0].set_ylabel("Elapsed Time (s)", fontsize=12)
# axes[2, 0].set_title("Elapsed Time: kite vs SCDemultiplexing", fontsize=14)
# axes[2, 0].grid(True, linestyle="--", alpha=0.6)

# # Add new subplot for max memory (bottom-right) - Bar Plot
# max_memory_new = [4231300 / 1e6, 1435824 / 1e6]  # Convert KB to GB
# axes[2, 1].bar(tools, max_memory_new, color=[kite_color, tool_colors[1]], alpha=0.7)
# axes[2, 1].set_xlabel("Tool", fontsize=12)
# axes[2, 1].set_ylabel("Max Memory (GB)", fontsize=12)
# axes[2, 1].set_title("Max Memory: kite vs SCDemultiplexing", fontsize=14)
# axes[2, 1].grid(True, linestyle="--", alpha=0.6)

# # Add panel labels (A, B, C, D, E, F)
# for i, ax in enumerate(axes.flatten()):
#     ax.text(-0.1, 1.1, chr(65 + i), transform=ax.transAxes, fontsize=16, fontweight='bold', va='top')

# # Adjust layout
# plt.tight_layout()

# # Save the figure
# output_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/plots/combined_comparison_subplots.png"
# plt.savefig(output_path, dpi=300, bbox_inches="tight")

# plt.show()





import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Sample data for elapsed time (in seconds)
elapsed_times_tool1 = [
    [8, 9, 9, 25, 381],  # Dataset 1
    [7, 7, 8, 22, 335],  # Dataset 2
    [274, 271, 268, 472, 2097],  # Dataset 3
    [505, 545, 595, 879, 2453]  # Dataset 4
]

elapsed_times_tool2 = [
    [278, 241, 213, 201, 198],  # Dataset 1
    [289, 259, 236, 227, 223],  # Dataset 2
    [3558, 2244, 1812, 1782, 1764],  # Dataset 3
    [15756, 12858, 13844, 13900, 13040]  # Dataset 4
]

# Convert Dataset 3 and Dataset 4 elapsed times from seconds to minutes
elapsed_times_tool1[2] = [x / 3600 for x in elapsed_times_tool1[2]]  # Dataset 3
elapsed_times_tool1[3] = [x / 3600 for x in elapsed_times_tool1[3]]  # Dataset 4
elapsed_times_tool2[2] = [x / 3600 for x in elapsed_times_tool2[2]]  # Dataset 3
elapsed_times_tool2[3] = [x / 3600 for x in elapsed_times_tool2[3]]  # Dataset 4

# Sample data for max memory (in KB)
max_memory_tool1 = [
    [92908, 120544, 161556, 1336172, 20921848],  # Dataset 1
    [68984, 74064, 136844, 1335988, 20921760],  # Dataset 2
    [1612732, 1612732, 1612732, 1612732, 88501428],  # Dataset 3
    [304288, 413896, 902972, 5637436, 47136372]  # Dataset 4
]

max_memory_tool2 = [
    [79416, 117356, 140480, 152012, 154928],  # Dataset 1
    [61826, 97152, 118268, 128428, 134524],  # Dataset 2
    [1630900, 1733932, 1750920, 1767988, 1773036],  # Dataset 3
    [18100248, 18389944, 18397660, 18400248, 18399488]  # Dataset 4
]

# Convert memory from KB to GB
max_memory_tool1 = np.array(max_memory_tool1) / 1e6  # Convert KB to GB
max_memory_tool2 = np.array(max_memory_tool2) / 1e6  # Convert KB to GB

# Dataset names
datasets = ["Artificial Subs", "Artificial Subs+Indels", "SIGNAL_seq", "NKI"]
mismatches = np.array([1, 2, 3, 4, 5])

# Colors and line styles
tool_colors = sns.color_palette("tab10", 2)  # Blue and orange for the two tools
kite_color = "lightgreen"
dataset_line_styles = ["-", "--", "-.", ":"]  # Line styles for datasets

# Create a 3x2 grid of subplots
fig, axes = plt.subplots(3, 2, figsize=(12, 16))

# Increase font size
plt.rcParams.update({'font.size': 12})


# Plot elapsed time for the first two datasets (top-left)
for i in range(2):  # First two datasets
    axes[0, 0].plot(mismatches, elapsed_times_tool1[i], label=f"{datasets[i]} - splitcode", 
                    color=tool_colors[0], linestyle=dataset_line_styles[i], linewidth=2)
    axes[0, 0].plot(mismatches, elapsed_times_tool2[i], label=f"{datasets[i]} - SCDemultiplexing Pipeline", 
                    color=tool_colors[1], linestyle=dataset_line_styles[i], linewidth=2)

axes[0, 0].set_xlabel("Number of Mismatches", fontsize=12)
axes[0, 0].set_ylabel("Elapsed Time (s)", fontsize=12)
axes[0, 0].set_title("Elapsed Time: Artificial Subs & Artificial Subs+Indels", fontsize=14)
axes[0, 0].grid(True, linestyle="--", alpha=0.6)
axes[0, 0].legend(loc='upper left', fontsize=10)
axes[0, 0].set_xticks(mismatches)
axes[0, 0].set_xticklabels([str(m) for m in mismatches], fontsize=10)

# Plot elapsed time for the last two datasets (top-right)
for i in range(2, 4):  # Last two datasets
    axes[0, 1].plot(mismatches, elapsed_times_tool1[i], label=f"{datasets[i]} - splitcode", 
                    color=tool_colors[0], linestyle=dataset_line_styles[i], linewidth=2)
    axes[0, 1].plot(mismatches, elapsed_times_tool2[i], label=f"{datasets[i]} - SCDemultiplexing Pipeline", 
                    color=tool_colors[1], linestyle=dataset_line_styles[i], linewidth=2)

axes[0, 1].set_xlabel("Number of Mismatches", fontsize=12)
axes[0, 1].set_ylabel("Elapsed Time (m)", fontsize=12)  # Updated y-axis label
axes[0, 1].set_title("Elapsed Time: SIGNAL_seq & NKI")
axes[0, 1].grid(True, linestyle="--", alpha=0.6)
axes[0, 1].legend(loc='upper left', fontsize=10)
axes[0, 1].set_ylim(0, max(max(elapsed_times_tool1[2] + elapsed_times_tool1[3]), max(elapsed_times_tool2[2] + elapsed_times_tool2[3])) + 2)
axes[0, 1].set_xticks(mismatches)
axes[0, 1].set_xticklabels([str(m) for m in mismatches], fontsize=10)

# Plot max memory for the first two datasets (middle-left)
for i in range(2):  # First two datasets
    axes[1, 0].plot(mismatches, max_memory_tool1[i], label=f"{datasets[i]} - splitcode", 
                    color=tool_colors[0], linestyle=dataset_line_styles[i], linewidth=2)
    axes[1, 0].plot(mismatches, max_memory_tool2[i], label=f"{datasets[i]} - SCDemultiplexing Pipeline", 
                    color=tool_colors[1], linestyle=dataset_line_styles[i], linewidth=2)

axes[1, 0].set_xlabel("Number of Mismatches", fontsize=12)
axes[1, 0].set_ylabel("Max Memory (GB)", fontsize=12)
axes[1, 0].set_title("Max Memory: Artificial Subs & Artificial Subs+Indels")
axes[1, 0].grid(True, linestyle="--", alpha=0.6)
axes[1, 0].legend(loc='upper left', fontsize=10)
axes[1, 0].set_xticks(mismatches)
axes[1, 0].set_xticklabels([str(m) for m in mismatches], fontsize=10)

# Plot max memory for the last two datasets (middle-right)
for i in range(2, 4):  # Last two datasets
    axes[1, 1].plot(mismatches, max_memory_tool1[i], label=f"{datasets[i]} - splitcode", 
                    color=tool_colors[0], linestyle=dataset_line_styles[i], linewidth=2)
    axes[1, 1].plot(mismatches, max_memory_tool2[i], label=f"{datasets[i]} - SCDemultiplexing Pipeline", 
                    color=tool_colors[1], linestyle=dataset_line_styles[i], linewidth=2)

axes[1, 1].set_xlabel("Number of Mismatches", fontsize=12)
axes[1, 1].set_ylabel("Max Memory (GB)", fontsize=12)
axes[1, 1].set_title("Max Memory: SIGNAL_seq & NKI")
axes[1, 1].grid(True, linestyle="--", alpha=0.6)
axes[1, 1].legend(loc='upper left', fontsize=10)
axes[1, 1].set_xticks(mismatches)
axes[1, 1].set_xticklabels([str(m) for m in mismatches], fontsize=10)

# Add new subplot for elapsed time (bottom-left) - Bar Plot
tools = ["kite", "SCDemultiplexing"]
elapsed_times_new = [304, 132]  # Elapsed times in seconds
axes[2, 0].bar(tools, elapsed_times_new, color=[kite_color, tool_colors[1]], alpha=0.7)
axes[2, 0].set_xlabel("Tool", fontsize=12)
axes[2, 0].set_ylabel("Elapsed Time (s)", fontsize=12)
axes[2, 0].set_title("Elapsed Time: kite vs SCDemultiplexing", fontsize=14)
axes[2, 0].grid(True, linestyle="--", alpha=0.6)

# Add new subplot for max memory (bottom-right) - Bar Plot
max_memory_new = [4231300 / 1e6, 1435824 / 1e6]  # Convert KB to GB
axes[2, 1].bar(tools, max_memory_new, color=[kite_color, tool_colors[1]], alpha=0.7)
axes[2, 1].set_xlabel("Tool", fontsize=12)
axes[2, 1].set_ylabel("Max Memory (GB)", fontsize=12)
axes[2, 1].set_title("Max Memory: kite vs SCDemultiplexing", fontsize=14)
axes[2, 1].grid(True, linestyle="--", alpha=0.6)

# Add panel labels (A, B, C, D, E, F)
for i, ax in enumerate(axes.flatten()):
    ax.text(-0.1, 1.1, chr(65 + i), transform=ax.transAxes, fontsize=16, fontweight='bold', va='top')

# Adjust layout
plt.tight_layout()

# Save the figure
output_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/plots/combined_comparison_subplots.png"
plt.savefig(output_path, dpi=300, bbox_inches="tight")

plt.show()

