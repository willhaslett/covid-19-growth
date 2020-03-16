import pandas as pd
import pickle
import c19all
import constants

# Creates `df_us`, a dictionary containing three dataframes, all of the same shape
#   `cases` US confirmed cases
#   `deaths` US deaths
#   `recovered` US recoveries

# NOTE: This takes a minute or two due to row-wise parsing of location fields
#       Consider using the associated pickle file for downstream work instead of importing this module

locations = constants.US_LOCATIONS_IN_SOURCE
population = constants.US_POPULATION
cruise_ships = constants.CRUISE_SHIPS
stabbrevs = constants.US_STATE_ABBREVS


_output_columns = [
    'date',
    'day',
    'state',
    'county',
    'territory',
    'other',
    'unkown_type',
    'sub_region',  # only state-level records
    'region',      # only state-level records
    'is_state',
    'lat',
    'long',
    'population',  # only state-level records
    'cases',
]

# Add any new US locations in the JH data as unkown_type
_new_locations = {}
df = c19all.for_country(c19all.df_all['cases'], 'US')
df = df.province_state.unique()
df = pd.DataFrame(data=df)
for i in range(len(df)):
    location = df.iloc[i, 0]
    if location not in locations:
        _new_locations[location] = 'unkown_type'
if bool(_new_locations):
    print('New locations found and assigned as unkown_type. constants.US_LOCATIONS_IN_SOURCE needs to be updated')


def _parse_locations(df):
    for i in range(len(df)):
        location = df.loc[i, '_location']
        if locations[location] == 'state':
            df.loc[i, 'is_state'] = True
            df.loc[i, 'state'] = location
            df.loc[i, 'sub_region'] = population[location]['sub_region']
            df.loc[i, 'region'] = population[location]['region']
            df.loc[i, 'population'] = int(
                round(population[location]['population']))
        elif locations[location] == 'county':
            df.loc[i, 'is_state'] = False
            # TODO: Error trapping here
            county_and_abbrev = location.split(', ')
            df.loc[i, 'county'] = county_and_abbrev[0].replace(' ', '')
            df.loc[i, 'state'] = stabbrevs[county_and_abbrev[1].replace(
                ' ', '')]
        elif locations[location] == 'territory':
            df.loc[i, 'is_state'] = False
            df.loc[i, 'territory'] = location
        elif locations[location] == 'other':
            df.loc[i, 'is_state'] = False
            df.loc[i, 'other'] = location
        else:
            df.loc[i, 'unknown_type'] = location
    return df


def _handle_special_cases(df):
    # Merge names for the District of Columbia
    df.other = df.other.apply(lambda other: (
        other, 'District of Columbia')[other == 'Washington, D.C.'])
    # Remove U.S. from the Virgin Islands
    df.territory = df.territory.apply(lambda territory: (
        territory, 'Virgin Islands')[territory == 'Virgin Islands, U.S.'])
    return df


def _us_data(df):
    df = df.rename(columns={'province_state': '_location'})
    df['state'] = None
    df['county'] = None
    df['territory'] = None
    df['other'] = None
    df['unknown_type'] = None
    df['is_state'] = None
    df = _parse_locations(df)
    df = _handle_special_cases(df)
    df = df.reset_index(drop=True)
    df.set_index(['date', 'day', 'state', 'county', 'territory',
                  'other', 'unknown_type', 'sub_region', 'region', 'is_state'])
    return df.filter(items=_output_columns)


df_us = {
    'cases': _us_data(c19all.for_country(c19all.df_all['cases'], 'US')),
    'deaths': _us_data(c19all.for_country(c19all.df_all['deaths'], 'US')),
    'recovered': _us_data(c19all.for_country(c19all.df_all['recovered'], 'US'))
}

# TODO
# def _cases_by_state(df):
#
# df_us_states = {
#     'cases': _cases_by_state(df_us['cases']),
#     'deaths': _cases_by_state(df_us['deaths']),
#     'recovered': _cases_by_state(df_us['recovered']),
# }
# pickle_file = open('pickles/df_us_states.p', 'wb')
# pickle.dump(df_us_states, pickle_file)

pickle_file = open('pickles/df_us.p', 'wb')
pickle.dump(df_us, pickle_file)


print('Updated pickles file pickles/df_us.p')