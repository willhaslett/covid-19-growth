import pandas as pd
import pickle

df = pickle.load(open('pickles/c19_us.p', 'rb'))['cases']

print(df)