import pandas as pd

# Load the complete dataset
file_path = r"\visualization intermediate submission\HDR23-24_Composite_indices_complete_time_series.csv"
data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Define the correct region codes that generally correspond to Asia
asian_region_codes = ['SA', 'AS', 'EAP']

# Initial filter by region
filtered_asian_countries = data[data['region'].isin(asian_region_codes)]

# Define a list of countries that should be excluded despite region code
non_asian_countries = ['Egypt', 'Tunisia', 'Somalia', 'Morocco', 'Algeria', 'Libya', 'Sudan']

# Explicitly remove non-Asian countries from the filtered data
filtered_asian_countries = filtered_asian_countries[~filtered_asian_countries['country'].isin(non_asian_countries)]

# Define a list of additional countries to include if needed (if missing from the initial filter)
additional_asian_countries = ['Israel', 'Turkey', 'Korea']  # Example countries not classified under SA/EAP/AS
additional_data = data[data['country'].isin(additional_asian_countries)]

# Combine the additional countries with the filtered dataset
final_asian_countries = pd.concat([filtered_asian_countries, additional_data])

# Extract HDI and GII columns
asian_countries_hdi = final_asian_countries.filter(regex=r'hdi_\d{4}')
asian_countries_gii = final_asian_countries.filter(regex=r'gii_\d{4}')

# Combine columns for output
asian_countries_hdi_gii = pd.concat([final_asian_countries['country'], asian_countries_hdi, asian_countries_gii], axis=1)

# Display a sample of the final data
print(f"Corrected Asian Countries Data:\n{asian_countries_hdi_gii.head()}")

# Save to CSV for Power BI visualization
output_file_path = "visualization_intermediate_submission/hdi_gii_filtered_asian_countries.csv"
asian_countries_hdi_gii.to_csv(output_file_path, index=False)
print(f"Filtered HDI and GII data for Asian countries saved to: {output_file_path}")