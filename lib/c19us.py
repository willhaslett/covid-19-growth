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

date_range = pd.date_range(start=constants.DAILY_START_DATE, end=pd.to_datetime('today'))
for date in date_range:
    date = date.strftime('%Y-%m-%d')
    print(date)











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