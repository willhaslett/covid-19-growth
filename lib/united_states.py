import pandas as pd
from operator import itemgetter
import etl

from pprint import pprint as pp

# US records with a state column for city/county data. Filter on state == NaN for state-level records
#   `df_cases_us` All US cases
#   `df_deaths_us` All US deaths
#   `df_recovered_us` All US recoveries

# US population dataframe
#   `df_population_us` 

# NOTE: The process of splitting out state abbreviations from the province_state column is destructive 
#       for that column
# Split province_state on the string ', ' creating new columns 'is_state' and 'state'
def us_data(df):
    df.province_state, df['state'] = itemgetter(
        0, 1)(df.province_state.str.split(', ').str)
    return df

# US data
df_cases_us = us_data(etl.for_country(etl.df_cases, 'US'))
df_deaths_us = us_data(etl.for_country(etl.df_deaths, 'US'))
df_recovered_us = us_data(etl.for_country(etl.df_recovered, 'US'))

# US population
df_population_us = pd.read_csv('csv/us_population.csv')