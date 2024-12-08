import os
import shutil
import numpy as np
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
# for name, dataset in zip(
#     ["Benin", "Sierra Leone", "Togo"],
#     [data_benin, data_sierraleone, data_togo]
# ):
#     numeric_data = dataset.select_dtypes(include=["number"])
    
#     if not numeric_data.empty:
#         correlation_matrix = numeric_data.corr()
        
#         # Create a heatmap
#         plt.figure(figsize=(10, 8))
#         sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", cbar=True)
        
#         plt.title(f"Correlation Heatmap for {name}", fontsize=16)
        
#         # Save plot
#         output_file = os.path.join(output_dir, f"{name.lower().replace(' ', '_')}_correlation_heatmap.png")
#         plt.savefig(output_file)
#         print(f"Correlation heatmap saved for {name} at {output_file}")
        
#         # Clear the current figure
#         plt.clf()
#     else:
#         print(f"No numeric data found in {name} dataset. Skipping correlation analysis.")


# # Wind Speed and Direction Analysis: Wind Rose Plot
# def plot_wind_rose(dataset, name):
#     if 'WS' in dataset.columns and 'WD' in dataset.columns:
#         wind_speed = dataset['WS'].dropna()
#         wind_direction = dataset['WD'].dropna()
        
#         plt.figure(figsize=(8, 8))
#         ax = plt.subplot(111, projection='polar')

#         # Convert wind direction from degrees to radians
#         wind_direction = np.radians(wind_direction)
        
#         ax.hist(wind_direction, bins=36, weights=wind_speed, histtype='stepfilled', color='blue', alpha=0.6)
        
#         ax.set_title(f"Wind Rose for {name}", fontsize=16)

#         output_file = os.path.join(output_dir, f"{name.lower().replace(' ', '_')}_wind_rose.png")
#         plt.savefig(output_file)
#         print(f"Wind rose saved for {name} at {output_file}")
        
#         plt.clf()
#     else:
#         print(f"Skipping wind rose plot for {name} due to missing columns.")

# # Call the function for each dataset
# for name, dataset in zip(["Benin", "Sierra Leone", "Togo"], [data_benin, data_sierraleone, data_togo]):
#     plot_wind_rose(dataset, name)

# # Temperature vs RH Analysis
# for name, dataset in zip(["Benin", "Sierra Leone", "Togo"], [data_benin, data_sierraleone, data_togo]):
#     if 'RH' in dataset.columns and 'Tamb' in dataset.columns:
#         plt.figure(figsize=(10, 6))
#         sns.scatterplot(x=dataset['RH'], y=dataset['Tamb'], hue=dataset['Tamb'], palette='viridis')
#         plt.title(f"Relative Humidity vs Temperature for {name}", fontsize=16)
#         plt.xlabel("Relative Humidity (%)")
#         plt.ylabel("Temperature (Tamb)")
#         plt.grid(True)

#         output_file = os.path.join(output_dir, f"{name.lower().replace(' ', '_')}_rh_vs_temp.png")
#         plt.savefig(output_file)
#         print(f"RH vs Temperature plot saved for {name} at {output_file}")
        
#         plt.clf()
#     else:
#         print(f"Skipping RH vs Temp plot for {name} as 'RH' or 'Tamb' is missing.")


# # Function for creating histograms (only for key columns)
# def plot_histograms(dataset, name, columns=None, max_plots=2):
#     if columns is None:
#         columns = ['GHI', 'DNI', 'DHI', 'WS', 'Tamb'] 
    
#     for idx, col in enumerate(columns[:max_plots]):
#         if col in dataset.columns:
#             plt.figure(figsize=(10, 6))
#             sns.histplot(dataset[col].dropna(), kde=True, color='blue', bins=30)
#             plt.title(f"Histogram of {col} for {name}", fontsize=16)
#             plt.xlabel(col)
#             plt.ylabel("Frequency")
#             plt.grid(True)
            
#             output_file = os.path.join(output_dir, f"{name.lower().replace(' ', '_')}_{col}_histogram.png")
#             plt.savefig(output_file)
#             print(f"Histogram of {col} saved for {name} at {output_file}")
            
#             plt.close()

# # Function for Z-Score Analysis (only for key columns)
# def plot_z_scores(dataset, name, columns=None, max_plots=2):
#     if columns is None:
#         columns = ['GHI', 'DNI', 'DHI', 'WS', 'Tamb'] 
    
