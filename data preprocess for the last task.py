import pandas as pd

file_path = "data/HDR23-24_Composite_indices_complete_time_series.csv"
data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Filter columns using regex to capture MYS and GNIPC across years
mys_columns = data.filter(regex=r'mys_\d{4}').columns  # Columns for Mean Years of Schooling (e.g., mys_1990, mys_2022)
gnipc_columns = data.filter(regex=r'gnipc_\d{4}').columns  # Columns for GNIPC (e.g., gnipc_1990, gnipc_2022)

# Ensure the dataset contains "country" and "region"
if 'country' in data.columns and 'region' in data.columns:
    selected_columns = ['country', 'region'] + list(mys_columns) + list(gnipc_columns)
else:
    raise KeyError("Dataset must contain 'country' and 'region' columns.")

# Select relevant columns
filtered_data = data[selected_columns]

# Drop rows with missing values in MYS or GNIPC
filtered_data = filtered_data.dropna(subset=mys_columns.union(gnipc_columns))

# Normalize GNIPC and MYS columns (optional)
for col in mys_columns.union(gnipc_columns):
    filtered_data[f'{col}_normalized'] = (filtered_data[col] - filtered_data[col].mean()) / filtered_data[col].std()

# Save the preprocessed data to a CSV file
output_file_path = "data/preprocessed_gnipc_mys.csv"
filtered_data.to_csv(output_file_path, index=False)

# Display a sample of the preprocessed data
print(f"Preprocessed Data Sample:\n{filtered_data.head()}")
print(f"Data saved to: {output_file_path}")
