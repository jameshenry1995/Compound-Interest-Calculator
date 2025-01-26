# Importing Packages
import pandas as pd
import altair as alt
import altair_viewer
import streamlit as st
alt.renderers.enable('html')


# Importing the necessary calculation functions from calculation_functions.py
from calculation_functions import compound_interest_recurr_invest_df
from calculation_functions import compound_interest_recurr_invest_fun





# Defining a title for the Dashboard
st.title("📈 Compound Interest Dashboard")



# Creating the Sidebar Inputs
recur_saving = st.sidebar.number_input("Recurring Savings ($)", min_value=10, value=1000, step=10)
interest_rate = st.sidebar.slider("Annual Interest Rate (%)", min_value=0.01, max_value=20.0, value=5.0, step=0.1) / 100
number_of_years = st.sidebar.slider("Number of Years", min_value=1, max_value=50, value=10, step=1)




# Creating the dataframe based on the inputs
df = compound_interest_recurr_invest_df(recur_saving, interest_rate, 12, number_of_years)


# Converting the polars df to pandas 
df_pandas = df.to_pandas()



# Create Vega-Altair Line Chart Time Series
chart = alt.Chart(df_pandas).mark_line(point=True).encode(
    x=alt.X('Year:Q', title="Year"),
    y=alt.Y('Future Value:Q', title="Future Value (CHF)", scale=alt.Scale(zero=False)),
    tooltip=['Year', 'Future Value']
).properties(
    title="Growth of Investment Over Time",
    width=600,
    height=400
)



# Display Chart
st.altair_chart(chart, use_container_width=True)

