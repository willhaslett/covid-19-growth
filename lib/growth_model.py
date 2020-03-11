from pprint import pprint as pp
import pandas as pd
import matplotlib.pyplot as plt
from lmfit import Model
from etl import df_us
from models import LinearModel

_df = df_us.groupby('day').sum().reset_index()
model = LinearModel()
params = model.make_params()
result = model.fit(_df.day, params, x=_df.day.to_list())
print(result.fit_report())