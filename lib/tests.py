import pandas as pd
from pprint import pprint as pp
import etl

print("\nCases:")
pp(etl.df_cases.head())

print("\nDeaths:")
pp(etl.df_deaths.head())

print("\nRecovered:")
pp(etl.df_recovered.head())

# print("\nCases for one country:")
# pp(etl.for_country('France').head())
# 
# print("\nCases for one province_state:")
# pp(etl.for_province_state('British Columbia').head())
# 
# print("\nTests passed")
