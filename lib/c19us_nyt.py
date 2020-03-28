import pandas as pd
import numpy as np
import urllib
import math
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
for column in county_columns:
    df[column] = df.apply(
        lambda row: counties.loc[column, str(row['fips'])], axis=1)
df = df[output_columns]
print(df)