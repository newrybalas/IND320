import streamlit as st
import pandas as pd

st.title("Reservoir data table")

# Load the reservoir data and cache it for faster app performance
@st.cache_data
def load_data():
    return pd.read_csv("Project work/reservoirs.csv", sep=",")

df = load_data()

# Display the imported data
# st.dataframe(df)
#---------------------------------------------------

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

# Display the data with the new column names
st.dataframe(df)

#------------------------------------------------------------------
st.subheader("Reservoir data – January 1995")

# Convert the date column to datetime to filter the data by year and month
df["date_Id"] = pd.to_datetime(df["date_Id"])

# Sort the data by date
df = df.sort_values("date_Id")

# Find the earliest date
first_date = df["date_Id"].min()

# Select data from the first month
first_month = df[
    (df["date_Id"].dt.year == first_date.year) &
    (df["date_Id"].dt.month == first_date.month)
]

# Display all columns forthe first month and show date without time
st.dataframe(
    first_month,
    column_config={
        "date_Id": st.column_config.DateColumn(
            "date_Id",
            format="YYYY-MM-DD"
        )
    },
    hide_index=True
)

#------------------------------------------------------------------
st.caption(
    "LineChartColumn() is only used for numerical columns. "
    "Therefore, non-numerical columns like date_Id, area_type og next_publication_date, are not displayed as line charts."
)
# Select the numeric columns
numeric_columns = first_month.select_dtypes(include="number").columns

# Create one row for each numeric column
chart_data = pd.DataFrame({
    "Column": numeric_columns,
    "January 1995": [
        first_month[column].tolist()
        for column in numeric_columns
    ]
})


# Show the first month as row-wise line charts
st.dataframe(
    chart_data,
    column_config={
        "January 1995": st.column_config.LineChartColumn(
            "January 1995"
        )
    },
    hide_index=True
)

