import pandas as pd
import os

# Define input and output paths
barcode_file = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/kite/NKI/Ex0003_kite_panel.csv"
features_file = "/scistor/informatica/ath100/SCDemultiplexing_Benchmark/benchmark_analysis/results/kite/NKI/features.tsv"

# Load barcode reference data
df = pd.read_csv(barcode_file)

# Clean antibody names (remove spaces, parentheses)
df["Antigen"] = df["Antigen"].str.replace(" ", "_", regex=True)
df["Antigen"] = df["Antigen"].str.replace(r"[()]", "", regex=True)

# Save feature file (barcode + antigen)
df[["Barcode", "Antigen"]].to_csv(features_file, index=False, header=False, sep="\t")

print(f"Feature file saved: {features_file}")
