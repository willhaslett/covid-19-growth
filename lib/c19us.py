import pandas as pd
import urllib
import math
import c19all
import constants

COUNTIES = constants.COUNTIES

FIPS = COUNTIES.keys()

DATE_RANGE = pd.date_range(start=constants.DAILY_START_DATE, end=pd.to_datetime('today')).tolist()

output_columns = [
    'date',
    'day', # since 2020-01-22
    'fips',
    'region',
    'sub_region',
    'state',
    'county',
    'lat',
    'long',
    'confirmed',
    'deaths',
    'recovered',
    'active',
]

_df_us = pd.DataFrame(columns=output_columns)

def df_from_daily_report(url):
    df = pd.read_csv(url)[['FIPS', 'Confirmed', 'Deaths', 'Recovered', 'Active']]
    df = df.rename(columns=constants.RENAMED_COLUMNS['daily_reports'])
    return df.loc[df.fips.isin(FIPS)]

dfs = []
for date in DATE_RANGE:
    url = constants.DATA_URLS['daily'].replace('##-##-####', date.strftime('%m-%d-%Y'))
    try:
        response =  urllib.request.urlopen(url)
    except urllib.error.HTTPError:
        break
    else:
        dfs.append(df_from_daily_report(url))

print(dfs)