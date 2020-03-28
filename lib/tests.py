import pandas as pd
import c19all
import dump_csv_and_json

# importing dump_csv_and_json tests the creation of all outputs with the latest data

# Check public functions
c19all.for_country(c19all.df_all['cases'], 'France')
c19all.for_province_state(c19all.df_all['cases'], 'British Columbia')

print('Tests passed')
