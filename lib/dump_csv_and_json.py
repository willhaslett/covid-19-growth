import c19all
import c19us_jh
import c19us_nyt
import c19us_combined
import pandas as pd

""" Generates CSV and JSON files for all available dataframes """

# For options, see https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html
JSON_ORIENT = 'table'

# For minified JSON, set to 0
JSON_INDENT = 2

DATAFRAMES = {
    'df_all_cases':   c19all.df_all['cases'],
    'df_all_deaths':  c19all.df_all['deaths'],
    'df_us_jh':       c19us_jh.df_us,
    'df_us_nyt':      c19us_nyt.df_us,
    'df_us_combined': c19us_combined.df_us,
}

for filename in DATAFRAMES:
    DATAFRAMES[filename].to_csv(f'output/csv/{filename}.csv', index=False)
    DATAFRAMES[filename].to_json(f'output/json/{filename}.json', orient=JSON_ORIENT, indent=JSON_INDENT)

print('Updated CSV files')
print('Updated JSON files')
