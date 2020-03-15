import pickle
import c19all
import c19us 

dfs = [
    {'name': 'c19_all', 'df': c19all.df_all},
    {'name': 'c19_us', 'df': c19us.df_us},
    {'name': 'c19_us_state', 'df': c19us.df_us_state},
    {'name': 'c19_us_county', 'df': c19us.df_us_county},
]

for df_dict in dfs:
    pickle_file = open(f'pickles/{df_dict["name"]}.p', 'wb')
    pickle.dump(df_dict['df'], pickle_file)