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

# # Group and pivot for heatmaps
# kite_grouped = kite_filtered.groupby(["SingleCell_BARCODE", "AB_BARCODE"])["AB_COUNT"].sum().reset_index()
# scd_grouped = scd_filtered.groupby(["SingleCell_BARCODE", "AB_BARCODE"])["AB_COUNT"].sum().reset_index()

# kite_heatmap = kite_grouped.pivot(index="AB_BARCODE", columns="SingleCell_BARCODE", values="AB_COUNT").fillna(0)
# scd_heatmap = scd_grouped.pivot(index="AB_BARCODE", columns="SingleCell_BARCODE", values="AB_COUNT").fillna(0)

# # Sort antibodies by total abundance (high to low)
# kite_heatmap = kite_heatmap.loc[kite_heatmap.sum(axis=1).sort_values(ascending=False).index]
# scd_heatmap = scd_heatmap.loc[scd_heatmap.sum(axis=1).sort_values(ascending=False).index]

# # Select high-abundance single cells
# kite_cell_sums = kite_heatmap.sum(axis=0)  # Sum across antibodies per cell
# scd_cell_sums = scd_heatmap.sum(axis=0)

# kite_sorted_cells = kite_cell_sums.sort_values(ascending=False).index
# scd_sorted_cells = scd_cell_sums.sort_values(ascending=False).index

# top_kite_cells = kite_sorted_cells[:100]  # Select top 300 most abundant cells
# top_scd_cells = scd_sorted_cells[:100]

# kite_sample = kite_heatmap[top_kite_cells]  # Subset heatmap for high-abundance cells
# scd_sample = scd_heatmap[top_scd_cells]

# # Sort antibodies by total abundance (high to low) and select top 10
# kite_top_antibodies = kite_heatmap.sum(axis=1).sort_values(ascending=False).head(10).index
# scd_top_antibodies = scd_heatmap.sum(axis=1).sort_values(ascending=False).head(10).index

# # Subset the heatmaps to include only the top 10 antibodies
# kite_sample_top10 = kite_sample.loc[kite_top_antibodies]
# scd_sample_top10 = scd_sample.loc[scd_top_antibodies]

# # Create the figure with subplots
# fig, axes = plt.subplots(2, 2, figsize=(18, 16))

# ### 1. Panel A: Bar plot of single cells
# axes[0, 0].bar(["KITE", "SCD"], [kite_cells_total, scd_cells_total], color=["lightgreen", "orange"])
# axes[0, 0].set_title("Number of Single Cells Retrieved")
# axes[0, 0].set_ylabel("Number of Cells")
# axes[0, 0].text(-0.1, 1.05, "A", fontsize=16, fontweight="bold", transform=axes[0, 0].transAxes)

# ### 2. Panel B: Density Plot of AB_COUNT
# kite_counts = kite_df["AB_COUNT"].values
# scd_counts = scd_df["AB_COUNT"].values

# sns.kdeplot(kite_counts, ax=axes[0, 1], color="lightgreen", label="KITE", fill=True, log_scale=True)
# sns.kdeplot(scd_counts, ax=axes[0, 1], color="orange", label="SCDemultiplexing", fill=True, log_scale=True)

# axes[0, 1].set_title("Density Plot of Protein Counts per Cell (Log Scale)")
# axes[0, 1].set_xlabel("Protein Count Per Cell")
# axes[0, 1].set_ylabel("Density")
# axes[0, 1].legend()
# axes[0, 1].text(-0.1, 1.05, "B", fontsize=16, fontweight="bold", transform=axes[0, 1].transAxes)

# ### 3. Panel C: Heatmap for KITE (high-abundance cells and top 10 antibodies)
# sns.heatmap(kite_sample_top10, ax=axes[1, 0], cmap="Reds", linewidths=0.01, linecolor="gray", robust=True)
# axes[1, 0].set_title("Top 10 Antibody Counts per Single Cell (KITE)")
# axes[1, 0].set_xlabel("Single Cells (Top 500 by Abundance)")
# axes[1, 0].set_ylabel("Antibodies (Top 10 by Abundance)")
# axes[1, 0].text(-0.1, 1.05, "C", fontsize=16, fontweight="bold", transform=axes[1, 0].transAxes)

# ### 4. Panel D: Heatmap for SCDemultiplexing (high-abundance cells and top 10 antibodies)
# sns.heatmap(scd_sample_top10, ax=axes[1, 1], cmap="Reds", linewidths=0.01, linecolor="gray", robust=True)
# axes[1, 1].set_title("Top 10 Antibody Counts per Single Cell (SCDemultiplexing)")
# axes[1, 1].set_xlabel("Single Cells (Top 500 by Abundance)")
# axes[1, 1].set_ylabel("Antibodies (Top 10 by Abundance)")
# axes[1, 1].text(-0.1, 1.05, "D", fontsize=16, fontweight="bold", transform=axes[1, 1].transAxes)

