import pandas as pd
import pickle
from c19us_jhu import df_us as df_jhu
from c19us_nyt import df_us as df_nyt

''' Merged Johns Hopkins and New York Times US county-level data. '''

renamed_columns = {
    'jhu': {
        'cases': 'cases_jhu',
        'deaths': 'deaths_jhu',
        'recovered': 'recovered_jhu',
        'active': 'active_jhu',
    },
    'nyt': {
        'cases': 'cases_nyt',
        'deaths': 'deaths_nyt',
    },
}

df_jhu= df_jhu.rename(columns=renamed_columns['jhu'])
df_nyt= df_nyt.rename(columns=renamed_columns['nyt'])

print('JH --------------------------')
print(df_jhu)
print('NYT --------------------------')
print(df_nyt)

df_us =  df_nyt

pickle_file = open('output/pickles/df_us_combined.p', 'wb')
pickle.dump(df_us, pickle_file)
print('Updated pickle file df_us_combined.p with Johns Hopkins and New York Times data')