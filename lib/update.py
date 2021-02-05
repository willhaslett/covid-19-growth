import pandas as pd
import c19all
import dump_csv_and_json


# Exmple function calls, the first of which will trigger a full update of the data locally
# If you are going to work with the resulting dataframes (see README) *within* python, your
# workflow is to run this once, then import the Pickle files to do downstream work
c19all.for_country(c19all.df_all['cases'], 'France')
c19all.for_province_state(c19all.df_all['cases'], 'British Columbia')

print('Output Pickle, CSV and JSON files are up-to-date. For further work in Pyhon, import the Pickles!')
