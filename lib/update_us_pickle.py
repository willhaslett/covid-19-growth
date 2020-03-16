import pickle
print('This will take a couple of minutes due to parsing of the US data')
import c19us 

pickle_file = open('pickles/c19_us.p', 'wb')
pickle.dump(c19us.df_us, pickle_file)
print('Updated pickle file for US data pickles/c19us.p')