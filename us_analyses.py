import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import pickle

# Choosing a set of dataframes
pickle_name = 'df_us'

# Choosing a data type
df_type = 'cases'

pickle_file = open(f'../pickles/{pickle_name}''.p', 'rb')
df= pickle.load(pickle_file)[df_type]
pickle_file.close()
df = df[['day', 'cases']]
df.groupby('day').sum()
print(df.index)
exit()
day, cases = df.day.to_numpy(), df.cases.to_numpy()
mpl.style.use('dark_background')
plt.plot(day, cases)
plt.show()
df = df[['day', 'cases']]
df.groupby('day').sum()
df.set_index(['day'])
print(df.index)
exit()
day, cases = numpy_array[0], numpy_array[1]
mpl.style.use('dark_background')
plt.plot(day, cases)
plt.show()
