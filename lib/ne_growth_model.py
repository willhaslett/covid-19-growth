# Pip
import pprint
import pandas as pd
from scipy.optimize import least_squares as ls

# Local
from etl import df_regional
from models import ggrowth

df = df_regional['NE'].groupby('date').sum().reset_index()
df = df[['int_date', 'cases']]

pp = pprint.pprint

pp(df)