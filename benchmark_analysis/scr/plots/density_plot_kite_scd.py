# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt


# # Load the input files for kite and SCDemultiplexing
# kite_file_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/kite_vs_scd_processing/cells_x_features_with_indices_and_ab.mtx"
# scd_file_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/SCDemultiplex_results/processing/new/ABABCOUNT.txt"

# # Read kite data and SCD data (assuming similar structure for both)
# kite_df = pd.read_csv(kite_file_path, sep="\t")
# scd_df = pd.read_csv(scd_file_path, sep="\t")

# # Get the number of unique single cells for each tool
# kite_cells = kite_df["SingleCell_BARCODE"].nunique()
# scd_cells = scd_df["SingleCell_BARCODE"].nunique()


# # Create the figure with subplots
# fig, axes = plt.subplots(2, 2, figsize=(18, 18))

# ### 1. Top-left: Barplot of the number of single cells for each tool
# axes[0, 0].bar(["kite", "SCDemultiplexing"], [kite_cells, scd_cells], color=["lightgreen", "orange"])
# axes[0, 0].set_title("Number of Single Cells Retrieved")
# axes[0, 0].set_ylabel("Number of Cells")
# axes[0, 0].set_ylim(0, max(kite_cells, scd_cells) + 2000)
# axes[0, 0].text(-0.1, 1.05, "A", fontsize=16, fontweight="bold", transform=axes[0, 0].transAxes)

# ### 2. Top-right: Density Plot of counts for each tool
# # Get the counts for kite and SCDemultiplexing
# kite_counts = kite_df["AB_COUNT"].values
# scd_counts = scd_df["AB_COUNT"].values

# sns.kdeplot(kite_counts, ax=axes[0, 1], color="lightgreen", label="kite", fill=True)
# sns.kdeplot(scd_counts, ax=axes[0, 1], color="orange", label="SCDemultiplexing", fill=True)
# axes[0, 1].set_title("Density of Counts")
# axes[0, 1].set_xlabel("Counts per Cell")
# axes[0, 1].set_ylabel("Density")
# axes[0, 1].legend()
# axes[0, 1].text(-0.1, 1.05, "B", fontsize=16, fontweight="bold", transform=axes[0, 1].transAxes)

# ### 3. Bottom-left: Heatmap for kite (AB_COUNT > 1)
# # Filter kite data for AB_COUNT > 1
# kite_filtered = kite_df[kite_df["AB_COUNT"] > 2]
# kite_grouped = kite_filtered.groupby(["SingleCell_BARCODE", "AB_BARCODE"])["AB_COUNT"].sum().reset_index()
# kite_heatmap_data = kite_grouped.pivot(index="SingleCell_BARCODE", columns="AB_BARCODE", values="AB_COUNT").fillna(0)

# # Reduce size (sample 300 rows for visualization)
# kite_sample = kite_heatmap_data.sample(n=min(200, len(kite_heatmap_data)), random_state=42)

# sns.heatmap(kite_sample, ax=axes[1, 0], cmap="Reds", linewidths=0.01, linecolor="gray", robust=True)
# axes[1, 0].set_title("Heatmap of Antibody Counts per Single Cell(kite)")
# axes[1, 0].set_xlabel("Antibodies")
# axes[1, 0].set_ylabel("Single Cells (Sampled=200)")
# axes[1, 0].text(-0.1, 1.05, "C", fontsize=16, fontweight="bold", transform=axes[1, 0].transAxes)

# ### 4. Bottom-right: Heatmap for SCDemultiplexing (AB_COUNT > 1)
# # Filter SCDemultiplexing data for AB_COUNT > 2
# scd_filtered = scd_df[scd_df["AB_COUNT"] > 2]
# scd_grouped = scd_filtered.groupby(["SingleCell_BARCODE", "AB_BARCODE"])["AB_COUNT"].sum().reset_index()
# scd_heatmap_data = scd_grouped.pivot(index="SingleCell_BARCODE", columns="AB_BARCODE", values="AB_COUNT").fillna(0)

# # Reduce size (sample 500 rows for visualization)
# scd_sample = scd_heatmap_data.sample(n=min(200, len(scd_heatmap_data)), random_state=42)

