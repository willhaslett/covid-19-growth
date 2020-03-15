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

def _parse_locations(df):
    # Iteration rather than vector functions for clarity and bug prevention
    for i in range(len(df)):
        location = df.loc[i, '_location']
        # Is it a state-level record?
        if location.isin(population.keys():
            df.loc[i, 'is_state'] = True
            df.loc[i, 'state'] = location
        # Is it a county-level record? (brittle)
        elif location.str.contains(', ')

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
    _parse_locations(df)
    return df

df = _us_data(c19all.for_country(c19all.df_cases, 'US'))

print(df)

# Raw US data
# df_us = {
#     'cases': _us_data(c19all.for_country(c19all.df_cases, 'US')),
#     'deaths': _us_data(c19all.for_country(c19all.df_deaths, 'US')),
#     'recovered': _us_data(c19all.for_country(c19all.df_recovered, 'US'))
# }