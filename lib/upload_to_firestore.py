import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd
from c19us_combined import df_us


# Be aware of Firestore pricing: https://firebase.google.com/docs/firestore/pricing
# TODO:
#   Async
#   Incremental daily uploads 

# Create the database client
cred = credentials.Certificate('.google_service_account_key.json')
firebase_admin.initialize_app(cred, {
  'projectId': 'your-firebase-project-id',
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
        
# Turn date and fips into columns
df_us = df_us.reset_index()

# Break up df_us into dfs for each date
dates = df_us.date.apply(lambda date: date.strftime('%Y-%m-%d')).unique().tolist()  
print(dates)

# Bulk uploads with all current data
# To upload a subset, filter first, e.g.: df = df[df.country == 'Japan']
# create_documents(c19all.df_all['cases'], 'global-cases')

# Delete collections
# delete_collection(db.collection('global-cases'))
