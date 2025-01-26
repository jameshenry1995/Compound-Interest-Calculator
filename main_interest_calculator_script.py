import pandas as pd
import altair as alt
import streamlit as st
from calculation_functions import (
    compound_interest_recurr_invest_df,
    compound_interest_recurr_invest_fun,
    compound_target_recurr_invest_fun
)

# Set up Streamlit page configuration
st.set_page_config(page_title="Compound Interest Calculator", layout="wide")

# Sidebar navigation
page = st.sidebar.radio("Select Page", ["Investment Growth Chart", "Target Calculation"])

if page == "Investment Growth Chart":
    st.title("📈 Compound Interest Dashboard")
    
    # Sidebar inputs
    recur_saving = st.sidebar.number_input("Recurring Savings (CHF)", min_value=1, value=50000, step=50)
    interest_rate = st.sidebar.slider("Annual Interest Rate (%)", min_value=0.1, max_value=100.0, value=5.0, step=0.1) / 100
    number_of_years = st.sidebar.slider("Number of Years", min_value=1, max_value=100, value=10, step=1)
    initial_capital = st.sidebar.number_input("Initial Capital (CHF)", min_value=0, value=0, step=100)

    # Calculate dataframe
    df = compound_interest_recurr_invest_df(recur_saving, interest_rate, 12, number_of_years, initial_capital)
    df_pandas = df.to_pandas()

    # Create and display Vega-Altair chart
    chart = alt.Chart(df_pandas).mark_line(point=True).encode(
        x=alt.X('Year:Q', title="Year"),
        y=alt.Y('Future Value:Q', title="Future Value (CHF)", scale=alt.Scale(zero=False)),
        tooltip=['Year', 'Future Value']
    ).properties(
        title="Growth of Investment Over Time",
        width=600,
        height=400
    )

    st.altair_chart(chart, use_container_width=True)

elif page == "Target Calculation":
    st.title("🎯 Investment Target Calculator")
    
    # User inputs for the target calculation
    starting_capital = st.number_input("Starting Capital (CHF)", min_value=0, value=10000, step=100)
    target_value = st.number_input("Target Amount (CHF)", min_value=1, value=100000, step=100)
    time = st.number_input("Time (years)", min_value=1, max_value=100, value=10, step=1)
    interest_rate_new = st.sidebar.slider("Annual Interest Rate (%)", min_value=0.1, max_value=100.0, value=5.0, step=0.1) / 100
    
    # Calculate result using myfunc
    if st.button("Calculate"):
        result = compound_target_recurr_invest_fun(starting_capital, target_value, time, interest_rate_new, 12)
        st.write(f"The required monthly saving amount is: **{result:.2f}**")
