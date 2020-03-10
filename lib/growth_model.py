# Pip
import pprint
import pandas as pd
from scipy.optimize import curve_fit

# Local
from etl import df_us
from models import ggrowth, egrowth

pp = pprint.pprint

# Starting with the Northeast region
REGION = 'NE'
df = df_us.groupby('day').sum().reset_index()
df = df[['day', 'cases']]

# Scipy wants Numpy arrays
np_array = df.to_numpy()
days = np_array[:, 0]
case_counts = np_array[:, 1]

popt, pcov = curve_fit(egrowth, days, case_counts)