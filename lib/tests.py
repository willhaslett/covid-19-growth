import pandas as pd
from pprint import pprint as pp
import etl

print("\nMain dataframe:")
pp(etl.df_all)

print("\nCases for one country:")
pp(etl.for_country('France'))

print("\nCases for one province_state:")
pp(etl.for_province_state('British Columbia').head())

print("\nTests passed")