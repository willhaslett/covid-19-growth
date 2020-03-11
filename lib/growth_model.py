from pprint import pprint as pp
import pandas as pd
from scipy.optimize import curve_fit
from lmfit import Model
from constants import REGIONS as regions
from etl import df_us
import models

# Aggregated US data
_df = df_us.groupby('day').sum().reset_index().to_numpy()
_df = _df[['day', 'cases']]

# Choose model
model = models.lmodel
print()
print('parameter names: {}'.format(model.param_names))
print('independent variables: {}'.format(model.independent_vars))
print()
params = model.make_params()
pp(params)
print()
result = model.fit(_df, params)
pp(result)