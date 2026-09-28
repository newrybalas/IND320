import streamlit as st

# Create the pages
home = st.Page("pages/0_Home_page.py", title="Home")
data_table = st.Page("pages/1_Data_Table.py", title="Data Table")
data_plot = st.Page("pages/2_Data_Plot.py", title="Data Plot")

# Create the sidebar navigation
pg = st.navigation({
    "Navigation": [home, data_table, data_plot]
})

# Run the selected page
pg.run()