# sns.heatmap(scd_sample, ax=axes[1, 1], cmap="Reds", linewidths=0.01, linecolor="gray", robust=True)
# axes[1, 1].set_title("Heatmap of Antibody Counts per Single Cell(SCDemultiplexing)")
# axes[1, 1].set_xlabel("Antibodies")
# axes[1, 1].set_ylabel("Single Cells (Sampled=200)")
# axes[1, 1].text(-0.1, 1.05, "D", fontsize=16, fontweight="bold", transform=axes[1, 1].transAxes)

# # Adjust layout
# plt.tight_layout()

# # Save the figure
# output_fig_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/kite_vs_scd_processing/combined_plot_with_panels.png"
# plt.savefig(output_fig_path, dpi=300, bbox_inches="tight")

# # Show the figure
# plt.show()

# # Print output file path
# print(f"Figure saved to: {output_fig_path}")






# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Load the input files for kite and SCDemultiplexing
# kite_file_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/kite_vs_scd_processing/cells_x_features_with_indices_and_ab.mtx"
# scd_file_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/SCDemultiplex_results/processing/new/ABABCOUNT.txt"

# # Read kite data and SCD data
# kite_df = pd.read_csv(kite_file_path, sep="\t")
# scd_df = pd.read_csv(scd_file_path, sep="\t")

# kite_cells_total = kite_df["SingleCell_BARCODE"].nunique()
# scd_cells_total = scd_df["SingleCell_BARCODE"].nunique()


# # Find common single-cell barcodes in both datasets
# common_cells = set(kite_df["SingleCell_BARCODE"]).intersection(set(scd_df["SingleCell_BARCODE"]))

# # Filter both datasets to keep only common single cells
# kite_filtered = kite_df[kite_df["SingleCell_BARCODE"].isin(common_cells)]
# scd_filtered = scd_df[scd_df["SingleCell_BARCODE"].isin(common_cells)]

# # Get the number of unique single cells in each tool
# kite_cells_1 = kite_filtered[kite_filtered["AB_COUNT"] > 1]
# scd_cells_1 = scd_filtered[scd_filtered["AB_COUNT"] > 1]


# # Create the figure with subplots
# fig, axes = plt.subplots(2, 2, figsize=(18, 18))

# ### 1. Top-left: Barplot of the number of single cells for each tool
# axes[0, 0].bar(["kite", "SCDemultiplexing"], [kite_cells_total, scd_cells_total], color=["lightgreen", "orange"])
# axes[0, 0].set_title("Number of Single Cells Retrieved")
# axes[0, 0].set_ylabel("Number of Cells")
# axes[0, 0].set_ylim(0, max(kite_cells_total, scd_cells_total) + 2000)
# axes[0, 0].text(-0.1, 1.05, "A", fontsize=16, fontweight="bold", transform=axes[0, 0].transAxes)

# ### 2. Top-right: Density Plot of counts for each tool
# # Get the counts for kite and SCDemultiplexing
# kite_counts = kite_df["AB_COUNT"].values
# scd_counts = scd_df["AB_COUNT"].values

# # sns.kdeplot(kite_counts, ax=axes[0, 1], color="lightgreen", label="kite", fill=True)
# # sns.kdeplot(scd_counts, ax=axes[0, 1], color="orange", label="SCDemultiplexing", fill=True)
# sns.violinplot(x=["kite"] * len(kite_counts), y=kite_counts, ax=axes[0, 1], color="lightgreen", label="kite")
# sns.violinplot(x=["SCDemultiplexing"] * len(scd_counts), y=scd_counts, ax=axes[0, 1], color="orange", label="SCDemultiplexing")
# # sns.boxplot(x=["kite"] * len(kite_counts), y=kite_counts, ax=axes[0, 1], color="lightgreen", label="kite")
# # sns.boxplot(x=["SCDemultiplexing"] * len(scd_counts), y=scd_counts, ax=axes[0, 1], color="orange", label="SCDemultiplexing")
# axes[0, 1].set_title("Violin plot of Protein Counts per Cell")
# axes[0, 1].set_xlabel("Tool")
# axes[0, 1].set_ylabel("Protein Count Per Cell")
# axes[0, 1].legend()
# axes[0, 1].text(-0.1, 1.05, "B", fontsize=16, fontweight="bold", transform=axes[0, 1].transAxes)

