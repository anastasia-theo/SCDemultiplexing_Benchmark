# import matplotlib
# import matplotlib.pyplot as plt
# import matplotlib_venn
# from matplotlib_venn import venn2


# # Data for Dataset 4
# dataset4_mismatches = [1, 2, 3, 4, 5]
# dataset4_scd_reads = [74930150, 76130776, 76165868, 76177739, 76174061]
# dataset4_split_reads = [58856859, 64143192, 58259928, 0, 0]
# dataset4_common_reads = [36546788, 13106844, 12402355, 0, 0]

# # Data for Dataset 3
# dataset3_mismatches = [1, 2, 3, 4, 5]
# dataset3_scd_reads = [9047318, 9639482, 9738669, 9837693, 9872678]
# dataset3_split_reads = [7632274, 7974183, 7933081, 0, 0]
# dataset3_common_reads = [7579021, 1936141, 643646, 0, 0]

# # Create a 3x2 grid of subplots
# fig, axes = plt.subplots(3, 2, figsize=(12, 18))

# # Function to create a Venn diagram for a given dataset and mismatch level
# def create_venn_diagram(ax, scd_reads, split_reads, common_reads, title):
#     # Calculate unique reads for SCD and Split
#     scd_unique = scd_reads - common_reads
#     split_unique = split_reads - common_reads
    
#     # Create the Venn diagram
#     venn = venn2(subsets=(scd_unique, split_unique, common_reads), set_labels=('SCD', 'Split'), ax=ax)
    
#     # Customize colors
#     for patch in venn.patches:
#         patch.set_alpha(0.6)  # Adjust transparency if needed
#     venn.get_patch_by_id('10').set_color('orange')  # SCD unique
#     venn.get_patch_by_id('01').set_color('skyblue')   # Split unique
#     venn.get_patch_by_id('11').set_color('purple')   # Overlap (optional: you can choose a different color)
    

#         # Increase the font size of the numbers in the Venn diagram
#     for text in venn.set_labels:
#         if text is not None:
#             text.set_fontsize(16)  # Adjust the font size as needed
#     for text in venn.subset_labels:
#         if text is not None:
#             text.set_fontsize(14)  # Adjust the font size as needed

#     # Set the title
#     ax.set_title(title, fontsize=16)

# # Plot for Dataset 3 - Mismatch 1 (Row 1, Column 1)
# create_venn_diagram(axes[0, 0], dataset3_scd_reads[0], dataset3_split_reads[0], dataset3_common_reads[0], 
#                    "SIGNAL_seq - 1 Mismatch ")

# # Plot for Dataset 3 - Mismatch 2 (Row 2, Column 1)
# create_venn_diagram(axes[1, 0], dataset3_scd_reads[1], dataset3_split_reads[1], dataset3_common_reads[1], 
#                    "SIGNAL_seq - 2 Mismatches")

# # Plot for Dataset 3 - Mismatch 3 (Row 3, Column 1)
# create_venn_diagram(axes[2, 0], dataset3_scd_reads[2], dataset3_split_reads[2], dataset3_common_reads[2], 
#                    "SIGNAL_seq - 3 Mismatches")

# # Plot for Dataset 4 - Mismatch 1 (Row 1, Column 2)
# create_venn_diagram(axes[0, 1], dataset4_scd_reads[0], dataset4_split_reads[0], dataset4_common_reads[0], 
#                    "NKI - 1 Mismatch")

# # Plot for Dataset 4 - Mismatch 2 (Row 2, Column 2)
# create_venn_diagram(axes[1, 1], dataset4_scd_reads[1], dataset4_split_reads[1], dataset4_common_reads[1], 
#                    "NKI - 2 Mismatches")

# # Plot for Dataset 4 - Mismatch 3 (Row 3, Column 2)
# create_venn_diagram(axes[2, 1], dataset4_scd_reads[2], dataset4_split_reads[2], dataset4_common_reads[2], 
#                    "NKI - 3 Mismatches")

# # Add panel labels (A, B, C, D, E, F)
# panel_labels = ['A', 'B', 'C', 'D', 'E', 'F']
# for i, ax in enumerate(axes.flatten()):
#     ax.text(-0.1, 1.1, panel_labels[i], transform=ax.transAxes, fontsize=16, fontweight='bold', va='top')

# # Adjust layout
# plt.tight_layout()

# # Save the figure
# output_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/plots/venn_diagrams_3x2.png"
# plt.savefig(output_path, dpi=300, bbox_inches="tight")

# # Show the plot
# plt.show()

# # /scistor/informatica/ath100/miniconda3/bin/python /scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/scr/plots_real.py




# import matplotlib.pyplot as plt
# import numpy as np

# # Data for Dataset 3 (SIGNAL_seq)
# dataset3_mismatches = [1, 2, 3]  # Only first 3 mismatch levels
# dataset3_scd_reads = [9047318, 9639482, 9738669]
# dataset3_split_reads = [7632274, 7974183, 7933081]
# dataset3_common_reads = [7579021, 1936141, 643646]

