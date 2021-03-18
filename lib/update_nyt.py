import pandas as pd
import numpy as np
import pickle
import c19us_nyt

# For options, see https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html
JSON_ORIENT = 'table'

# For not-minified JSON, set to > 0
JSON_INDENT = 0

DATAFRAMES = {
    'df_us_nyt':  c19us_nyt.df_us.reset_index(),
}

for filename in DATAFRAMES:
    DATAFRAMES[filename].to_csv(f'output/csv/{filename}.csv', index=False)
    DATAFRAMES[filename].to_json(f'output/json/{filename}.json', orient=JSON_ORIENT, indent=JSON_INDENT)

print('Updated CSV files with New York Times data')
print('Updated JSON files with New York Times data')