# ### 3. Bottom-left: Heatmap for kite (AB_COUNT > 1)
# # Group and pivot for heatmaps
# kite_grouped = kite_filtered.groupby(["SingleCell_BARCODE", "AB_BARCODE"])["AB_COUNT"].sum().reset_index()
# scd_grouped = scd_filtered.groupby(["SingleCell_BARCODE", "AB_BARCODE"])["AB_COUNT"].sum().reset_index()

# kite_heatmap_data = kite_grouped.pivot(index="SingleCell_BARCODE", columns="AB_BARCODE", values="AB_COUNT").fillna(0)
# scd_heatmap_data = scd_grouped.pivot(index="SingleCell_BARCODE", columns="AB_BARCODE", values="AB_COUNT").fillna(0)

# # Ensure same cell order in both heatmaps
# common_cells_list = list(common_cells)  # Convert set to list
# kite_heatmap_data = kite_heatmap_data.loc[common_cells_list]
# scd_heatmap_data = scd_heatmap_data.loc[common_cells_list]

# # Sample 200 cells for visualization
# kite_sample = kite_heatmap_data.sample(n=min(500, len(kite_heatmap_data)), random_state=42)
# scd_sample = scd_heatmap_data.sample(n=min(500, len(scd_heatmap_data)), random_state=42)

# sns.heatmap(kite_sample, ax=axes[1, 0], cmap="Reds", linewidths=0.01, linecolor="gray", robust=True)
# axes[1, 0].set_title("Heatmap of Antibody Counts per Single Cell (kite)")
# axes[1, 0].set_xlabel("Antibodies")
# axes[1, 0].set_ylabel("Single Cells (Matched Sampled=200)")
# axes[1, 0].text(-0.1, 1.05, "C", fontsize=16, fontweight="bold", transform=axes[1, 0].transAxes)

# ### 4. Bottom-right: Heatmap for SCDemultiplexing (AB_COUNT > 1)
# sns.heatmap(scd_sample, ax=axes[1, 1], cmap="Reds", linewidths=0.01, linecolor="gray", robust=True)
# axes[1, 1].set_title("Heatmap of Antibody Counts per Single Cell (SCDemultiplexing)")
# axes[1, 1].set_xlabel("Antibodies")
# axes[1, 1].set_ylabel("Single Cells (Matched Sampled=200)")
# axes[1, 1].text(-0.1, 1.05, "D", fontsize=16, fontweight="bold", transform=axes[1, 1].transAxes)

# # Adjust layout
# plt.tight_layout()

# # Save the figure
# output_fig_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/kite_vs_scd_processing/combined_plot_with_panels_matched_cells_violin.png"
# plt.savefig(output_fig_path, dpi=300, bbox_inches="tight")

# # Show the figure
# plt.show()

# # Print output file path
# print(f"Figure saved to: {output_fig_path}")





import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the input files for kite and SCDemultiplexing
kite_file_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/kite_vs_scd_processing/cells_x_features_with_indices_and_ab.mtx"
scd_file_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/SCDemultiplex_results/processing/new/ABABCOUNT.txt"

# Read kite data and SCD data
kite_df = pd.read_csv(kite_file_path, sep="\t")
scd_df = pd.read_csv(scd_file_path, sep="\t")

kite_cells_total = kite_df["SingleCell_BARCODE"].nunique()
scd_cells_total = scd_df["SingleCell_BARCODE"].nunique()

# Find common single-cell barcodes in both datasets
common_cells = set(kite_df["SingleCell_BARCODE"]).intersection(set(scd_df["SingleCell_BARCODE"]))

# Filter both datasets to keep only common single cells
kite_filtered = kite_df[kite_df["SingleCell_BARCODE"].isin(common_cells)]
scd_filtered = scd_df[scd_df["SingleCell_BARCODE"].isin(common_cells)]

# Get the number of unique single cells in each tool
kite_cells_1 = kite_filtered[kite_filtered["AB_COUNT"] > 1]
scd_cells_1 = scd_filtered[scd_filtered["AB_COUNT"] > 1]

# Create the figure with subplots
fig, axes = plt.subplots(2, 2, figsize=(18, 18))

