from pprint import pprint as pp
import pandas as pd
from scipy.optimize import curve_fit
from lmfit import Model
from constants import REGIONS as regions
from etl import df_us
import models

# Aggregated US data
_df = df_us.groupby('day').sum().reset_index()
_df = _df[['day', 'cases']]
pp(hasattr(_df, '__array__'))

model = models.lmodel
pp(model)
pp('parameter names: {}'.format(model.param_names))
pp('independent variables: {}'.format(model.independent_vars))
pp('')

params = model.make_params(m=1)
print(params)
print()

result = model.fit(_df.cases, day=_df.day, m=1)
pp(result)