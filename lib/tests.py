print("\nTakes a couple of minutes because the US data parser has a lot to do")
print("When this finishes, `/pickes/df_us.p` will be up-to-date with the Johns Hopkins repo")
print("To update the US data at any time: `python c19us.py`\n")
import pandas as pd
import c19all
import c19us

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
print(c19all.for_province_state(c19all.df_all['cases'], 'British Columbia').head())

# c19us.py
print("\nUS Cases (head):")
print(c19us.df_us['cases'].head())
print("\nUS Deaths (head):")
print(c19us.df_us['deaths'].head())
print("\nUS Recovered (head):")
print(c19us.df_us['recovered'].head())

print("\nTests passed")
