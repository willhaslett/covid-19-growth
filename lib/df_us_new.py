import pandas as pd
import pickle

# df = pd.DataFrame(data=pickle.load(open('pickles/c19_us.p', 'rb'))['cases'])
df = data=pickle.load(open('pickles/c19_us.p', 'rb'))['cases']

places = pd.DataFrame(df.state_county.unique())

places.to_csv('csv/foo.csv', index=False)