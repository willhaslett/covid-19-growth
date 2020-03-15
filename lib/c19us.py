import pandas as pd
from operator import itemgetter
import c19all
import csv
from constants import US_POPULATION as us_population
from constants import CRUISE_SHIPS as cruise_ships

from pprint import pprint as pp

# Dataframes
# `df_us` A Dictionary of case, death, and recovery dataframes for the US
# `df_us_states` A Dictionary of state-level case, death, and recovery dataframes for the US
# `df_us_counties` A Dictionary of county-level case, death, and recovery dataframes for the US
# `df_us_population` 2019 US census population data by state, sub-region, and region

# Functions
# `us_data(df)` Filter input dataframe on US rows
# `us_data_state(df)` Filter input US dataframe state-level records

def _us_data(df):
    df = df.rename(columns={'province_state': 'state_county'})
    df = df[~df.state_county.isin(cruise_ships)]
    # For consistency with census data
    df.state_county = df.state_county.apply(lambda state: (state, 'District of Columbia') [state == 'Washington, D.C.'])
    df = df.drop(['country'], axis=1)
    return df
print("\ndf_us:")
print(df_us['cases'])

def _us_data_state(df):
    df = df.rename(columns={'state_county': 'state'})
    df = df[df.state.isin(us_population.keys())]
    df['population'] = df.state.apply(lambda state: us_population[state]['population'])
    df['sub_region'] = df.state.apply(lambda state: us_population[state]['sub_region'])
    df['region'] = df.state.apply(lambda state: us_population[state]['region'])
    return df[['date', 'day', 'cases', 'state', 'population', 'sub_region', 'region']]

# Dict of US state-level data
df_us_state = {
    'cases': _us_data_state(df_us['cases']),
    'deaths': _us_data_state(df_us['deaths']),
    'recovered': _us_data_state(df_us['cases'])
}
print("\ndf_us_state:")
print(df_us_state['cases'])

def _us_data_county(df):
    df = df.rename(columns={'state_county': 'county'})
    df = df[~df.county.isin(us_population.keys())]
    df = df[~df.county.isin(cruise_ships)]
    return df[['date', 'day', 'county', 'cases']]

# Dict of US county-level data
df_us_county = {
    'cases': _us_data_county(df_us['cases']),
    'deaths': _us_data_county(df_us['deaths']),
    'recovered': _us_data_county(df_us['recovered']),
}
print("\ndf_us_county:")
print(df_us_county['cases'])