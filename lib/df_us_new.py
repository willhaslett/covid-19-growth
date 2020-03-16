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
    'unkown_type',
    'is_state',
    'lat',
    'long',
    'sub_region',
    'region',
]

# Add any new US locations in the JH data as unkown_type
_new_locations = {}
df = c19all.for_country(c19all.df_cases, 'US')
df = df.province_state.unique()
df = pd.DataFrame(data=df)
for i in range(len(df)):
    location = df.iloc[i, 0]
    if location in locations:
        _new_locations[location] = 'unkown_type'
locations = locations.update(_new_locations)

def _parse_locations(df):
    # The District of Columbia is treated as a state
    for i in range(len(df)):
        location = df.loc[i, '_location']
        if locations[location] == 'state':
            df.loc[i, 'is_state'] = True
            df.loc[i, 'state'] = location
        elif locations[location] == 'county':
            df.loc[i, 'is_state'] = False
            df.loc[i, 'county'] = location
        elif locations[location] == 'territory':
            df.loc[i, 'is_state'] = False
            df.loc[i, 'territory'] = location
        else:
            df.loc[i, 'unknown_type'] = location

def _us_data(df):
    df = df.rename(columns={'province_state': '_location'})
    df['state'] = None
    df['county'] = None
    df['territory'] = None
    df['unknown_type'] = None
    df['is_state'] = None
    # Remove cruise ship data
    df = df[~df._location.isin(cruise_ships)]
    df = df.reset_index(drop=True)
    _parse_locations(df)
    return df

# df = _us_data(c19all.for_country(c19all.df_cases, 'US'))
df = c19all.for_country(c19all.df_cases, 'US')
df = df.province_state.unique()
df = pd.DataFrame(data=df)
df.to_csv('foo.csv', index=False)

print(df)

# Raw US data
# df_us = {
#     'cases': _us_data(c19all.for_country(c19all.df_cases, 'US')),
#     'deaths': _us_data(c19all.for_country(c19all.df_deaths, 'US')),
#     'recovered': _us_data(c19all.for_country(c19all.df_recovered, 'US'))
# }