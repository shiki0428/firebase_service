import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("config/serviceAccountKey.json") # ダウンロードした秘密鍵
firebase_admin.initialize_app(cred)

db = firestore.client()

data = {"name": "Los Angeles"}
# Add a new doc in collection 'cities' with ID 'LA'
db.collection("users").document("LA").set(data,merge = True)