from pprint import pprint as pp
import pandas as pd
from scipy.optimize import curve_fit

# Local
from etl import df_us
import models
from constants import REGIONS as regions

# Starting with the Northeast region
REGION = 'NE'
_df = df_us.groupby('day').sum().reset_index()
_df = _df[['day', 'cases']]

# Scipy wants Numpy arrays
_np_array = _df.to_numpy()
_day = _np_array[:, 0]
_cases = _np_array[:, 1]

# Choose model
model = models.lgrowth

# Fit model
popt, pcov = curve_fit(model, _day, _cases)

# Predicted case counts
pred_cases = _df.apply(model(_df.day, popt[0]), columns='cases')

pp(pred_cases)
