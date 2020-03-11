from pprint import pprint as pp
import pandas as pd
from scipy.optimize import curve_fit
from etl import df_us
import models
from constants import REGIONS as regions


# from lmfit import minimize, Parameters
# def residual(params, x, data, eps_data):
#     amp = params['amp']
#     phaseshift = params['phase']
#     freq = params['frequency']
#     decay = params['decay']
#     model = amp * sin(x*freq + phaseshift) * exp(-x*x*decay)
#     return (data-model) / eps_data
# params = Parameters()
# params.add('amp', value=10)
# params.add('decay', value=0.007)
# params.add('phase', value=0.2)
# params.add('frequency', value=3.0)
# out = minimize(residual, params, args=(x, data, eps_data))

# Choose model
model = models.lgrowth

# Starting with the Northeast region
REGION = 'NE'
_df = df_us.groupby('day').sum().reset_index()
_df = _df[['day', 'cases']]

# Scipy wants Numpy arrays
_np_array = _df.to_numpy()
_day = _np_array[:, 0]
_cases = _np_array[:, 1]

# Fit model
_model_parameters, _model_covariance = curve_fit(model, _day, _cases)

# Predicted case counts
pred_cases = _df.drop(['cases'], axis=1).applymap(
    lambda x: model(x, _model_parameters[0]))

pp(pred_cases)
