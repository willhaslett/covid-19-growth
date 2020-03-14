import pandas as pd
from operator import itemgetter
import c19all

from pprint import pprint as pp

# Dataframes
# `df_us` A Dictionary of case, death, and recovery dataframes for the US
# `df_us_states` A Dictionary of state-level case, death, and recovery dataframes for the US
# `df_us_counties` A Dictionary of county-level case, death, and recovery dataframes for the US
# `df_us_population` 2019 US census population data by state, sub-region, and region

# Functions
# `us_data(df)` Filter input dataframe on US rows
# `us_data_state(df)` Filter input US dataframe state-level records
# `population_for_state(state_name)`

# US population by state, region and subregion
df_us_population = pd.read_csv('csv/us_population.csv')

def _us_data(df):
    df = df.rename(columns={'province_state': 'state'})
    # For consistency with census data
    df.state = df.state.apply(lambda state: (state, 'District of Columbia') [state == 'Washington, D.C.'])
    df.state, df['state_abbrev'] = itemgetter(0, 1)(df.state.str.split(', ').str)
    return df

# Dict of all US data. Flagged as private bevcause of inconsistent types in the `state` column from upstream
_df_us = {
    'cases': _us_data(c19all.for_country(c19all.df_cases, 'US')),
    'deaths': _us_data(c19all.for_country(c19all.df_deaths, 'US')),
    'recovered': _us_data(c19all.for_country(c19all.df_recovered, 'US'))
}

# df_us as a public dataframe is deprecated and this will be removed
df_us = _df_us

def _us_data_state(df):
    df = df[df['state'].isin(df_us_population['state'])]
    return df[['day', 'state', 'cases']]

# Dict of US state-level data
df_us_state = {
    'cases': _us_data_state(df_us['cases']),
    'deaths': _us_data_state(df_us['deaths']),
    'recovered': _us_data_state(df_us['recovered']),
}

def _us_data_county(df):
    df = df[~df['state'].isin(df_us_population['state'])]
    return df[['day', 'state', 'cases']]

# Dict of US county-level data
df_us_county = {
    'cases': _us_data_county(df_us['cases']),
    'deaths': _us_data_county(df_us['deaths']),
    'recovered': _us_data_county(df_us['recovered']),
}