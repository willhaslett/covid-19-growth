import pandas as pd
import pickle
import c19all
import constants

locations = constants.US_LOCATIONS_IN_SOURCE
population = constants.US_POPULATION
cruise_ships = constants.CRUISE_SHIPS
stabbrev = constants.US_STATE_ABBREVS

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
    df['county'] = None
    df['territory'] = None
    df['is_state'] = None
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