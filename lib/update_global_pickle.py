import pickle
import c19all 

pickle_file = open('pickles/df_all.p', 'wb')
pickle.dump(c19all.df_all, pickle_file)
print('Updated pickle file pickles/df_all.p for global data')