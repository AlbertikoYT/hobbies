import os
from pymongo import MongoClient
import certifi

MONGO_URI = os.environ.get('MONGO_URI')  # <- viene desde Render
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["db_hobbies_app"]  # nombre de tu base
    except ConnectionError:
        print('Error de conexión con la base de datos')
    return db
