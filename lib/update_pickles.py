import pickle
import etl
import us

dfs = [
    {'name': 'df_all', 'df': etl.df_all},
    {'name': 'df_us', 'df': us.df_us},
    {'name': 'df_us_states', 'df': us.df_us_states},
]

for df_dict in dfs:
    pickle_file = open(f'pickles/{df_dict["name"]}.p', 'wb')
    pickle.dump(df_dict['df'], pickle_file)