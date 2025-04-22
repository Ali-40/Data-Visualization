import plotly.express as px
import pandas as pd

# Load the dataset
data_path = "data/preprocessed_gnipc_mys.csv"
data = pd.read_csv(data_path)

# Map region codes to region names
region_mapping = {
    "SA": "South America",
    "ECA": "Europe & Central Asia",
    "AS": "Asia",
    "LAC": "Latin America & Caribbean",
    "SSA": "Sub-Saharan Africa",
    "EAP": "East Asia & Pacific",
}
data['region'] = data['region'].map(region_mapping)

# Melt the dataset for plotting
plot_df = data.melt(id_vars=["country", "region"], var_name="year_attribute", value_name="value")
plot_df['year'] = plot_df['year_attribute'].str.extract(r'(\d{4})').astype(int)
plot_df['attribute'] = plot_df['year_attribute'].str.contains('mys').map({True: "MYS", False: "GNIPC"})

# Split MYS and GNIPC data
mys_df = plot_df[plot_df['attribute'] == "MYS"]
gnipc_df = plot_df[plot_df['attribute'] == "GNIPC"]

# Merge MYS and GNIPC data to align years for each country
merged_df = pd.merge(
    mys_df,
    gnipc_df,
    on=["country", "region", "year"],
    suffixes=("_mys", "_gnipc")
)

# Define a custom color palette
custom_colors = {
    "South America": "#1f77b4",  # Blue
    "Europe & Central Asia": "#ff7f0e",  # Orange
    "Asia": "#2ca02c",  # Green
    "Latin America & Caribbean": "#d62728",  # Red
    "Sub-Saharan Africa": "#000000",  # Black
    "East Asia & Pacific": "#8c564b"  # Brown
}

# Create scatter plot with manually adjusted marker size
fig = px.scatter(
    merged_df,
    x="value_mys",
    y="value_gnipc",
    color="region",
    hover_name="country",
    animation_frame="year",
    labels={"value_mys": "Mean Years of Schooling (MYS)", "value_gnipc": "Gross National Income per Capita (GNIPC)"},
    title="Impact of Education on Economic Growth Over Time by Country",
    color_discrete_map=custom_colors
)

# Update marker size globally
fig.update_traces(marker=dict(size=10))  # Increase the size of all bubbles

# Update axes ranges
fig.update_layout(
    xaxis=dict(
        title="Mean Years of Schooling (MYS)",
        range=[0, 14]
    ),
    yaxis=dict(
        title="Gross National Income per Capita (GNIPC)",
        range=[0, 105000]
    )
)

fig.show()
