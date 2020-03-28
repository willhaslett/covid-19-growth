import pandas as pd
import numpy as np
import pickle
from c19us_jhu import df_us as df_jhu
from c19us_nyt import df_us as df_nyt

''' Merged Johns Hopkins and New York Times US county-level data. '''

df_jhu = df_jhu[['cases', 'deaths', 'recovered', 'active']]
df_us = df_nyt.join(df_jhu, lsuffix='_nyt', rsuffix='_jhu')

pickle_file = open('output/pickles/df_us_combined.p', 'wb')
pickle.dump(df_us, pickle_file)
print('Updated pickle file df_us_combined.p with Johns Hopkins and New York Times data')
