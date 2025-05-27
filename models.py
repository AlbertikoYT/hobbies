from pymongo import MongoClient
import certifi
import os

MONGO_URI = os.environ.get('MONGO_URI')
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)  # <- IMPORTANTE
        db = client["db_hobbies_app"]
        return db
    except Exception as e:
        print("Error de conexión:", e)
        return None
