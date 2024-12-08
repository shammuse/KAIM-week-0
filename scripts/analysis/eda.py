import pandas as pd

# Load datasets
data_benin = pd.read_csv("data/benin-malanville.csv")
data_sierraleone = pd.read_csv("data/sierraleone-bumbuna.csv")
data_togo = pd.read_csv("data/togo-dapaong_qc.csv")

# Print basic info
for name, data in zip(["Benin", "Sierra Leone", "Togo"], 
                      [data_benin, data_sierraleone, data_togo]):
    print(f"Dataset: {name}")
    print(data.info())
    print(data.describe())
    print(data.head())
    print("-" * 50)
