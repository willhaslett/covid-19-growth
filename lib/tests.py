import pandas as pd
from pprint import pprint as pp
import etl

print("\nCases (head):")
pp(etl.df_cases.head())

print("\nDeaths (head):")
pp(etl.df_deaths.head())

print("\nRecovered (head):")
pp(etl.df_recovered.head())

print("\nCases for one country (head):")
pp(etl.for_country(etl.df_cases, 'France').head())

print("\nCases for one province_state (head):")
pp(etl.for_province_state(etl.df_cases, 'British Columbia').head())

print("\nTests passed")
