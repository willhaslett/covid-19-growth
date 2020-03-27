import pandas as pd
import pickle
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
    return pd_date.strftime('%Y-%m-%d')

date_range = pd.date_range(start=constants.DAILY_START_DATE, end=pd.to_datetime('today')).tolist()
date_range = [date.strftime('%Y-%m-%d') for date in date_range]
print(date_range)











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