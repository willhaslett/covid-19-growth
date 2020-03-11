import pandas as pd
from operator import itemgetter

# Exposes
#   df_all: All raw data converted to long format with dates as Pandas timestamps
#   df_us: Filter out non-US, rename columns, split state into column
#   for_states()
#   sum_by_date()

# df_all
df_all = pd.read_csv('confirmed_cases.csv')
_date_cols = df_all.filter(regex=('^\d+/\d+/\d+$')).columns.array
df_all = pd.melt(df_all, id_vars=['Province/State', 'Country/Region', 'Lat',
                                  'Long'], value_vars=date_cols, var_name='date', value_name='cases')
df_all.date = pd.to_datetime(df_all.date, format='%m/%d/%y')
df_all['day'] = df_all['days_since'] = (df_all.date - pd.to_datetime(df_all.date.iloc[0])).astype('timedelta64[D]')

# df_us
df_us = df_all[df_all['Country/Region'] == 'US'].reset_index()
df_us = df_us.drop(columns='Country/Region')
df_us = df_us.rename(
    columns={'Province/State': 'city_county', 'Lat': 'lat', 'Long': 'long'})
df_us.city_county, df_us['state'] = itemgetter(
    0, 1)(df_us.city_county.str.split(', ').str)

def for_states(state_list):
    return df_us[df_us.state.isin(state_list)].reset_index()

def sum_by_date(df):
    return df.groupby('date').sum().reset_index()