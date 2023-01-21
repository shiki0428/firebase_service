import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("config/serviceAccountKey.json") # ダウンロードした秘密鍵
firebase_admin.initialize_app(cred)

db = firestore.client()
docs = db.collection('users').get()
for doc in docs:
    print(doc.to_dict())