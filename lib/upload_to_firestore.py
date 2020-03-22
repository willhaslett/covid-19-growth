import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd
import pickle

# Create database client
cred = credentials.Certificate('.google_service_account_key.json')
firebase_admin.initialize_app(cred, {
  'projectId': 'covidlocal',
})
db = firestore.client()

df_type = 'cases'
pickle_name = 'df_us_region_and_state'
pickle_file = open(f'output/pickles/{pickle_name}''.p', 'rb')
df = pickle.load(pickle_file)[df_type]
pickle_file.close()
df = df.loc[df['day'] > 57]

def row_to_document(row):




  # doc_ref = db.collection('users').document('alovelace')
  # doc_ref.set({
  #     'first': 'Tony',
  #     'last': 'Lovelace',
  #     'born': 1815
  # })