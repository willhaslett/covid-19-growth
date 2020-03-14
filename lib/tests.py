import pandas as pd
from pprint import pprint as pp
import etl
import us

# etl.py
print("\nCases (head):")
pp(etl.df_all['cases'].head())
print("\nDeaths (head):")
pp(etl.df_all['deaths'].head())
print("\nRecovered (head):")
pp(etl.df_all['recovered'].head())
print("\nCases for one country (head):")
pp(etl.for_country(etl.df_all['cases'], 'France').head())
print("\nCases for one province_state (head):")
pp(etl.for_province_state(etl.df_all['cases'], 'British Columbia').head())

#us.py
print("\nUS Cases (head):")
pp(us.df_us['cases'].head())
print("\nUS Deaths (head):")
pp(us.df_us['deaths'].head())
print("\nUS Recovered (head):")
pp(us.df_us['recovered'].head())
print("\nUS Cases by state (head):")
pp(us.df_us_states['cases'].head())
print("\nUS Deaths by state (head):")
pp(us.df_us_states['deaths'].head())
print("\nUS Recovered by state(head):")
pp(us.df_us_states['recovered'].head())

print("\nTests passed")
