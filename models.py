from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://Alberto:96321jva@cluster0.nfpp4.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["db_hobbies_app"]
    except ConnectionError:
        print('Error de conexión con la base de datos')
    return db
