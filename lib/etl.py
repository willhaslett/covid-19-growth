import pandas as pd
from operator import itemgetter

# For now, just working with the confirmed cases CSV
# This file is intended to only setup the initial dataframe, with optional regional filtering. Import the dataframe to your downstream files as:
#     from etl import df_us # and/or df_regional

# TODO: the other regions
REGIONS = {
    'NE': ['ME', 'NY', 'NJ', 'VT', 'MA', 'RI', 'CT', 'NH', 'PA'],
    'SE': ['SC', 'VA', 'WV', 'NC', 'MS', 'AR', 'TN', 'FL', 'GA', 'AL', 'KY', 'LA'],
}

# df_all: All raw data converted to long format with dates as Pandas timestamps
#####################################################################################
df_all = pd.read_csv('confirmed_cases.csv')
date_cols = df_all.filter(regex=('^\d+/\d+/\d+$')).columns.array
df_all = pd.melt(df_all, id_vars=['Province/State', 'Country/Region', 'Lat',
                                  'Long'], value_vars=date_cols, var_name='date', value_name='cases')
df_all.date = pd.to_datetime(df_all.date, format='%m/%d/%y')
df_all['int_date'] = df_all.date.map(lambda date: 10000*date.year + 100*date.month + date.day)

# df_us: Filter out non-US, rename columns, split state into column
#####################################################################################
df_us = df_all[df_all['Country/Region'] == 'US'].reset_index()
df_us = df_us.drop(columns='Country/Region')
df_us = df_us.rename(
    columns={'Province/State': 'city_county', 'Lat': 'lat', 'Long': 'long'})
df_us.city_county, df_us['state'] = itemgetter(
    0, 1)(df_us.city_county.str.split(', ').str)

# df_regional: A dict of US dataframes by region
#####################################################################################
def for_region(state_list):
    return df_us[df_us.state.isin(state_list)]

df_regional = {
    'NE': (for_region(REGIONS['NE'])).reset_index(),
    'SE': (for_region(REGIONS['SE'])).reset_index(),
}