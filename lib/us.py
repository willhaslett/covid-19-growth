import pandas as pd
from operator import itemgetter
import etl

from pprint import pprint as pp

# US records:
# 3 dataframes (df_cases_us, df_deaths_us, df_recoveries_us) with a state abbreviation column added for city/county level data.
# ollected in the dictionary `df_us`

# US state-level records:
# As above, filtered on state-level records only
# Collected in the dictionary `df_us_states`

# US population dataframe
#   `df_population_us` 

# NOTE: The process of splitting out state abbreviations from the province_state column is destructive 
#       for that column
# Split province_state on the string ', ' creating new columns 'is_state' and 'state'
def us_data(df):
    df = df.rename(columns={'province_state': 'state'})
    # For consistency with census data
    df.state = df.state.apply(lambda state: (state, 'District of Columbia') [state == 'Washington, D.C.'])
    df.state, df['state_abbrev'] = itemgetter(0, 1)(df.state.str.split(', ').str)
    return df

# Only state-level data. The df_us_states dictionary contains all US data, passed through this. Returns
#   state
#   cases
def state_level_only(df):
    df = df[df['state'].isin(df_us_population['state'])]
    return df[['state', 'cases']]

def population_for_state(state_name):
    return df_us_population[df_us_population.state == state_name].iloc[0].population_2019

# US population
df_us_population = pd.read_csv('csv/us_population.csv')

# US data
df_cases_us = us_data(etl.for_country(etl.df_cases, 'US'))
df_deaths_us = us_data(etl.for_country(etl.df_deaths, 'US'))
df_recovered_us = us_data(etl.for_country(etl.df_recovered, 'US'))

# Dict of all US data
df_us = {
    'cases': df_cases_us,
    'deaths': df_deaths_us,
    'recovered': df_recovered_us
}

# Dict of state-level data
df_us_states = {
    'cases': state_level_only(df_us['cases']),
    'deaths': state_level_only(df_us['deaths']),
    'recovered': state_level_only(df_us['recovered']),
}