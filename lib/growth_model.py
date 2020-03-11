from pprint import pprint as pp
import pandas as pd
import matplotlib.pyplot as plt
from lmfit import Model
from etl import df_us
import models

# Aggregated US data
_df = df_us.groupby('day').sum().reset_index()
_df = _df[['day', 'cases']]
pp(hasattr(_df, '__array__'))


# Pick a model. See models.py
model = models.lmodel
pp(model)
pp('parameter names: {}'.format(model.param_names))
pp('independent variables: {}'.format(model.independent_vars))
pp('')

result = model.fit(_df.cases, day=_df.day, m=1)
print(result.fit_report())

plt.plot(_df.day, _df.cases, 'bo')
plt.plot(_df, result.init_fit, 'k--', label='initial fit')
plt.plot(_df, result.best_fit, 'r-', label='best fit')
plt.legend(loc='best')
plt.show()