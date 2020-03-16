import pandas as pd
import pickle
import c19all
import constants

# NOTE: Creation of the three US dataframes is quite slow currently, due to the use of row-wise
#       iteration when parsing locations. For downstream work, you may want to use the
#       assocciated pickle file. See update_pickles.py

locations = constants.US_LOCATIONS_IN_SOURCE
population = constants.US_POPULATION
cruise_ships = constants.CRUISE_SHIPS
stabbrev = constants.US_STATE_ABBREVS


_output_columns = [
    'date',
    'day',
    'cases',
    'state',
    'county',
    'territory',
    'other',
    'unkown_type',
    'is_state',
    'lat',
    'long',
    'sub_region',  # only state-level records
    'region',      # only state-level records
    'population',  # only state-level records
]

# Add any new US locations in the JH data as unkown_type
_new_locations = {}
df = c19all.for_country(c19all.df_cases, 'US')
df = df.province_state.unique()
df = pd.DataFrame(data=df)
for i in range(len(df)):
    location = df.iloc[i, 0]
    if location not in locations:
        _new_locations[location] = 'unkown_type'
if bool(_new_locations):
    print('New locations found. constants.US_LOCATIONS_IN_SOURCE needs to be updated')


def _parse_locations(df):
    # The District of Columbia is treated as a state
    for i in range(len(df)):
        location = df.loc[i, '_location']
        if locations[location] == 'state':
            df.loc[i, 'is_state'] = True
            df.loc[i, 'state'] = location
            df.loc[i, 'sub_region'] = population[location]['sub_region']
            df.loc[i, 'region'] = population[location]['region']
            df.loc[i, 'population'] = population[location]['population']
        elif locations[location] == 'county':
            df.loc[i, 'is_state'] = False
            df.loc[i, 'county'] = location
        elif locations[location] == 'territory':
            df.loc[i, 'is_state'] = False
            df.loc[i, 'territory'] = location
        elif locations[location] == 'other':
            df.loc[i, 'is_state'] = False
            df.loc[i, 'other'] = location
        else:
            df.loc[i, 'unknown_type'] = location


def _us_data(df):
    df = df.rename(columns={'province_state': '_location'})
    df['state'] = None
    df['county'] = None
    df['territory'] = None
    df['other'] = None
    df['unknown_type'] = None
    df['is_state'] = None
    # Remove cruise ship data
    df = df[~df._location.isin(cruise_ships)]
    # Merge names for the District of Columbia
    df._location = df._location.apply(lambda state: (
        state, 'District of Columbia')[state == 'Washington, D.C.'])
    df = df.reset_index(drop=True)
    _parse_locations(df)
    return df.filter(items=_output_columns)


df = _us_data(c19all.for_country(c19all.df_cases, 'US'))
print(df)
# df.to_csv('csv/foo.csv', index=False)

# Raw US data
# df_us = {
#     'cases': _us_data(c19all.for_country(c19all.df_cases, 'US')),
#     'deaths': _us_data(c19all.for_country(c19all.df_deaths, 'US')),
#     'recovered': _us_data(c19all.for_country(c19all.df_recovered, 'US'))
# }