# # Adjust layout
# plt.tight_layout()

# # Save the figure
# output_fig_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/kite_vs_scd_processing/combined_plot_with_panels_top300_top10ab.png"
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

# # Group and pivot for heatmaps
# kite_grouped = kite_filtered.groupby(["SingleCell_BARCODE", "AB_BARCODE"])["AB_COUNT"].sum().reset_index()
# scd_grouped = scd_filtered.groupby(["SingleCell_BARCODE", "AB_BARCODE"])["AB_COUNT"].sum().reset_index()

# kite_heatmap = kite_grouped.pivot(index="AB_BARCODE", columns="SingleCell_BARCODE", values="AB_COUNT").fillna(0)
# scd_heatmap = scd_grouped.pivot(index="AB_BARCODE", columns="SingleCell_BARCODE", values="AB_COUNT").fillna(0)

# # Sort antibodies by total abundance (high to low)
# kite_heatmap = kite_heatmap.loc[kite_heatmap.sum(axis=1).sort_values(ascending=False).index]
# scd_heatmap = scd_heatmap.loc[scd_heatmap.sum(axis=1).sort_values(ascending=False).index]

# # Select high-abundance single cells
# kite_cell_sums = kite_heatmap.sum(axis=0)  # Sum across antibodies per cell
# scd_cell_sums = scd_heatmap.sum(axis=0)

# kite_sorted_cells = kite_cell_sums.sort_values(ascending=False).index
# scd_sorted_cells = scd_cell_sums.sort_values(ascending=False).index

# top_kite_cells = kite_sorted_cells[:300]  # Select top 300 most abundant cells
# top_scd_cells = scd_sorted_cells[:300]

# kite_sample = kite_heatmap[top_kite_cells]  # Subset heatmap for high-abundance cells
# scd_sample = scd_heatmap[top_scd_cells]

# # Remove pS6 from the heatmaps
# kite_sample_no_pS6 = kite_sample.drop("pS6 [S240/S244] (2)", errors="ignore")
# scd_sample_no_pS6 = scd_sample.drop("pS6 [S240/S244] (2)", errors="ignore")

# # Sort antibodies by total abundance (high to low) and select top 10
# kite_top_antibodies = kite_sample_no_pS6.sum(axis=1).sort_values(ascending=False).head(10).index
# scd_top_antibodies = scd_sample_no_pS6.sum(axis=1).sort_values(ascending=False).head(10).index

# # Subset the heatmaps to include only the top 10 antibodies
# kite_sample_top10 = kite_sample_no_pS6.loc[kite_top_antibodies]
# scd_sample_top10 = scd_sample_no_pS6.loc[scd_top_antibodies]

# # Create the figure with subplots
# fig, axes = plt.subplots(2, 2, figsize=(18, 18))

# ### 1. Panel A: Bar plot of single cells
# axes[0, 0].bar(["KITE", "SCD"], [kite_cells_total, scd_cells_total], color=["lightgreen", "orange"])
# axes[0, 0].set_title("Number of Single Cells Retrieved")
# axes[0, 0].set_ylabel("Number of Cells")
# axes[0, 0].text(-0.1, 1.05, "A", fontsize=16, fontweight="bold", transform=axes[0, 0].transAxes)

# ### 2. Panel B: Density Plot of AB_COUNT
# kite_counts = kite_df["AB_COUNT"].values
# scd_counts = scd_df["AB_COUNT"].values

# sns.kdeplot(kite_counts, ax=axes[0, 1], color="lightgreen", label="KITE", fill=True, log_scale=True)
# sns.kdeplot(scd_counts, ax=axes[0, 1], color="orange", label="SCDemultiplexing", fill=True, log_scale=True)

# axes[0, 1].set_title("Density Plot of Protein Counts per Cell (Log Scale)")
# axes[0, 1].set_xlabel("Protein Count Per Cell")
# axes[0, 1].set_ylabel("Density")
# axes[0, 1].legend()
# axes[0, 1].text(-0.1, 1.05, "B", fontsize=16, fontweight="bold", transform=axes[0, 1].transAxes)

