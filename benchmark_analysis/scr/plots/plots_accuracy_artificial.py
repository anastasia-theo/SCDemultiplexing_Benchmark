# import matplotlib.pyplot as plt
# import numpy as np

# # Data for Tool 1 (splitcode)
# tool1_dataset1_true_reads = [380445, 635804, 329375, 0, 0]
# tool1_dataset2_true_reads = [151208, 163388, 140763, 0, 0]

# tool1_dataset1_false_reads = [166, 4571, 74, 0, 0]
# tool1_dataset2_false_reads = [174, 2211, 790, 0, 0]

# # Data for Tool 2 (SCDemultiplexing Pipeline)
# tool2_dataset1_true_reads = [360212, 536297, 652396, 704772, 719540]
# tool2_dataset2_true_reads = [264473, 426690, 515255, 564098, 580747]

# tool2_dataset1_false_reads = [1761, 7878, 15000, 19677, 21349]
# tool2_dataset2_false_reads = [1813, 9677, 19432, 28542, 33826]

# # Mismatch levels
# mismatches = [1, 2, 3, 4, 5]
# x = np.arange(len(mismatches))  # X-axis positions

# # Bar width
# bar_width = 0.35

# # Create a 2x2 grid of subplots
# fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# # Plot for Dataset 1 - True Reads (Top-left)
# axes[0, 0].bar(x - bar_width/2, tool1_dataset1_true_reads, width=bar_width, label="splitcode", color="skyblue")
# axes[0, 0].bar(x + bar_width/2, tool2_dataset1_true_reads, width=bar_width, label="SCDemultiplexing Pipeline", color="orange")
# axes[0, 0].set_xlabel("Number of Mismatches")
# axes[0, 0].set_ylabel("True Reads")
# axes[0, 0].set_title("Dataset 1: Artificial Subs - True Reads")
# axes[0, 0].set_xticks(x)
# axes[0, 0].set_xticklabels(mismatches)
# axes[0, 0].set_ylim(0, 1_000_000)  # Set y-axis limit to 1 million
# axes[0, 0].legend(loc="upper left")
# axes[0, 0].grid(True, linestyle="--", alpha=0.6)
# axes[0, 0].ticklabel_format(axis='y', style='plain')  # Disable scientific notation

# # Plot for Dataset 2 - True Reads (Top-right)
# axes[0, 1].bar(x - bar_width/2, tool1_dataset2_true_reads, width=bar_width, label="splitcode", color="lightgreen")
# axes[0, 1].bar(x + bar_width/2, tool2_dataset2_true_reads, width=bar_width, label="SCDemultiplexing Pipeline", color="red")
# axes[0, 1].set_xlabel("Number of Mismatches")
# axes[0, 1].set_ylabel("True Reads")
# axes[0, 1].set_title("Dataset 2: Artificial Subs+Indels - True Reads")
# axes[0, 1].set_xticks(x)
# axes[0, 1].set_xticklabels(mismatches)
# axes[0, 1].set_ylim(0, 1_000_000)  # Set y-axis limit to 1 million
# axes[0, 1].legend(loc="upper left")
# axes[0, 1].grid(True, linestyle="--", alpha=0.6)
# axes[0, 1].ticklabel_format(axis='y', style='plain')  # Disable scientific notation

# # Plot for Dataset 1 - False Reads (Bottom-left)
# axes[1, 0].bar(x - bar_width/2, tool1_dataset1_false_reads, width=bar_width, label="splitcode", color="skyblue")
# axes[1, 0].bar(x + bar_width/2, tool2_dataset1_false_reads, width=bar_width, label="SCDemultiplexing Pipeline", color="orange")
# axes[1, 0].set_xlabel("Number of Mismatches")
# axes[1, 0].set_ylabel("False Reads")
# axes[1, 0].set_title("Dataset 1: Artificial Subs - False Reads")
# axes[1, 0].set_xticks(x)
# axes[1, 0].set_xticklabels(mismatches)
# axes[1, 0].set_ylim(0, 40_000)  # Set y-axis limit to 1 million
# axes[1, 0].legend(loc="upper left")
# axes[1, 0].grid(True, linestyle="--", alpha=0.6)
# axes[1, 0].ticklabel_format(axis='y', style='plain')  # Disable scientific notation

