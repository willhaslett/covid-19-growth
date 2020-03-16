import pickle
import c19all
import c19us 

_dicts = [
    {'name': 'c19_all', 'dict': c19all.df_all},
    {'name': 'c19_us', 'dict': c19us.df_us},
]

for _dict in _dicts:
    pickle_file = open(f'pickles/{_dict["name"]}.p', 'wb')
    pickle.dump(_dict['dict'], pickle_file)

print('Updated pickle files')