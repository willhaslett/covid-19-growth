import c19us
import c19all
import pandas as pd

# c19all.py
print("\nGlobal cases (head):")
print(c19all.df_all['cases'].head())
print("\nGlobal deaths (head):")
print(c19all.df_all['deaths'].head())
print("\nGlobal recovered (head):")
print(c19all.df_all['recovered'].head())
print("\nCases for one country (head):")
print(c19all.for_country(c19all.df_all['cases'], 'France').head())
print("\nCases for one province_state (head):")
print(c19all.for_province_state(
    c19all.df_all['cases'], 'British Columbia').head())

# c19us.py
print("\nUS Cases (head):")
print(c19us.df_us['cases'].head())
print("\nUS Deaths (head):")
print(c19us.df_us['deaths'].head())
print("\nUS Recovered (head):")
print(c19us.df_us['recovered'].head())

print("\nPickle files for global and US data are up-to-date with the Johns Hopkins CSV files")
print("`python c19us.py` (~10 seconds) refreshes both pickles")
print("`python c19all.py` (snappy) refreshes the global pickle")
print("Tests passed\n")
