import pandas as pd
import pickle
from pprint import pprint as pp
import c19all
import constants


""" Creates `df_us`, a dictionary containing three dataframes, all of the same shape
    `cases` US confirmed cases
    `deaths` US deaths
    `recovered` US recoveries

    Takes about 10 seconds to run. After running once, use `pickles/df_us.p` instead of importing this module to avoid the wait 
"""

KNOWN_LOCATIONS = constants.US_LOCATIONS_IN_SOURCE
POPULATION = constants.US_POPULATION
STABBREVS = constants.US_STATE_ABBREVS


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


def _parse_location(row):
    location = row._location
    if location not in KNOWN_LOCATIONS:
        row.unkown_type = location
        print(f'Location {location} assigend as unkown_type. Update constants.US_LOCATIONS_IN_SOURCE')
        print('New locations found and assigned as unkown_type. constants.US_LOCATIONS_IN_SOURCE needs to be updated')
        return row
    if KNOWN_LOCATIONS[location] == 'state':
        row.is_state = True
        row.state = location
        row.sub_region = POPULATION[location]['sub_region']
        row.region = POPULATION[location]['region']
        row.population = int(round(POPULATION[location]['population']))
        return row
    row.is_state = False
    if KNOWN_LOCATIONS[location] == 'county':
        # TODO: Error trapping here
        county_and_abbrev = location.split(', ')
        row.county = county_and_abbrev[0].replace(' ', '')
        row.state = STABBREVS[county_and_abbrev[1].replace(' ', '')]
        return row
    if KNOWN_LOCATIONS[location] == 'territory':
        row.territory = location
        return row
    if KNOWN_LOCATIONS[location] == 'other':
        row.other = location
        return row
    print(f'Failed to parse {location} as known or unkown_type')
    raise ValueError('A very specific bad thing happened.')



def _handle_special_cases(df):
    """ Special case renaming of locations """
    # Merge names for the District of Columbia
    df.other = df.other.apply(lambda other: (
        other, 'District of Columbia')[other == 'Washington, D.C.'])
    # Remove U.S. from the Virgin Islands
    df.territory = df.territory.apply(lambda territory: (
        territory, 'Virgin Islands')[territory == 'Virgin Islands, U.S.'])
    return df


def _us_data(df):
    """ Produce output dataframe from raw JH data filtered on US records """
    df = df.rename(columns={'province_state': '_location'})
    df['state'] = None
    df['county'] = None
    df['territory'] = None
    df['other'] = None
    df['unknown_type'] = None
    df['is_state'] = None
    df['sub_region'] = None
    df['region'] = None
    df['population'] = None
    df = df.apply(lambda row: _parse_location(row), axis=1)
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

pickle_file = open('pickles/df_us.p', 'wb')
pickle.dump(df_us, pickle_file)
print("Updated pickle file pickles/df_us.p with all US data")


""" Output dictionary of dataframes grouped by state (county/state merged)
def _us_state_data(df):
  TODO

df_us_by_state = {
    'cases': _us_state_data(df_us['cases']),
    'deaths': _us_state_data(df_us['deaths']),
    'recovered': _us_state_data(df_us['recovered']),
}
pickle_file = open('pickles/df_us_by_state.p', 'wb')
pickle.dump(df_us_by_state, pickle_file)
print('Updated pickle file pickles/df_us_by_state.p with US data grouped by state')
"""
