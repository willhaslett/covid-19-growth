import pandas as pd
from pprint import pprint as pp
import all
import us

# all.py
print("\nCases (head):")
pp(all.df_all['cases'].head())
print("\nDeaths (head):")
pp(all.df_all['deaths'].head())
print("\nRecovered (head):")
pp(all.df_all['recovered'].head())
print("\nCases for one country (head):")
pp(all.for_country(all.df_all['cases'], 'France').head())
print("\nCases for one province_state (head):")
pp(all.for_province_state(all.df_all['cases'], 'British Columbia').head())

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
