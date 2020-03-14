import pandas as pd
from operator import itemgetter
import etl

from pprint import pprint as pp

# Dataframes
# `df_us` A Dictionary of case, death, and recovery dataframes for the US
# `df_us_states` A Dictionary of state-level case, death, and recovery dataframes for the US
# `df_us_population` 2019 US census population data by state, sub-region, and region

# Functions
# `us_data(df)` Filter input dataframe on US rows.
# `us_data_state(df)` Filter input US dataframe state-level records.
# `population_for_state(state_name)`

# All US data. Applied to cases, deaths, recoveries in the dictionary `df_us`
def us_data(df):
    df = df.rename(columns={'province_state': 'state'})
    # For consistency with census data
    df.state = df.state.apply(lambda state: (state, 'District of Columbia') [state == 'Washington, D.C.'])
    df.state, df['state_abbrev'] = itemgetter(0, 1)(df.state.str.split(', ').str)
    return df

# Sate-level US data. Applied to cases, deaths, recoveries in the dictionary `df_us_states`
def us_data_state(df):
    df = df[df['state'].isin(df_us_population['state'])]
    return df[['state', 'cases']]

# Unused at present
def population_for_state(state_name):
    return df_us_population[df_us_population.state == state_name].iloc[0].population_2019

# US population
df_us_population = pd.read_csv('csv/us_population.csv')

# Dict of all US data
df_us = {
    'cases': us_data(etl.for_country(etl.df_cases, 'US')),
    'deaths': us_data(etl.for_country(etl.df_deaths, 'US')),
    'recovered': us_data(etl.for_country(etl.df_recovered, 'US'))
}

# Dict of US state-level data
df_us_states = {
    'cases': us_data_state(df_us['cases']),
    'deaths': us_data_state(df_us['deaths']),
    'recovered': us_data_state(df_us['recovered']),
}
