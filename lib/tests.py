import pandas as pd
import c19us
import c19all
import dump_csv_and_json

# Check public functions
c19all.for_country(c19all.df_all['cases'], 'France')
c19all.for_province_state(c19all.df_all['cases'], 'British Columbia')

print("Tests passed\n")
