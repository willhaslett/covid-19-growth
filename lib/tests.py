import pandas as pd
from pprint import pprint as pp
import c19all
import c19us

# all.py
print("\nCases (head):")
pp(c19all.df_all['cases'].head())
print("\nDeaths (head):")
pp(c19all.df_all['deaths'].head())
print("\nRecovered (head):")
pp(c19all.df_all['recovered'].head())
print("\nCases for one country (head):")
pp(c19all.for_country(c19all.df_all['cases'], 'France').head())
print("\nCases for one province_state (head):")
pp(c19all.for_province_state(c19all.df_all['cases'], 'British Columbia').head())

#us.py
print("\nUS Cases (head):")
pp(c19us.df_us['cases'].head())
print("\nUS Deaths (head):")
pp(c19us.df_us['deaths'].head())
print("\nUS Recovered (head):")
pp(c19us.df_us['recovered'].head())
print("\nUS Cases by state (head):")
pp(c19us.df_us_states['cases'].head())
print("\nUS Deaths by state (head):")
pp(c19us.df_us_states['deaths'].head())
print("\nUS Recovered by state(head):")
pp(c19us.df_us_states['recovered'].head())

print("\nTests passed")