### 1. Top-left: Barplot of the number of single cells for each tool
axes[0, 0].bar(["kite", "SCDemultiplexing"], [kite_cells_total, scd_cells_total], color=["lightgreen", "orange"])
axes[0, 0].set_title("Number of Single Cells Retrieved")
axes[0, 0].set_ylabel("Number of Cells")
axes[0, 0].set_ylim(0, max(kite_cells_total, scd_cells_total) + 2000)
axes[0, 0].text(-0.1, 1.05, "A", fontsize=16, fontweight="bold", transform=axes[0, 0].transAxes)

### 2. Top-right: Density Plot of counts for each tool
# Get the counts for kite and SCDemultiplexing
kite_counts = kite_df["AB_COUNT"].values
scd_counts = scd_df["AB_COUNT"].values

# Create density plots with log-scaled y-axis
sns.kdeplot(kite_counts, ax=axes[0, 1], color="lightgreen", label="kite", fill=True, log_scale=True)
sns.kdeplot(scd_counts, ax=axes[0, 1], color="orange", label="SCDemultiplexing", fill=True, log_scale=True)

# Customize the plot
axes[0, 1].set_title("Density Plot of Protein Counts per Cell (Log Scale)")
axes[0, 1].set_xlabel("Protein Count Per Cell")
axes[0, 1].set_ylabel("Density")
axes[0, 1].legend()
axes[0, 1].text(-0.1, 1.05, "B", fontsize=16, fontweight="bold", transform=axes[0, 1].transAxes)

### 3. Bottom-left: Heatmap for kite (AB_COUNT > 1)
# Group and pivot for heatmaps
kite_grouped = kite_filtered.groupby(["SingleCell_BARCODE", "AB_BARCODE"])["AB_COUNT"].sum().reset_index()
scd_grouped = scd_filtered.groupby(["SingleCell_BARCODE", "AB_BARCODE"])["AB_COUNT"].sum().reset_index()

kite_heatmap_data = kite_grouped.pivot(index="SingleCell_BARCODE", columns="AB_BARCODE", values="AB_COUNT").fillna(0)
scd_heatmap_data = scd_grouped.pivot(index="SingleCell_BARCODE", columns="AB_BARCODE", values="AB_COUNT").fillna(0)

# Ensure same cell order in both heatmaps
common_cells_list = list(common_cells)  # Convert set to list
kite_heatmap_data = kite_heatmap_data.loc[common_cells_list]
scd_heatmap_data = scd_heatmap_data.loc[common_cells_list]

# Sample 200 cells for visualization
kite_sample = kite_heatmap_data.sample(n=min(500, len(kite_heatmap_data)), random_state=42)
scd_sample = scd_heatmap_data.sample(n=min(500, len(scd_heatmap_data)), random_state=42)

sns.heatmap(kite_sample, ax=axes[1, 0], cmap="Reds", linewidths=0.001, linecolor="gray", robust=True)
axes[1, 0].set_title("Heatmap of Antibody Counts per Single Cell (kite)")
axes[1, 0].set_xlabel("Antibodies")
axes[1, 0].set_ylabel("Single Cells (Matched Sampled=200)")
axes[1, 0].text(-0.1, 1.05, "C", fontsize=16, fontweight="bold", transform=axes[1, 0].transAxes)

### 4. Bottom-right: Heatmap for SCDemultiplexing (AB_COUNT > 1)
sns.heatmap(scd_sample, ax=axes[1, 1], cmap="Reds", linewidths=0.001, linecolor="gray", robust=True)
axes[1, 1].set_title("Heatmap of Antibody Counts per Single Cell (SCDemultiplexing)")
axes[1, 1].set_xlabel("Antibodies")
axes[1, 1].set_ylabel("Single Cells (Matched Sampled=200)")
axes[1, 1].text(-0.1, 1.05, "D", fontsize=16, fontweight="bold", transform=axes[1, 1].transAxes)

# Adjust layout
plt.tight_layout()

# Save the figure
output_fig_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/kite_vs_scd_processing/combined_plot_with_panels_matched_cells_density.png"
plt.savefig(output_fig_path, dpi=300, bbox_inches="tight")

# Show the figure
plt.show()

# Print output file path
print(f"Figure saved to: {output_fig_path}")




