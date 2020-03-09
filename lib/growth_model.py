# Pip
import pprint
import pandas as pd
from scipy.optimize import curve_fit

# Local
from etl import df_us
from models import ggrowth

pp = pprint.pprint

# Starting with the Northeast region
REGION = 'NE'
# Group by date and sum
df = df_us.groupby('int_date').sum().reset_index()
# Keep only the 2d vector of interest
df = df[['int_date', 'cases']]

# Scipy wants Numpy arrays
np_array = df.to_numpy()
dates = np_array[:, 0]
case_counts = np_array[:, 1]

popt, pcov = curve_fit(ggrowth, dates, case_counts)

# Print model coefficients
print(case_counts)