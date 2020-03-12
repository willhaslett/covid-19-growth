import pprint
import pandas as pd
from pprint import pprint as pp
import etl

pp(etl.df_all)
pp(etl.for_country('France'))
pp(etl.for_province_state('British Columbia'))

# TODO: Actual tests