# # Plot for Dataset 2 - False Reads (Bottom-right)
# axes[1, 1].bar(x - bar_width/2, tool1_dataset2_false_reads, width=bar_width, label="splitcode", color="lightgreen")
# axes[1, 1].bar(x + bar_width/2, tool2_dataset2_false_reads, width=bar_width, label="SCDemultiplexing Pipeline", color="red")
# axes[1, 1].set_xlabel("Number of Mismatches")
# axes[1, 1].set_ylabel("False Reads")
# axes[1, 1].set_title("Dataset 2: Artificial Subs+Indels - False Reads")
# axes[1, 1].set_xticks(x)
# axes[1, 1].set_xticklabels(mismatches)
# axes[1, 1].set_ylim(0, 40_000)  # Set y-axis limit to 1 million
# axes[1, 1].legend(loc="upper left")
# axes[1, 1].grid(True, linestyle="--", alpha=0.6)
# axes[1, 1].ticklabel_format(axis='y', style='plain')  # Disable scientific notation

# # Add panel labels (A, B, C, D)
# for i, ax in enumerate(axes.flatten()):
#     ax.text(-0.1, 1.1, chr(65 + i), transform=ax.transAxes, fontsize=16, fontweight='bold', va='top')

# # Adjust layout
# plt.tight_layout()

# # Save the figure
# output_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/plots/true_false_reads_comparison_subplots.png"
# plt.savefig(output_path, dpi=300, bbox_inches="tight")

# # Show the plot
# plt.show()



import matplotlib.pyplot as plt
import numpy as np

# Data for Tool 1 (splitcode)
tool1_dataset1_true_reads = [380445, 635804, 329375, 0, 0]
tool1_dataset2_true_reads = [151208, 163388, 140763, 0, 0]

tool1_dataset1_false_reads = [166, 4571, 74, 0, 0]
tool1_dataset2_false_reads = [174, 2211, 790, 0, 0]

# Data for Tool 2 (SCDemultiplexing Pipeline)
tool2_dataset1_true_reads = [360212, 536297, 652396, 704772, 719540]
tool2_dataset2_true_reads = [264473, 426690, 515255, 564098, 580747]

tool2_dataset1_false_reads = [1761, 7878, 15000, 19677, 21349]
tool2_dataset2_false_reads = [1813, 9677, 19432, 28542, 33826]

# Mismatch levels
mismatches = [1, 2, 3, 4, 5]
x = np.arange(len(mismatches))  # X-axis positions

# Bar width
bar_width = 0.35

# Colors for tools
tool_colors = {"splitcode": "skyblue", "SCDemultiplexing Pipeline": "orange"}

# Create a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# Plot for Dataset 1 - True Reads (Top-left)
axes[0, 0].bar(x - bar_width/2, tool1_dataset1_true_reads, width=bar_width, label="splitcode", 
               color=tool_colors["splitcode"])
axes[0, 0].bar(x + bar_width/2, tool2_dataset1_true_reads, width=bar_width, label="SCDemultiplexing Pipeline", 
               color=tool_colors["SCDemultiplexing Pipeline"])
axes[0, 0].set_xlabel("Number of Mismatches")
axes[0, 0].set_ylabel("True Reads")
axes[0, 0].set_title("Dataset 1: Artificial Subs - True Reads")
axes[0, 0].set_xticks(x)
axes[0, 0].set_xticklabels(mismatches)
axes[0, 0].set_ylim(0, 1_000_000)  # Set y-axis limit to 1 million
axes[0, 0].legend(loc="upper left")
axes[0, 0].grid(True, linestyle="--", alpha=0.6)
axes[0, 0].ticklabel_format(axis='y', style='plain')  # Disable scientific notation

