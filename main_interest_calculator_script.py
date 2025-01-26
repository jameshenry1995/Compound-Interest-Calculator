import os
import subprocess
import sys

def install_requirements():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError:
        print("Error installing dependencies. Check requirements.txt.")

install_requirements()

#import polars as pl
import pandas as pd
import altair as alt
import altair_viewer
import streamlit as st
alt.renderers.enable('html')




def compound_interest_recurr_invest_fun(recur_saving, interest_rate, compound_occurences, number_of_years):
    sum_recur_deposit = ( ( (1 + interest_rate/ compound_occurences) ** (number_of_years * compound_occurences) ) - 1 ) / (interest_rate / compound_occurences)
    compound_rate_eoy = 1 + (interest_rate / compound_occurences)
    future_value = recur_saving * sum_recur_deposit * compound_rate_eoy
    return future_value


import polars as pl

def compound_interest_recurr_invest_df(recur_saving, interest_rate, compound_occurences, number_of_years):
    data = []
    
    for t in range(1, number_of_years + 1):
        sum_recur_deposit = (((1 + interest_rate/ compound_occurences) ** (t* compound_occurences) ) - 1) / (interest_rate / compound_occurences)
        compound_rate_eoy = 1 + (interest_rate / compound_occurences)
        future_value = recur_saving * sum_recur_deposit * compound_rate_eoy
        data.append((t, future_value))
    
    df = pl.DataFrame(data, schema=["Year", "Future Value"])
    return df

# Example Usage




st.title("📈 Compound Interest Dashboard")

# Sidebar Inputs
recur_saving = st.sidebar.number_input("Recurring Savings ($)", min_value=10, value=1000, step=10)
interest_rate = st.sidebar.slider("Annual Interest Rate (%)", min_value=0.01, max_value=20.0, value=5.0, step=0.1) / 100
number_of_years = st.sidebar.slider("Number of Years", min_value=1, max_value=50, value=10, step=1)



df = compound_interest_recurr_invest_df(recur_saving, interest_rate, 12, number_of_years)
#print(compound_interest_recurr_invest_fun(1000, 0.05, 12, 2))

df_pandas = df.to_pandas()

# Create Vega-Altair Line Chart
chart = alt.Chart(df_pandas).mark_line(point=True).encode(
    x=alt.X('Year:Q', title="Year"),
    y=alt.Y('Future Value:Q', title="Future Value (CHF)", scale=alt.Scale(zero=False)),
    tooltip=['Year', 'Future Value']
).properties(
    title="Growth of Investment Over Time",
    width=600,
    height=400
)

print(compound_interest_recurr_invest_fun(1000, 0.05, 12, 2))


# Display Chart
st.altair_chart(chart, use_container_width=True)
