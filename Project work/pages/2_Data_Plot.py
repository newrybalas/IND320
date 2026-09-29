import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Reservoir Data Plot")

# Load the reservoir data
@st.cache_data
def load_data():
    return pd.read_csv("Project work/reservoirs.csv", sep=",")

df = load_data()

# Rename columns to clear English names
df = df.rename(columns={
    "dato_Id": "date_Id",
    "omrType": "area_type",
    "omrnr": "area_number",
    "iso_aar": "iso_year",
    "iso_uke": "iso_week",
    "fyllingsgrad": "fill_level",
    "kapasitet_TWh": "capacity_TWh",
    "fylling_TWh": "fill_TWh",
    "neste_Publiseringsdato": "next_publication_date",
    "fyllingsgrad_forrige_uke": "fill_level_previous_week",
    "endring_fyllingsgrad": "change_in_fill_level"
})

# Convert the date column to datetime
df["date_Id"] = pd.to_datetime(df["date_Id"])

# Sort the data by date
df = df.sort_values("date_Id")

#------------------------------------------------------------

# Select numerical columns that are relevant for plotting
numeric_columns = df.select_dtypes(include="number").columns

# Remove columns that are not measurement values that are natural to plot over time 
numeric_columns = numeric_columns.drop(["iso_year", "iso_week", "area_number"])

# Create a list with the columns that can be plotted
column_options = ["All columns"] + list(numeric_columns)

# Dropdown menu for selecting a column
selected_column = st.selectbox(
    "Select a column:",
    column_options
)

#----------------------------------------------------------
# Create a year-month column for the slider
df["year_month"] = df["date_Id"].dt.to_period("M")

# Get all months in chronological order
months = sorted(df["year_month"].unique())

# Select a range of months
selected_months = st.select_slider(
    "Select month range:",
    options=months,
    value=(months[0], months[0])   # set the first month as the default
)

# Filter the data to the selected months
filtered_df = df[
    (df["year_month"] >= selected_months[0]) &
    (df["year_month"] <= selected_months[1])
]

# Select the numeric columns that can be plotted
numeric_columns = filtered_df.select_dtypes(include="number").columns

# Create the plot
fig, ax = plt.subplots()

if selected_column == "All columns":
    # Plot all numeric columns
    for column in numeric_columns:
        ax.plot(filtered_df["date_Id"], filtered_df[column], label=column)

elif selected_column in numeric_columns:
    # Plot the selected column
    ax.plot(
        filtered_df["date_Id"],
        filtered_df[selected_column],
        label=selected_column
    )

# Add a title based on the selected column
if selected_column == "All columns":
    ax.set_title("All Reservoir Data")
else:
    ax.set_title(f"Reservoir Data")

ax.set_xlabel("Date")
ax.set_ylabel("Value")

# Display the plot in Streamlit
st.pyplot(fig)

# Display the data with the new column names and sorted data by date
# st.dataframe(df)