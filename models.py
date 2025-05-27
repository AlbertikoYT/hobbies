from pymongo import MongoClient
import os
import certifi
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.environ.get("MONGO_URI")
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)  # <- esta línea es crucial
        db = client["db_hobbies_app"]
        return db
    except Exception as e:
        print("Error de conexión:", e)
        return None