# ### 3. Panel C: Heatmap for KITE (high-abundance cells and top 10 antibodies, excluding pS6)
# sns.heatmap(kite_sample_top10, ax=axes[1, 0], cmap="Reds", linewidths=0.01, linecolor="gray", robust=True)
# axes[1, 0].set_title("Top 10 Antibody Counts per Single Cell (KITE, Excluding pS6)")
# axes[1, 0].set_xlabel("Single Cells (Top 300 by Abundance)")
# axes[1, 0].set_ylabel("Antibodies (Top 10 by Abundance)")
# axes[1, 0].text(-0.1, 1.05, "C", fontsize=16, fontweight="bold", transform=axes[1, 0].transAxes)

# ### 4. Panel D: Heatmap for SCDemultiplexing (high-abundance cells and top 10 antibodies, excluding pS6)
# sns.heatmap(scd_sample_top10, ax=axes[1, 1], cmap="Reds", linewidths=0.01, linecolor="gray", robust=True)
# axes[1, 1].set_title("Top 10 Antibody Counts per Single Cell (SCDemultiplexing, Excluding pS6)")
# axes[1, 1].set_xlabel("Single Cells (Top 300 by Abundance)")
# axes[1, 1].set_ylabel("Antibodies (Top 10 by Abundance)")
# axes[1, 1].text(-0.1, 1.05, "D", fontsize=16, fontweight="bold", transform=axes[1, 1].transAxes)

# # Adjust layout
# plt.tight_layout()

# # Save the figure
# output_fig_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/kite_vs_scd_processing/combined_plot_with_panels_top300_top10ab_no_pS6.png"
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

# Get the total number of single cells
kite_cells_total = kite_df["SingleCell_BARCODE"].nunique()
scd_cells_total = scd_df["SingleCell_BARCODE"].nunique()

# Find common single-cell barcodes in both datasets
common_cells = set(kite_df["SingleCell_BARCODE"]).intersection(set(scd_df["SingleCell_BARCODE"]))

# Filter both datasets to keep only common single cells
kite_filtered = kite_df[kite_df["SingleCell_BARCODE"].isin(common_cells)]
scd_filtered = scd_df[scd_df["SingleCell_BARCODE"].isin(common_cells)]

# Group and pivot for heatmaps
kite_grouped = kite_filtered.groupby(["SingleCell_BARCODE", "AB_BARCODE"])["AB_COUNT"].sum().reset_index()
scd_grouped = scd_filtered.groupby(["SingleCell_BARCODE", "AB_BARCODE"])["AB_COUNT"].sum().reset_index()

kite_heatmap = kite_grouped.pivot(index="AB_BARCODE", columns="SingleCell_BARCODE", values="AB_COUNT").fillna(0)
scd_heatmap = scd_grouped.pivot(index="AB_BARCODE", columns="SingleCell_BARCODE", values="AB_COUNT").fillna(0)

# Sort antibodies by total abundance (high to low)
kite_heatmap = kite_heatmap.loc[kite_heatmap.sum(axis=1).sort_values(ascending=False).index]
scd_heatmap = scd_heatmap.loc[scd_heatmap.sum(axis=1).sort_values(ascending=False).index]

# Select high-abundance single cells
kite_cell_sums = kite_heatmap.sum(axis=0)  # Sum across antibodies per cell
scd_cell_sums = scd_heatmap.sum(axis=0)

kite_sorted_cells = kite_cell_sums.sort_values(ascending=False).index
scd_sorted_cells = scd_cell_sums.sort_values(ascending=False).index

top_kite_cells = kite_sorted_cells[:300]  # Select top 300 most abundant cells
top_scd_cells = scd_sorted_cells[:300]

kite_sample = kite_heatmap[top_kite_cells]  # Subset heatmap for high-abundance cells
scd_sample = scd_heatmap[top_scd_cells]

# Remove pS6 from the heatmaps
kite_sample_no_pS6 = kite_sample.drop("pS6 [S240/S244] (2)", errors="ignore")
scd_sample_no_pS6 = scd_sample.drop("pS6 [S240/S244] (2)", errors="ignore")

# Sort antibodies by total abundance (high to low) and select top 10
kite_top_antibodies = kite_sample_no_pS6.sum(axis=1).sort_values(ascending=False).head(10).index
scd_top_antibodies = scd_sample_no_pS6.sum(axis=1).sort_values(ascending=False).head(10).index

# Subset the heatmaps to include only the top 10 antibodies
kite_sample_top10 = kite_sample_no_pS6.loc[kite_top_antibodies]
scd_sample_top10 = scd_sample_no_pS6.loc[scd_top_antibodies]





# Create the figure with subplots
fig, axes = plt.subplots(2, 2, figsize=(20, 16))

