import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load datasets
data_benin = pd.read_csv("data/benin-malanville.csv")
data_sierraleone = pd.read_csv("data/sierraleone-bumbuna.csv")
data_togo = pd.read_csv("data/togo-dapaong_qc.csv")

# # Create output directory
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Print basic info
# for name, data in zip(["Benin", "Sierra Leone", "Togo"], 
#                       [data_benin, data_sierraleone, data_togo]):
#     print(f"Dataset: {name}")
#     print(data.info())
#     print(data.describe())
#     print(data.head())
#     print("-" * 50)


# # Check for missing values and outliers
# for name, data in zip(["Benin", "Sierra Leone", "Togo"], 
#                       [data_benin, data_sierraleone, data_togo]):
#     print(f"Missing values in {name}:")
#     print(data.isnull().sum())
#     print("Outliers detected:")
#     numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
#     z_scores = data[numeric_cols].apply(lambda x: (x - x.mean()) / x.std())
#     outliers = (z_scores.abs() > 3).sum()
#     print(outliers)
#     print("-" * 50)


# # Convert 'Timestamp' column to datetime
# for dataset, name in zip(
#     [data_benin, data_sierraleone, data_togo],
#     ["Benin", "Sierra Leone", "Togo"]
# ):
#     try:
#         dataset['Timestamp'] = pd.to_datetime(dataset['Timestamp'])
#     except KeyError:
#         print(f"'Timestamp' column is missing in the {name} dataset")
#         continue


# # Time Series Analysis: Plot GHI, DNI, DHI, and Tamb over time
# for name, dataset in zip(
#     ["Benin", "Sierra Leone", "Togo"],
#     [data_benin, data_sierraleone, data_togo]
# ):
#     if 'Timestamp' in dataset.columns:
#         plt.figure(figsize=(12, 6))
        
#         # Plot each variable
#         plt.plot(dataset['Timestamp'], dataset['GHI'], label='GHI', color='orange', linewidth=1.5)
#         plt.plot(dataset['Timestamp'], dataset['DNI'], label='DNI', color='blue', linewidth=1.5)
#         plt.plot(dataset['Timestamp'], dataset['DHI'], label='DHI', color='green', linewidth=1.5)
#         plt.plot(dataset['Timestamp'], dataset['Tamb'], label='Tamb (Temperature)', color='red', linewidth=1.5)
        
#         plt.title(f"Time Series Analysis for {name}", fontsize=16)
#         plt.xlabel("Timestamp", fontsize=12)
#         plt.ylabel("Values", fontsize=12)
#         plt.legend(fontsize=10)
#         plt.grid(True, which='both', linestyle='--', linewidth=0.5)
        
#         output_file = os.path.join(output_dir, f"{name.lower().replace(' ', '_')}_time_series.png")
#         plt.savefig(output_file)
#         print(f"Plot saved for {name} dataset at {output_file}")
        
#         # Clear the current figure
#         plt.clf()
#     else:
#         print(f"Skipping {name} dataset because 'Timestamp' column is missing.")
        

# Correlation analysis for each dataset
for name, dataset in zip(
    ["Benin", "Sierra Leone", "Togo"],
    [data_benin, data_sierraleone, data_togo]
):
    numeric_data = dataset.select_dtypes(include=["number"])
    
    if not numeric_data.empty:
        correlation_matrix = numeric_data.corr()
        
        # Create a heatmap
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", cbar=True)
        
        plt.title(f"Correlation Heatmap for {name}", fontsize=16)
        
        # Save plot
        output_file = os.path.join(output_dir, f"{name.lower().replace(' ', '_')}_correlation_heatmap.png")
        plt.savefig(output_file)
        print(f"Correlation heatmap saved for {name} at {output_file}")
        
        # Clear the current figure
        plt.clf()
    else:
        print(f"No numeric data found in {name} dataset. Skipping correlation analysis.")