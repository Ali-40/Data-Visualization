import pandas as pd

# Load your dataset
file_path = "./data/hdi_gii_filtered_asian_countries.csv"  # Change this to your file location
data = pd.read_csv(file_path)

# Display the first few rows (for reference)
print(data.head())

# Unpivot HDI and GII columns (from 1990 to 2022)
hdi_columns = [f"hdi_{year}" for year in range(1990, 2023)]
gii_columns = [f"gii_{year}" for year in range(1990, 2023)]

# Melt (unpivot) the HDI and GII columns
hdi_melted = data.melt(id_vars=['country'], value_vars=hdi_columns,
                       var_name='year', value_name='hdi')
gii_melted = data.melt(id_vars=['country'], value_vars=gii_columns,
                       var_name='year', value_name='gii')

# Combine the unpivoted HDI and GII into a single DataFrame
hdi_melted['year'] = hdi_melted['year'].str.extract(r'(\d+)').astype(int)  # Extract year as an integer
gii_melted['year'] = gii_melted['year'].str.extract(r'(\d+)').astype(int)

# Merge the two melted dataframes on 'country' and 'year'
merged_data = pd.merge(hdi_melted, gii_melted, on=['country', 'year'])

# Display the transformed dataset
print(merged_data.head())

# Save the transformed data to a new CSV file
merged_data.to_csv("data/unpivoted_hdi_gii_asian_countries.csv", index=False)