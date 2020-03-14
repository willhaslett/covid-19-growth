import pickle
import etl
import us

# Pickles are written for Jupyter, which is sometimes unhappy about importing local .py files

dfs = [
    {'name': 'df_cases', 'df': etl.df_cases},
    {'name': 'df_deaths', 'df': etl.df_deaths},
    {'name': 'df_recovered', 'df': etl.df_recovered},
    {'name': 'df_cases_us', 'df': us.df_cases_us},
    {'name': 'df_deaths_us', 'df': us.df_deaths_us},
    {'name': 'df_recovered_us', 'df': us.df_recovered_us},
    {'name': 'df_population_us', 'df': us.df_population_us}
]

for df_dict in dfs:
    pickle_file = open(f'pickles/{df_dict["name"]}.p', 'wb')
    pickle.dump(df_dict["df"], pickle_file)
