import pandas as pd
import pickle
from c19us_jh import df_us as df_jh
from c19us_nyt import df_us as df_nyt

''' Merged Johns Hopkins and New York Times US county-level data. '''

df_us =  df_nyt

pickle_file = open('output/pickles/df_us_combined.p', 'wb')
pickle.dump(df_us, pickle_file)
print('Updated pickle file df_us_combined.p with Johns Hopkins and New York Times data')