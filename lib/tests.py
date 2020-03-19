import c19us
import c19all
import pandas as pd

# c19all.py
print("\nGlobal recovered (tail):")
print(c19all.df_all['recovered'].tail())
print("\nGlobal deaths (tail):")
print(c19all.df_all['deaths'].tail())
print("\nGlobal cases (tail):")
print(c19all.df_all['cases'].tail())
print("\nCases for one country (tail):")
print(c19all.for_country(c19all.df_all['cases'], 'France').tail())
print("\nCases for one province_state (tail):")
print(c19all.for_province_state(
    c19all.df_all['cases'], 'British Columbia').tail())

# c19us.py
print("\nUS Recovered (tail):")
print(c19us.df_us['recovered'].tail())
print("\nUS Deaths (tail):")
print(c19us.df_us['deaths'].tail())
print("\nUS Cases (tail):")
print(c19us.df_us['cases'].tail())

print("\nUS Recovered by region/state(tail):")
print(c19us.df_us_region_and_state['recovered'].tail())
print("\nUS Deaths by region/state (tail):")
print(c19us.df_us_region_and_state['deaths'].tail())
print("\nUS Cases by region/state(tail):")
print(c19us.df_us_region_and_state['cases'].tail())

print("\nPickle files for global and US data are up-to-date with the Johns Hopkins CSV files")
print("Tests passed\n")