# # Data for Dataset 4 (NKI)
# dataset4_mismatches = [1, 2, 3]  # Only first 3 mismatch levels
# dataset4_scd_reads = [74930150, 76130776, 76165868]
# dataset4_split_reads = [58856859, 64143192, 58259928]
# dataset4_common_reads = [36546788, 13106844, 12402355]

# # Create a 1x2 grid of subplots (one plot per dataset)
# fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# # Increase font size for all text
# plt.rcParams.update({'font.size': 12})

# # Function to create a line chart for a given dataset
# def create_line_chart(ax, mismatches, scd_reads, split_reads, common_reads, dataset_name):
#     # Plot SCD reads
#     ax.plot(mismatches, scd_reads, label='SCD Reads', color='orange', marker='o', linestyle='-', linewidth=2)
#     # Plot Split reads
#     ax.plot(mismatches, split_reads, label='Split Reads', color='skyblue', marker='s', linestyle='--', linewidth=2)
#     # Plot Common reads
#     ax.plot(mismatches, common_reads, label='Common Reads', color='purple', marker='^', linestyle='-.', linewidth=2)
    
#     # Customize the plot
#     ax.set_xlabel("Number of Mismatches", fontsize=12)
#     ax.set_ylabel("Number of Reads", fontsize=12)
#     ax.set_title(f"{dataset_name} - Reads by Mismatch Level", fontsize=14)
#     ax.grid(True, linestyle='--', alpha=0.6)
#     ax.legend(loc='upper right', fontsize=10)
#     ax.set_xticks(mismatches)
#     ax.set_xticklabels([str(m) for m in mismatches], fontsize=10)

# # Plot for Dataset 3 (SIGNAL_seq)
# create_line_chart(axes[0], dataset3_mismatches, dataset3_scd_reads, dataset3_split_reads, dataset3_common_reads, "SIGNAL_seq")

# # Plot for Dataset 4 (NKI)
# create_line_chart(axes[1], dataset4_mismatches, dataset4_scd_reads, dataset4_split_reads, dataset4_common_reads, "NKI")

# # Add panel labels (A, B)
# panel_labels = ['A', 'B']
# for i, ax in enumerate(axes):
#     ax.text(-0.1, 1.1, panel_labels[i], transform=ax.transAxes, fontsize=16, fontweight='bold', va='top')

# # Adjust layout
# plt.tight_layout()

# # Save the figure
# output_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/plots/real_datasets.png"
# plt.savefig(output_path, dpi=300, bbox_inches="tight")

# # Show the plot
# plt.show()


import matplotlib.pyplot as plt
import matplotlib_venn
from matplotlib_venn import venn2
import numpy as np

# Data for Dataset 4 (NKI)
dataset4_mismatches = [1, 2, 3, 4, 5]
dataset4_scd_reads = [74930150, 76130776, 76165868, 76177739, 76174061]
dataset4_split_reads = [58856859, 64143192, 58259928, 0, 0]
dataset4_common_reads = [36546788, 13106844, 12402355, 0, 0]

# Data for Dataset 3 (SIGNAL_seq)
dataset3_mismatches = [1, 2, 3, 4, 5]
dataset3_scd_reads = [9047318, 9639482, 9738669, 9837693, 9872678]
dataset3_split_reads = [7632274, 7974183, 7933081, 0, 0]
dataset3_common_reads = [7579021, 1936141, 643646, 0, 0]

# Create a 2x2 grid of subplots (top row for Venn diagrams, bottom row for line charts)
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# Function to create a Venn diagram for a given dataset and mismatch level
def create_venn_diagram(ax, scd_reads, split_reads, common_reads, title):
    # Calculate unique reads for SCD and Split
    scd_unique = scd_reads - common_reads
    split_unique = split_reads - common_reads
    
    # Create the Venn diagram
    venn = venn2(subsets=(scd_unique, split_unique, common_reads), set_labels=('SCD', 'Split'), ax=ax)
    
    # Customize colors
    for patch in venn.patches:
        patch.set_alpha(0.6)  # Adjust transparency if needed
    venn.get_patch_by_id('10').set_color('orange')  # SCD unique
    venn.get_patch_by_id('01').set_color('skyblue')   # Split unique
    venn.get_patch_by_id('11').set_color('purple')   # Overlap (optional: you can choose a different color)
    
    # Increase the font size of the numbers in the Venn diagram
    for text in venn.set_labels:
        if text is not None:
            text.set_fontsize(16)  # Adjust the font size as needed
    for text in venn.subset_labels:
        if text is not None:
            text.set_fontsize(14)  # Adjust the font size as needed

    # Set the title
    ax.set_title(title, fontsize=16)

# Plot for Dataset 3 - Mismatch 1 (Panel A)
create_venn_diagram(axes[0, 0], dataset3_scd_reads[0], dataset3_split_reads[0], dataset3_common_reads[0], 
                   "SIGNAL_seq - 1 Mismatch")

