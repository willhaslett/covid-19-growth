import pandas as pd
import urllib
import math
import pickle
import constants

''' US county-level data from the New York Times files. '''

counties = pd.DataFrame(constants.COUNTIES)
fips = constants.COUNTIES.keys()
county_columns = constants.US_COUNTY_COLUMNS['nyt']
output_columns = constants.US_OUTPUT_COLUMNS['nyt']
start_date = constants.START_DATE['nyt']

df = pd.read_csv(constants.DATA_URLS['us']['nyt'])
df = df.loc[df.fips.isin(fips)]
df = df.astype({'fips': 'int32'})
df.date = pd.to_datetime(df.date)
df['start_date'] = pd.to_datetime(start_date)
df['day'] = (df.date - df.start_date).astype('timedelta64[D]')
df.day = df.day.astype('int')
for column in county_columns:
    df[column] = df.apply(
        lambda row: counties.loc[column, str(row['fips'])], axis=1)
df_us = df[output_columns].set_index(['date', 'fips'])

try:
    get_ipython
except:
    pickle_file = open('output/pickles/df_us_nyt.p', 'wb')
    pickle.dump(df_us, pickle_file)
    print('Updated pickle file df_us_nyt.p with New York Times data')
