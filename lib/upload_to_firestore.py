import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials
cred = credentials.Certificate('.google_service_account_key.json')

firebase_admin.initialize_app(cred, {
  'projectId': 'covidlocal',
})

db = firestore.client()
