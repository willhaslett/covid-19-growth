import pickle
import c19all 

pickle_file = open('pickles/c19_all.p', 'wb')
pickle.dump(c19all.df_all, pickle_file)
print('Updated pickle file for global data pickles/c19all.p')