#     for idx, col in enumerate(columns[:max_plots]): 
#         if col in dataset.columns:
#             z_scores = (dataset[col] - dataset[col].mean()) / dataset[col].std()
#             plt.figure(figsize=(10, 6))
#             sns.histplot(z_scores.dropna(), kde=True, color='red', bins=30)
#             plt.title(f"Z-Score Distribution of {col} for {name}", fontsize=16)
#             plt.xlabel("Z-Score")
#             plt.ylabel("Frequency")
#             plt.grid(True)

#             output_file = os.path.join(output_dir, f"{name.lower().replace(' ', '_')}_{col}_zscore.png")
#             plt.savefig(output_file)
#             print(f"Z-Score plot of {col} saved for {name} at {output_file}")
            
#             plt.close()

# # Function for Bubble Chart (only if all required columns are present)
# def plot_bubble_chart(dataset, name, max_plots=1):
#     required_columns = ['GHI', 'Tamb', 'WS', 'RH']
#     if all(col in dataset.columns for col in required_columns):
#         for idx in range(max_plots): 
#             plt.figure(figsize=(10, 6))
            
#             plt.scatter(
#                 dataset['GHI'], dataset['Tamb'], 
#                 s=dataset['RH'] * 10,  
#                 c=dataset['WS'], cmap='viridis', alpha=0.6, edgecolors="w", linewidth=0.5
#             )
#             plt.title(f"Bubble Chart for {name}: GHI vs Tamb vs WS", fontsize=16)
#             plt.xlabel("GHI (Solar Radiation)")
#             plt.ylabel("Tamb (Temperature)")
#             plt.colorbar(label="Wind Speed (WS)")
#             plt.grid(True)

#             output_file = os.path.join(output_dir, f"{name.lower().replace(' ', '_')}_ghi_vs_tamb_vs_ws_bubble.png")
#             plt.savefig(output_file)
#             print(f"Bubble chart saved for {name} at {output_file}")
            
#             plt.close()

# # Execute the functions for each dataset
# for name, dataset in zip(["Benin", "Sierra Leone", "Togo"], [data_benin, data_sierraleone, data_togo]):
#     # Generate histograms for key columns (GHI, DNI, DHI, WS, Tamb), limiting to 2 histograms per dataset
#     plot_histograms(dataset, name, max_plots=2)
    
#     # Perform Z-Score analysis for key columns (GHI, DNI, DHI, WS, Tamb), limiting to 2 Z-score plots per dataset
#     plot_z_scores(dataset, name, max_plots=2)
    
#     # Generate one bubble chart per dataset
#     plot_bubble_chart(dataset, name, max_plots=1)

# Function to clean the dataset
def clean_dataset(dataset, name):
    missing_values = dataset.isnull().sum()
    print(f"Missing values in {name} dataset:\n{missing_values}\n")

    if dataset['Comments'].isnull().all():
        print(f"Dropping 'Comments' column in {name} because it's entirely null.")
        dataset.drop(columns=['Comments'], inplace=True)

    dataset.fillna({
        'GHI': dataset['GHI'].mean(),
        'DNI': dataset['DNI'].mean(),
        'Tamb': dataset['Tamb'].mean(),
        'WS': dataset['WS'].mean(),
        'RH': dataset['RH'].mean()
    }, inplace=True)
    
    dataset.loc[dataset['Tamb'] < 0, 'Tamb'] = dataset['Tamb'].mean()
    dataset.loc[dataset['GHI'] < 0, 'GHI'] = 0
    dataset.loc[dataset['DNI'] < 0, 'DNI'] = 0
    
    dataset.loc[dataset['GHI'] > 2000, 'GHI'] = 2000
    dataset.loc[dataset['DNI'] > 2000, 'DNI'] = 2000
    
    print(f"Cleaned {name} dataset:\n{dataset.head()}\n")
    
    cleaned_file = f"output/{name.lower().replace(' ', '_')}_cleaned.csv"
    dataset.to_csv(cleaned_file, index=False)
    print(f"Cleaned dataset for {name} saved at {cleaned_file}\n")
    
    return dataset

for name, dataset in zip(["Benin", "Sierra Leone", "Togo"], [data_benin, data_sierraleone, data_togo]):
    cleaned_data = clean_dataset(dataset, name)
