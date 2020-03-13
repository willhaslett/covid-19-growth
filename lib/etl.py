import pandas as pd
from operator import itemgetter
import constants

# Exposes
# `df_cases` All global cases, long format, dates as Pandas timestamps
# `df_deaths` All global deaths, long format, dates as Pandas timestamps
# `df_recovered` All global recoveries, long format, dates as Pandas timestamps
# `filter(df, column, vlaue)` Generic filter
# `for_country(df, country)` Filter by country
# `for_province_state(df, province_state)` Filter by province_state
# `sum_by_date(df)` Group by date and sum case counts 

# Perform ETL on a COVID-19 CSV file
def df_from_csv(file_name):
    _df = pd.read_csv(file_name)
    _df = _df.rename(columns=constants.RENAMED_COLUMNS)
    _date_cols = _df.filter(regex=('^\d+/\d+/\d+$')).columns.array
    _df = pd.melt(_df, id_vars=['province_state', 'country', 'lat',
                                      'long'], value_vars=_date_cols, var_name='date', value_name='cases')
    _df.date = pd.to_datetime(_df.date, format='%m/%d/%y')
    _df['day'] = (_df.date - pd.to_datetime(_df.date.iloc[0])).astype('timedelta64[D]')
    return _df

df_cases = df_from_csv('confirmed_cases.csv')
df_deaths = df_from_csv('deaths.csv')
df_recovered = df_from_csv('recovered_cases.csv')

# General purpose filter.
def filter(df, column, value):
    return df[df[column] == value].reset_index()

# Filter on country
def for_country(df, country):
    return filter(df, 'country', country)

# Filter on country province_state
def for_province_state(df, province_state):
    return filter(df, 'province_state', province_state)

# Split province_state on the string ', ' creating a new column 'state'
def state_to_col_destructive(df):
    df.province_state, df['state'] = itemgetter(
        0, 1)(df.province_state.str.split(', ').str)
    return df

# Return input with all rows collapsed by date and cases summed
def sum_by_date(df):
    return df.groupby('date').sum().reset_index()
