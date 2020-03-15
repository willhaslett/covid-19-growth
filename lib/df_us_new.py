import pandas as pd
import pickle
import c19all
import constants
from constants import US_LOCATIONS_IN_SOURCE as locations
from constants import US_POPULATION as population
from constants import CRUISE_SHIPS as cruise_ships

output_columns = [
    'date',
    'day',
    'cases',
    'state',
    'county',
    'territory',
    'is_state',
    'lat',
    'long'
]

def _us_data(df):
    df = df.rename(columns={'province_state': '_location'})
    df['state'] = None
    # Remove cruise ship data
    df = df[~df._location.isin(cruise_ships)]
    # Rename Washington D.C. records
    df.state_county = df._location.apply(lambda state: (state, 'District of Columbia') [state == 'Washington, D.C.'])
    df = df.drop(['country'], axis=1)
    return df

df = _us_data(c19all.for_country(c19all.df_cases, 'US'))

print(df)

# Raw US data
# df_us = {
#     'cases': _us_data(c19all.for_country(c19all.df_cases, 'US')),
#     'deaths': _us_data(c19all.for_country(c19all.df_deaths, 'US')),
#     'recovered': _us_data(c19all.for_country(c19all.df_recovered, 'US'))
# }