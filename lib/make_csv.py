import c19us
import c19all
import pandas as pd

""" Generates CSV files in csv_out for all available dataframes """

DATAFRAMES = {
    'df_all_cases':                     c19all.df_all['cases'],
    'df_all_deaths':                    c19all.df_all['deaths'],
    'df_all_recovered':                 c19all.df_all['recovered'],
    'df_us_cases':                      c19us.df_us['cases'],
    'df_us_deaths':                     c19us.df_us['deaths'],
    'df_us_recovered':                  c19us.df_us['recovered'],
    'df_us_region_and_state_cases':     c19us.df_us['cases'],
    'df_us_region_and_state_deaths':    c19us.df_us['deaths'],
    'df_us_region_and_state_recovered': c19us.df_us['recovered'],
}

for filename in DATAFRAMES:
    DATAFRAMES[filename].to_csv(f'csv_out/{filename}.csv')

print('Generated up-to-date CSV files')