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

# All US data. Used to build `df_us`, which should not be used unless you want to preserve the
# mixed types in the province_state column of the JH US data
def us_data(df):
    df = df.rename(columns={'province_state': 'state'})
    # For consistency with census data
    df.state = df.state.apply(lambda state: (state, 'District of Columbia') [state == 'Washington, D.C.'])
    df.state, df['state_abbrev'] = itemgetter(0, 1)(df.state.str.split(', ').str)
    return df

# Dict of all US data
df_us = {
    'cases': us_data(c19all.for_country(c19all.df_cases, 'US')),
    'deaths': us_data(c19all.for_country(c19all.df_deaths, 'US')),
    'recovered': us_data(c19all.for_country(c19all.df_recovered, 'US'))
}

# State-level US data. Used to build `df_us_state`
def us_data_state(df):
    df = df[df['state'].isin(df_us_population['state'])]
    return df[['day', 'state', 'cases']]

# Dict of US state-level data
df_us_state = {
    'cases': us_data_state(df_us['cases']),
    'deaths': us_data_state(df_us['deaths']),
    'recovered': us_data_state(df_us['recovered']),
}

# County-level US data. Used to build `df_us_county`
def us_data_county(df):
    df = df[~df['state'].isin(df_us_population['state'])]
    return df[['day', 'state', 'cases']]

# Dict of US county-level data
df_us_county = {
    'cases': us_data_county(df_us['cases']),
    'deaths': us_data_county(df_us['deaths']),
    'recovered': us_data_county(df_us['recovered']),
}

# Region-level US data. Used to build `df_us_region`
def us_data_region(df):
    regions = df_us_population.region.unique().tolist()
    pp(regions)

us_data_region(df_us_state['cases'])