import pandas as pd
import urllib
import c19all
import constants

""" Exposes df_us, a dictionary with dataframes holding all US county-level data
     df_us = {
         'cases': <all US cases dataframe>,
         'deaths': <all US deaths dataframe>
         'recovered': <all US recoveries dataframe>
         'active': <all US active cases dataframe>
     }
"""

def date_to_str(pd_date):
    return pd_date.strftime('%m-%d-%Y')

date_range = pd.date_range(start=constants.DAILY_START_DATE, end=pd.to_datetime('today')).tolist()
date_range = [date.strftime('%m-%d-%Y') for date in date_range]
daily_dfs = {}
for date in date_range:
    url = constants.DATA_URLS['daily'].replace('##-##-####', date)
    response =  urllib.request.urlopen(url)
    if response.code == 200:
        daily_dfs[date] = pd.read_csv(url)

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