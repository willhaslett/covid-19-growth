import pandas as pd
from urllib import error, request
import math
import pickle
import constants

''' US county-level data from the Johns Hopkins files. '''

counties = pd.DataFrame(constants.COUNTIES)
fips = constants.COUNTIES.keys()
county_columns = constants.US_COUNTY_COLUMNS['jhu']
output_columns = constants.US_OUTPUT_COLUMNS['jhu']
start_date = constants.START_DATE['jhu']

DATE_RANGE = pd.date_range(
    start=pd.to_datetime(constants.START_DATE['jhu']),
    end=pd.to_datetime('today')
).tolist()

def df_from_daily_report(date, url):
    df = pd.read_csv( url)[['FIPS', 'Confirmed', 'Deaths', 'Recovered', 'Active']]
    df = df.rename(columns=constants.JHU_RENAMED_COLUMNS['daily_reports'])
    df = df.loc[df.fips.isin(fips)]
    df = df.astype({'fips': 'int32'})
    df['date'] = date
    df['day'] = (date - pd.to_datetime(start_date)).days
    for column in county_columns:
        df[column] = df.apply(
            lambda row: counties.loc[column, str(row['fips'])], axis=1)
    return df[output_columns].set_index('fips')

dfs = []
for date in DATE_RANGE:
    url = constants.DATA_URLS['us']['jhu'].replace(
        '##-##-####', date.strftime('%m-%d-%Y'))
    try:
        response = request.urlopen(url)
    except error.HTTPError:
        break
    else:
        dfs.append(df_from_daily_report(date, url))

df_us = pd.concat(dfs)

pickle_file = open('output/pickles/df_us_jhu.p', 'wb')
pickle.dump(df_us, pickle_file)
print('Updated pickle file df_us_jhu.p with Johns Hopkins data')