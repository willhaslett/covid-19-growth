import pandas as pd
from operator import itemgetter
import constants

# Exposes
#   df_all: All raw data converted to long format with dates as Pandas timestamps
#   for_country()
#   for_province_state()
#   sum_by_date()

# df_all
_df_all = pd.read_csv('confirmed_cases.csv')
_df_all = _df_all.rename(columns=constants.RENAMED_COLUMNS)
_date_cols = _df_all.filter(regex=('^\d+/\d+/\d+$')).columns.array
_df_all = pd.melt(_df_all, id_vars=['province_state', 'country', 'lat',
                                  'long'], value_vars=_date_cols, var_name='date', value_name='cases')
_df_all.date = pd.to_datetime(_df_all.date, format='%m/%d/%y')
_df_all['day'] = (_df_all.date - pd.to_datetime(_df_all.date.iloc[0])).astype('timedelta64[D]')
df_all = _df_all

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