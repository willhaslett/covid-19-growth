# Pip
import pprint
import pandas as pd
from scipy.optimize import least_squares

# Local
from etl import df_regional
from etl import df_us
from models import ggrowth

pp = pprint.pprint

df = df_regional['NE'].groupby('int_date').sum().reset_index()
df = df[['int_date', 'cases']]

pp(df)