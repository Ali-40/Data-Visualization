import pandas as pd

# Load the data
data_path = "data/preprocessed_gnipc_mys.csv"
data = pd.read_csv(data_path)

# Shift MYS by 15 years to simulate a lag effect
for year in range(1990, 2008):  # Shift range to ensure valid 15-year gap
    mys_col = f"mys_{year}"
    gnipc_col = f"gnipc_{year + 15}"
    if mys_col in data.columns and gnipc_col in data.columns:
        data[f"{mys_col}_shifted"] = data[gnipc_col]

# Filter rows with non-null shifted values
shifted_data = data.filter(regex=r'(mys_\d{4}|gnipc_\d{4}_shifted)').dropna()

# Save the prepared dataset
shifted_data.to_csv("data/shifted_mys_gnipc.csv", index=False)
print("Shifted dataset saved as 'shifted_mys_gnipc.csv'")
