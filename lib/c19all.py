import pandas as pd
from operator import itemgetter
import constants

# Global data, long format, dates as Pandas timestamps
#   `df_cases` All global cases
#   `df_deaths` All global deaths
#   `df_recovered` All global recoveries
#   `df_all` A dictionary containing the above three dataframes

# Data manipulation functions
#   `filter(df, column, vlaue)` Generic filter
#   `for_country(df, country)` Filter by country
#   `for_province_state(df, province_state)` Filter by province_state
#   `sum_by_date(df)` Group by date and sum case counts 

# Perform ETL on a Johns Hopkins COVID-19 CSV file, Returning a dataframe
def df_from_csv(file_name):
    df = pd.read_csv(file_name)
    df = df.rename(columns=constants.RENAMED_COLUMNS)
    date_cols = df.filter(regex=('^\d+/\d+/\d+$')).columns.array
    df = pd.melt(df, id_vars=['province_state', 'country', 'lat',
                                      'long'], value_vars=date_cols, var_name='date', value_name='cases')
    df.date = pd.to_datetime(df.date, format='%m/%d/%y')
    df['day'] = (df.date - pd.to_datetime(df.date.iloc[0])).astype('timedelta64[D]')
    df.day = df.day.apply(lambda day: int(round(day)))
    return df[['date', 'day', 'cases', 'province_state', 'country', 'lat', 'long']]

# General purpose filter.
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

# Dictionary containing dataframes for all global data
df_all = {
    'cases': df_from_csv('csv/confirmed_cases.csv'),
    'deaths': df_from_csv('csv/deaths.csv'),
    'recovered': df_from_csv('csv/recovered_cases.csv')
}

print(df_all['cases'])

# NOTE: These are deprecated. Use df_all.
df_cases = df_all['cases']
df_deaths = df_all['deaths'] 
df_recovered = df_all['recovered'] 