# Plot for Dataset 4 - Mismatch 1 (Panel B)
create_venn_diagram(axes[0, 1], dataset4_scd_reads[0], dataset4_split_reads[0], dataset4_common_reads[0], 
                   "NKI - 1 Mismatch")

# Function to create a line chart for a given dataset
def create_line_chart(ax, mismatches, scd_reads, split_reads, common_reads, dataset_name):
    # Plot SCD reads
    ax.plot(mismatches, scd_reads, label='SCD Reads', color='orange', marker='o', linestyle='-', linewidth=2)
    # Plot Split reads
    ax.plot(mismatches, split_reads, label='Split Reads', color='skyblue', marker='s', linestyle='--', linewidth=2)
    # Plot Common reads
    ax.plot(mismatches, common_reads, label='Common Reads', color='purple', marker='^', linestyle='-.', linewidth=2)
    
    # Customize the plot
    ax.set_xlabel("Number of Mismatches", fontsize=12)
    ax.set_ylabel("Number of Reads", fontsize=12)
    ax.set_title(f"{dataset_name} - Reads by Mismatch Level", fontsize=14)
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend(loc='upper right', fontsize=10)
    ax.set_xticks(mismatches)
    ax.set_xticklabels([str(m) for m in mismatches], fontsize=10)

# Plot for Dataset 3 (SIGNAL_seq) Line Chart (Panel C)
create_line_chart(axes[1, 0], dataset3_mismatches, dataset3_scd_reads, dataset3_split_reads, dataset3_common_reads, "SIGNAL_seq")

# Plot for Dataset 4 (NKI) Line Chart (Panel D)
create_line_chart(axes[1, 1], dataset4_mismatches, dataset4_scd_reads, dataset4_split_reads, dataset4_common_reads, "NKI")

# Add panel labels (A, B, C, D)
panel_labels = ['A', 'B', 'C', 'D']
for i, ax in enumerate(axes.flatten()):
    ax.text(-0.1, 1.1, panel_labels[i], transform=ax.transAxes, fontsize=16, fontweight='bold', va='top')

# Adjust layout
plt.tight_layout()

# Save the figure
output_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/plots/combined_venn_line_plots_updated.png"
plt.savefig(output_path, dpi=300, bbox_inches="tight")

# Show the plot
plt.show()




# VENN FOR INTERSECTION OF SCD AND SPLIT READS

# import matplotlib.pyplot as plt
# from matplotlib_venn import venn2

# # Define the values for SCD Reads Venn diagram
# scd_1_mismatch = 9047318
# scd_3_mismatch = 9738669
# scd_common = 9047318  # Common reads between 1 and 3 mismatches

# # Define the values for Split Reads Venn diagram
# split_1_mismatch = 7632274
# split_3_mismatch = 7933081
# split_common = 584746  # Common reads between 1 and 3 mismatches

# # Create a figure with two subplots for the Venn diagrams
# fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# # Function to create Venn diagram
# def create_venn(ax, set1, set2, common, title, label1, label2):
#     unique_set1 = set1 - common
#     unique_set2 = set2 - common

#     venn = venn2(subsets=(unique_set1, unique_set2, common), set_labels=(label1, label2), ax=ax)

#     # Customize colors
#     venn.get_patch_by_id('10').set_color('orange')  # Unique to set 1
#     venn.get_patch_by_id('01').set_color('skyblue')  # Unique to set 2
#     venn.get_patch_by_id('11').set_color('purple')  # Overlapping area
    
#     # Increase the font size of the numbers in the Venn diagram
#     for text in venn.set_labels:
#         if text is not None:
#             text.set_fontsize(14)  # Adjust font size for labels
#     for text in venn.subset_labels:
#         if text is not None:
#             text.set_fontsize(12)  # Adjust font size for numbers

#     ax.set_title(title, fontsize=14)
#     ax.set_aspect('equal')  # Keep the circles proportional
#     ax.set_xticks([])  # Remove axis ticks
#     ax.set_yticks([])

# # Create Venn diagram for SCD Reads
# create_venn(axes[0], scd_1_mismatch, scd_3_mismatch, scd_common, "SCD Reads (1 vs 3 Mismatches)", "1 Mismatch", "3 Mismatches")

# # Create Venn diagram for Split Reads
# create_venn(axes[1], split_1_mismatch, split_3_mismatch, split_common, "Split Reads (1 vs 3 Mismatches)", "1 Mismatch", "3 Mismatches")


# # Add panel labels (A, B)
# panel_labels = ['A', 'B']
# for i, ax in enumerate(axes):
#     ax.text(-0.1, 1.1, panel_labels[i], transform=ax.transAxes, fontsize=16, fontweight='bold', va='top')


# # Adjust layout
# plt.tight_layout()

# # Save the figure
# output_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/plots/scd_split_venn.png"
# plt.savefig(output_path, dpi=300, bbox_inches="tight")

# # Show the plot
# plt.show()
