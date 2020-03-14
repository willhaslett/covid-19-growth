import pickle
import c19all
import c19us 

dfs = [
    {'name': 'df_c19all', 'df': c19all.df_all},
    {'name': 'df_c19us', 'df': c19us.df_us},
    {'name': 'df_c19us_state', 'df': c19us.df_us_state},
    {'name': 'df_c19us_county', 'df': c19us.df_us_county},
]

for df_dict in dfs:
    pickle_file = open(f'pickles/{df_dict["name"]}.p', 'wb')
    pickle.dump(df_dict['df'], pickle_file)
