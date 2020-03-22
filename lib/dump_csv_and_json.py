import c19us
import c19all
import pandas as pd

""" Generates CSV and JSON files for all available dataframes """

DATAFRAMES = {
    'df_all_cases':                     c19all.df_all['cases'],
    'df_all_deaths':                    c19all.df_all['deaths'],
    'df_all_recovered':                 c19all.df_all['recovered'],
    'df_us_cases':                      c19us.df_us['cases'],
    'df_us_deaths':                     c19us.df_us['deaths'],
    'df_us_recovered':                  c19us.df_us['recovered'],
    'df_us_region_and_state_cases':     c19us.df_us_region_and_state['cases'],
    'df_us_region_and_state_deaths':    c19us.df_us_region_and_state['deaths'],
    'df_us_region_and_state_recovered': c19us.df_us_region_and_state['recovered'],
}

for filename in DATAFRAMES:
    DATAFRAMES[filename].to_csv(f'output/csv/{filename}.csv')
    DATAFRAMES[filename].to_json(f'output/json/{filename}.json')

print('Updated CSV files')
print('Updated JSON files')
