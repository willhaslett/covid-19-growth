import pandas as pd
import urllib
import math
import c19all
import constants

DATE_RANGE = pd.date_range(start=constants.DAILY_START_DATE, end=pd.to_datetime('today')).tolist()

def df_from_daily_report(url):
    df = pd.read_csv(url)[['FIPS', 'Confirmed', 'Deaths', 'Recovered', 'Active']]
    df = df.rename(columns=constants.RENAMED_COLUMNS['daily_reports'])
    # Remove problematic records
    df = df.loc[~df.fips.isnull()]
    return df

daily_dfs = {}
for date in DATE_RANGE:
    filename_date = date.strftime('%m-%d-%Y')
    iso_8601_date = date.strftime('%Y-%m-%d') 
    url = constants.DATA_URLS['daily'].replace('##-##-####', filename_date)
    try:
        response =  urllib.request.urlopen(url)
    except urllib.error.HTTPError:
        break
    else:
        daily_dfs[iso_8601_date] = df_from_daily_report(url)

print(daily_dfs)


_output_columns = [
    'date',
    'day',
    'fips'
    'region',
    'sub_region',
    'state',
    'county',
    'lat',
    'long',
    'population',
    'cases',
]