import pandas as pd
from operator import itemgetter
import constants

# Exposes
#   df_all: All raw data converted to long format with dates as Pandas timestamps
#   for_country()
#   for_province_state()
#   sum_by_date()

# df_cases
_df_cases = pd.read_csv('confirmed_cases.csv')
_df_cases = _df_cases.rename(columns=constants.RENAMED_COLUMNS)
_date_cols = _df_cases.filter(regex=('^\d+/\d+/\d+$')).columns.array
_df_cases = pd.melt(_df_cases, id_vars=['province_state', 'country', 'lat',
                                  'long'], value_vars=_date_cols, var_name='date', value_name='cases')
_df_cases.date = pd.to_datetime(_df_cases.date, format='%m/%d/%y')
_df_cases['day'] = (_df_cases.date - pd.to_datetime(_df_cases.date.iloc[0])).astype('timedelta64[D]')
df_cases = _df_cases

# df_deaths
_df_deaths = pd.read_csv('confirmed_cases.csv')
_df_deaths = _df_deaths.rename(columns=constants.RENAMED_COLUMNS)
_date_cols = _df_deaths.filter(regex=('^\d+/\d+/\d+$')).columns.array
_df_deaths = pd.melt(_df_deaths, id_vars=['province_state', 'country', 'lat',
                                  'long'], value_vars=_date_cols, var_name='date', value_name='cases')
_df_deaths.date = pd.to_datetime(_df_deaths.date, format='%m/%d/%y')
_df_deaths['day'] = (_df_deaths.date - pd.to_datetime(_df_deaths.date.iloc[0])).astype('timedelta64[D]')
df_deaths = _df_deaths

# df_recovered
_df_recovered = pd.read_csv('confirmed_cases.csv')
_df_recovered = _df_recovered.rename(columns=constants.RENAMED_COLUMNS)
_date_cols = _df_recovered.filter(regex=('^\d+/\d+/\d+$')).columns.array
_df_recovered = pd.melt(_df_recovered, id_vars=['province_state', 'country', 'lat',
                                  'long'], value_vars=_date_cols, var_name='date', value_name='cases')
_df_recovered.date = pd.to_datetime(_df_recovered.date, format='%m/%d/%y')
_df_recovered['day'] = (_df_recovered.date - pd.to_datetime(_df_recovered.date.iloc[0])).astype('timedelta64[D]')
df_recovered = _df_recovered

# General purpose filter.
def filter(column, value):
    return df_all[df_all[column] == value].reset_index()

# Filter on country
def for_country(country):
    return filter('country', country)

# Filter on country province_state
def for_province_state(province_state):
    return filter('province_state', province_state)

# Split province_state on the string ', ' creating a new column 'state'
def state_to_col_destructive(df):
    df.province_state, df['state'] = itemgetter(
        0, 1)(df.province_state.str.split(', ').str)
    return df

# Return input with all rows collapsed by date and cases summed
def sum_by_date(df):
    return df.groupby('date').sum().reset_index()

# Returns a dataframe summary