### 1. Panel A: Bar plot of single cells
axes[0, 0].bar(["KITE", "SCD"], [kite_cells_total, scd_cells_total], color=["lightgreen", "orange"])
axes[0, 0].set_title("Number of Single Cells Retrieved")
axes[0, 0].set_ylabel("Number of Cells")
axes[0, 0].text(-0.1, 1.05, "A", fontsize=16, fontweight="bold", transform=axes[0, 0].transAxes)

### 2. Panel B: Density Plot of AB_COUNT
kite_counts = kite_df["AB_COUNT"].values
scd_counts = scd_df["AB_COUNT"].values

sns.kdeplot(kite_counts, ax=axes[0, 1], color="lightgreen", label="KITE", fill=True, log_scale=True)
sns.kdeplot(scd_counts, ax=axes[0, 1], color="orange", label="SCDemultiplexing", fill=True, log_scale=True)

axes[0, 1].set_title("Density Plot of Protein Counts per Cell (Log Scale)")
axes[0, 1].set_xlabel("Protein Count Per Cell")
axes[0, 1].set_ylabel("Density")
axes[0, 1].legend()
axes[0, 1].text(-0.1, 1.05, "B", fontsize=16, fontweight="bold", transform=axes[0, 1].transAxes)

### 3. Panel C: Heatmaps for SCDemultiplexing (with and without pS6)
# Heatmap with pS6
sns.heatmap(scd_sample.loc[scd_sample.sum(axis=1).sort_values(ascending=False).head(10).index], 
            ax=axes[1, 0], cmap="Reds", linewidths=0.01, linecolor="gray", robust=True)
axes[1, 0].set_title("Top 10 Antibody Counts per Single Cell (SCDemultiplexing, Including pS6)")
axes[1, 0].set_xlabel("Single Cells (Top 300 by Abundance)")
axes[1, 0].set_ylabel("Antibodies (Top 10 by Abundance)")
axes[1, 0].text(-0.1, 1.05, "C", fontsize=16, fontweight="bold", transform=axes[1, 0].transAxes)

# Heatmap without pS6
sns.heatmap(scd_sample_top10, ax=axes[1, 1], cmap="Reds", linewidths=0.01, linecolor="gray", robust=True)
axes[1, 1].set_title("Top 10 Antibody Counts per Single Cell (SCDemultiplexing, Excluding pS6)")
axes[1, 1].set_xlabel("Single Cells (Top 300 by Abundance)")
axes[1, 1].set_ylabel("Antibodies (Top 10 by Abundance)")
axes[1, 1].text(-0.1, 1.05, "D", fontsize=16, fontweight="bold", transform=axes[1, 1].transAxes)

# Adjust layout
plt.tight_layout()

# Save the figure
output_fig_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/kite_vs_scd_processing/main_text_figure_with_pS6_contrast.png"
plt.savefig(output_fig_path, dpi=300, bbox_inches="tight")

# Show the figure
plt.show()

# Print output file path
print(f"Figure saved to: {output_fig_path}")


# # For kite:
# # Create the figure with subplots for KITE heatmaps
# fig, axes = plt.subplots(1, 2, figsize=(18, 9))

# ### 1. KITE Heatmap with pS6
# sns.heatmap(kite_sample.loc[kite_sample.sum(axis=1).sort_values(ascending=False).head(10).index], 
#             ax=axes[0], cmap="Reds", linewidths=0.01, linecolor="gray", robust=True)
# axes[0].set_title("Top 10 Antibody Counts per Single Cell (KITE, Including pS6)")
# axes[0].set_xlabel("Single Cells (Top 300 by Abundance)")
# axes[0].set_ylabel("Antibodies (Top 10 by Abundance)")
# axes[0].text(-0.1, 1.05, "A", fontsize=16, fontweight='bold', ha='center', va='center', transform=axes[0].transAxes)


# ### 2. KITE Heatmap without pS6
# sns.heatmap(kite_sample_top10, ax=axes[1], cmap="Reds", linewidths=0.01, linecolor="gray", robust=True)
# axes[1].set_title("Top 10 Antibody Counts per Single Cell (KITE, Excluding pS6)")
# axes[1].set_xlabel("Single Cells (Top 300 by Abundance)")
# axes[1].set_ylabel("Antibodies (Top 10 by Abundance)")
# axes[1].text(-0.1, 1.05, "B", fontsize=16, fontweight='bold', ha='center', va='center', transform=axes[1].transAxes)

# # Adjust layout
# plt.tight_layout()

# # Save the supplementary figure
# supplementary_fig_path = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/kite_vs_scd_processing/supplementary_kite_heatmaps.png"
# plt.savefig(supplementary_fig_path, dpi=300, bbox_inches="tight")

# # Show the figure
# plt.show()

# # Print output file path
# print(f"Supplementary figure saved to: {supplementary_fig_path}")