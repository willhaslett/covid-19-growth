from pprint import pprint as pp
import pandas as pd
import matplotlib.pyplot as plt
from lmfit import Model
from etl import df_us

# TODO: implement or delete file

# def ggrowth(x, r, m, c0):
#     # Generalized growth https://www.sciencedirect.com/science/article/pii/S1755436516000037
#     a = c0 ** (1/m)
#     return ((r/m) * x + a) ** m