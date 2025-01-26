# Getting the install requirements function
from requirements_fun import install_requirements

# Installing requirements
install_requirements()

# Import Polars
import polars as pl


# Defining a function that directly calculated the saving amount after n years
def compound_interest_recurr_invest_fun(recur_saving, interest_rate, compound_occurences, number_of_years):
    sum_recur_deposit = ( ( (1 + interest_rate/ compound_occurences) ** (number_of_years * compound_occurences) ) - 1 ) / (interest_rate / compound_occurences)
    compound_rate_eoy = 1 + (interest_rate / compound_occurences)
    future_value = recur_saving * sum_recur_deposit * compound_rate_eoy
    return future_value


# Defining a function that stores the yearly compounded savings amount into a polars df
def compound_interest_recurr_invest_df(recur_saving, interest_rate, compound_occurences, number_of_years):
    data = []
    
    for t in range(1, number_of_years + 1):
        sum_recur_deposit = (((1 + interest_rate/ compound_occurences) ** (t* compound_occurences) ) - 1) / (interest_rate / compound_occurences)
        compound_rate_eoy = 1 + (interest_rate / compound_occurences)
        future_value = recur_saving * sum_recur_deposit * compound_rate_eoy
        data.append((t, future_value))
    
    df = pl.DataFrame(data, schema=["Year", "Future Value"])
    return df
