import pandas as pd
from operator import itemgetter
import constants

# Exposes
#   df_all: All raw data converted to long format with dates as Pandas timestamps
#   df_us: Filter out non-US, rename columns, split state into column
#   for_states()
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

# df_us
_df_us = df_all[df_all['country'] == 'US'].reset_index()
_df_us = _df_us.drop(columns='country')
_df_us.province_state, _df_us['state'] = itemgetter(
    0, 1)(_df_us.province_state.str.split(', ').str)
df_us = _df_us

def for_states(state_list):
    return df_us[df_us.state.isin(state_list)].reset_index()

def sum_by_date(df):
    return df.groupby('date').sum().reset_index()