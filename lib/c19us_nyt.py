import pandas as pd
import urllib
import math
import constants

''' US county-level data from the New York Times files. '''

counties = pd.DataFrame(constants.COUNTIES)
fips = constants.COUNTIES.keys()

df = pd.read_csv(constants.DATA_URLS['us']['nyt'])
df = df.loc[df.fips.isin(fips)]
df = df.astype({'fips': 'int32'})

print(df)