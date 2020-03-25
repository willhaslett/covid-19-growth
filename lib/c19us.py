import pandas as pd
import pickle
import c19all
import constants


""" Creates two dictionaries of structured US data
    df_us()
        Contains case, death and recovery data by date with location type parsed into columns for each type
    df_region_and_state()
        Contains case, death, and recovery data by date, aggregated by state, with columns for US 2019 census region, sub_region, and population
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
    'unknown_type',
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
        KNOWN_LOCATIONS[location] = 'unkown_type'
        print(f'Location {location} assigend as unknown_type. Update constants.US_LOCATIONS_IN_SOURCE')
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
    if KNOWN_LOCATIONS[location] == 'unkown_type':
        row.unknown_type = location
        return row
    raise ValueError('Parsing location failed. Open a GitHub issue.')


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
    df['region'] = None
    df['sub_region'] = None
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


def _by_region_and_state(df):
    df = df[['date', 'region', 'sub_region', 'state', 'population', 'cases']]
    return df.groupby(['date', 'region', 'sub_region', 'state'], as_index=False).sum()


df_us_region_and_state = {
    'cases': _by_region_and_state(df_us['cases']),
    'deaths': _by_region_and_state(df_us['deaths']),
    'recovered': _by_region_and_state(df_us['recovered']),
}

# Optional pickle files

# pickle_file = open('output/pickles/df_us.p', 'wb')
# pickle.dump(df_us, pickle_file)
# print('Updated pickle file df_us.p')
# pickle_file = open('output/pickles/df_us_region_and_state.p', 'wb')
# pickle.dump(df_us, pickle_file)
# print('Updated pickle file df_us_region_and_state.p')
