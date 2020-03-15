import pandas as pd
from pprint import pprint as pp
import c19all
import c19us

# c19all.py
print("\nGlobal cases (head):")
pp(c19all.df_all['cases'].head())
print("\nGlobal deaths (head):")
pp(c19all.df_all['deaths'].head())
print("\nGlobal recovered (head):")
pp(c19all.df_all['recovered'].head())
print("\nCases for one country (head):")
pp(c19all.for_country(c19all.df_all['cases'], 'France').head())
print("\nCases for one province_state (head):")
pp(c19all.for_province_state(c19all.df_all['cases'], 'British Columbia').head())

# c19us.py
# National
print("\nUS Cases (head):")
pp(c19us.df_us_state['cases'].head())
print("\nUS Deaths (head):")
pp(c19us.df_us_state['deaths'].head())
print("\nUS Recovered (head):")
pp(c19us.df_us_state['recovered'].head())
# State
print("\nUS Cases by state (head):")
pp(c19us.df_us_state['cases'].head())
print("\nUS Deaths by state (head):")
pp(c19us.df_us_state['deaths'].head())
print("\nUS Recovered by state (head):")
pp(c19us.df_us_state['recovered'].head())
# County
print("\nUS Cases by county (head):")
pp(c19us.df_us_county['cases'].head())
print("\nUS Deaths by county (head):")
pp(c19us.df_us_county['deaths'].head())
print("\nUS Recovered by county (head):")
pp(c19us.df_us_county['recovered'].head())

print("\nTests passed")
