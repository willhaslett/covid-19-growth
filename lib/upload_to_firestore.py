import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd
import pickle
import c19all
import c19us

# Be aware of Firestore pricing: https://firebase.google.com/docs/firestore/pricing
# If you run one or both of the uploads, the corresponding shell will be busy for aWHILE
# TODO:
#   Async
#   Incremental daily uploads 

# Create the database client
cred = credentials.Certificate('.google_service_account_key.json')
firebase_admin.initialize_app(cred, {
  'projectId': 'covidlocal',
})
db = firestore.client()

# Create Firestore documents from a dataframe
def create_documents(df, collection):
  records = df.to_dict('records')
  for record in records:
    doc = db.collection(collection).document()
    print(u'Creating doc {}'.format(doc.id))
    doc.set(record)

# Delete a collection. This does not work if there are sub-collections present
# https://firebase.google.com/docs/firestore/solutions/delete-collections
def delete_collection(coll_ref, batch_size=100):
    docs = coll_ref.limit(batch_size).stream()
    deleted = 0
    for doc in docs: 
        print(u'Deleting doc {}'.format(doc.id))
        doc.reference.delete()
        deleted = deleted + 1
    if deleted >= batch_size:
        return delete_collection(coll_ref, batch_size)

# Bulk uploads with all current data
# To upload a subset, filter first: df = df[df.country == 'Japan']
# create_documents(c19all.df_all['cases'], 'global-cases')
# create_documents(c19us.df_us_region_and_state['cases'], 'us-cases')

# Delete collections
# delete_collection(db.collection('global-cases'))
# delete_collection(db.collection('us-cases'))