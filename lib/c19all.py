import pandas as pd
from operator import itemgetter
import pickle
import constants


""" Exposes df_all, a dictionary with dataframes holding all global time series data
     df_all = {
         'cases': <all global cases dataframe>,
         'deaths': <all global deaths dataframe>
     }

    Dataframe functions
    `filter(df, column, vlaue)` Generic filter
    `for_country(df, country)` Filter by country
    `for_province_state(df, province_state)` Filter by province_state
    `sum_by_date(df)` Group by date and sum case counts 
    `date_to_day(date)` Convert a date to the number of days since the date of the first records
    `day_to_date(day)` Convert a number of days since the first records to a date
"""

renamed_columns = constants.JHU_RENAMED_COLUMNS['time_series']

# Perform ETL on a Johns Hopkins COVID-19 time series file, Returning a dataframe
def df_from_csv(file_name):
    df = pd.read_csv(file_name)
    df = df.rename(columns=renamed_columns)
    date_cols = df.filter(regex=('^\d+/\d+/\d+$')).columns.array
    df = pd.melt(df, id_vars=['province_state', 'country', 'lat',
                                      'long'], value_vars=date_cols, var_name='date', value_name='cases')
    df.date = pd.to_datetime(df.date, format='%m/%d/%y')
    df['day'] = (df.date - pd.to_datetime(df.date.iloc[0])).astype('timedelta64[D]')
    df.day = df.day.apply(lambda day: int(round(day)))
    return df[['date', 'day', 'cases', 'province_state', 'country', 'lat', 'long']]

# General purpose filter
def filter(df, column, value):
    return df[df[column] == value].reset_index()

# Filter on country
def for_country(df, country):
    return filter(df, 'country', country)

# Filter on province_state. us.py has its own function for this
def for_province_state(df, province_state):
    return filter(df, 'province_state', province_state)

# Return input with all rows collapsed by date and cases summed
def sum_by_date(df):
    return df.groupby('date').sum().reset_index()

# Convert a date to the number of days since the date of the first records
def date_to_day(date):
    return (date - pd.to_datetime('2020-01-21')).days

# Convert a number of days since the first records to a date
def day_to_date(day):
    pd.to_datetime('2020-03-21') + pd.DateOffset(days=day)
    
_df_cases = df_from_csv(constants.DATA_URLS['global']['cases'])
_df_deaths = df_from_csv(constants.DATA_URLS['global']['deaths']).rename(columns={'cases': 'deaths'})

# Dictionary containing dataframes for all global data
df_all = {
    'cases': _df_cases,
    'deaths': _df_deaths
}

try:
    get_ipython
except:
    pickle_file = open('output/pickles/df_all.p', 'wb')
    pickle.dump(df_all, pickle_file)
    print('Updated pickle file df_all.p with global data')
