import pandas as pd
from urllib import error, request
import math
import constants

''' US county-level data from the Johns Hopkins files. '''

counties = pd.DataFrame(constants.COUNTIES)
fips = constants.COUNTIES.keys()

DATE_RANGE = pd.date_range(
    start=pd.to_datetime(constants.JH_START_DATE),
    end=pd.to_datetime('today')
).tolist()

county_columns = [
    'county',
    'state',
    'sub_region',
    'region',
    'lat',
    'long',
]

output_columns = [
    'date',
    'day',
    'county',
    'state',
    'sub_region',
    'region',
    'lat',
    'long',
    'confirmed',
    'deaths',
    'recovered',
    'active'
]


def df_from_daily_report(date, url):
    df = pd.read_csv(
        url)[['FIPS', 'Confirmed', 'Deaths', 'Recovered', 'Active']]
    df = df.rename(columns=constants.JH_RENAMED_COLUMNS['daily_reports'])
    df = df.loc[df.fips.isin(fips)]
    df = df.astype({'fips': 'int32'})
    df['date'] = date
    df['day'] = (date - pd.to_datetime(constants.JH_START_DATE)).days
    for column in county_columns:
        df[column] = df.apply(
            lambda row: counties.loc[column, str(row['fips'])], axis=1)
    return df[output_columns]


dfs = []
for date in DATE_RANGE:
    url = constants.DATA_URLS['us']['jh'].replace(
        '##-##-####', date.strftime('%m-%d-%Y'))
    try:
        response = request.urlopen(url)
    except error.HTTPError:
        break
    else:
        dfs.append(df_from_daily_report(date, url))

df_us = pd.concat(dfs)