# Plot for Dataset 2 - True Reads (Top-right)
axes[0, 1].bar(x - bar_width/2, tool1_dataset2_true_reads, width=bar_width, label="splitcode", 
               color=tool_colors["splitcode"])
axes[0, 1].bar(x + bar_width/2, tool2_dataset2_true_reads, width=bar_width, label="SCDemultiplexing Pipeline", 
               color=tool_colors["SCDemultiplexing Pipeline"])
axes[0, 1].set_xlabel("Number of Mismatches")
axes[0, 1].set_ylabel("True Reads")
axes[0, 1].set_title("Dataset 2: Artificial Subs+Indels - True Reads")
axes[0, 1].set_xticks(x)
axes[0, 1].set_xticklabels(mismatches)
axes[0, 1].set_ylim(0, 1_000_000) # Set y-axis limit to 1 million
axes[0, 1].legend(loc="upper left")
axes[0, 1].grid(True, linestyle="--", alpha=0.6)
axes[0, 1].ticklabel_format(axis='y', style='plain')  # Disable scientific notation

# Plot for Dataset 1 - False Reads (Bottom-left)
axes[1, 0].bar(x - bar_width/2, tool1_dataset1_false_reads, width=bar_width, label="splitcode", 
               color=tool_colors["splitcode"])
axes[1, 0].bar(x + bar_width/2, tool2_dataset1_false_reads, width=bar_width, label="SCDemultiplexing Pipeline", 
               color=tool_colors["SCDemultiplexing Pipeline"])
axes[1, 0].set_xlabel("Number of Mismatches")
axes[1, 0].set_ylabel("False Reads")
axes[1, 0].set_title("Dataset 1: Artificial Subs - False Reads")
axes[1, 0].set_xticks(x)
axes[1, 0].set_xticklabels(mismatches)
axes[1, 0].set_ylim(0, 40_000)  # Set y-axis limit to 40,000
axes[1, 0].legend(loc="upper left")
axes[1, 0].grid(True, linestyle="--", alpha=0.6)
axes[1, 0].ticklabel_format(axis='y', style='plain')  # Disable scientific notation

# Plot for Dataset 2 - False Reads (Bottom-right)
axes[1, 1].bar(x - bar_width/2, tool1_dataset2_false_reads, width=bar_width, label="splitcode", 
               color=tool_colors["splitcode"])
axes[1, 1].bar(x + bar_width/2, tool2_dataset2_false_reads, width=bar_width, label="SCDemultiplexing Pipeline", 
               color=tool_colors["SCDemultiplexing Pipeline"])
axes[1, 1].set_xlabel("Number of Mismatches")
axes[1, 1].set_ylabel("False Reads")
axes[1, 1].set_title("Dataset 2: Artificial Subs+Indels - False Reads")
axes[1, 1].set_xticks(x)
axes[1, 1].set_xticklabels(mismatches)
axes[1, 1].set_ylim(0, 40_000) # Set y-axis limit to 40,000
axes[1, 1].legend(loc="upper left")
axes[1, 1].grid(True, linestyle="--", alpha=0.6)
axes[1, 1].ticklabel_format(axis='y', style='plain')  # Disable scientific notation

# Add panel labels (A, B, C, D)
for i, ax in enumerate(axes.flatten()):
    ax.text(-0.1, 1.1, chr(65 + i), transform=ax.transAxes, fontsize=16, fontweight='bold', va='top')

# Adjust layout
plt.tight_layout()

# Save the figure
output_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/plots/true_false_reads_comparison_subplots.png"
plt.savefig(output_path, dpi=300, bbox_inches="tight")

# Show the plot
plt.show()