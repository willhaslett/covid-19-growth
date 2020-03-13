import pickle
import etl

dfs = ['df_cases', 'df_deaths', 'df_recovered']
for df in dfs:
    pickle_file = open(f'pickles/{df}.p','wb')
    pickle.dump(eval('etl.' + df), pickle_file)