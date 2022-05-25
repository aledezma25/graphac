from ast import Try
import pymongo

MONGO_HOST="localhost"
MONGO_PORT="27017"
MONGO_TIEMPO_FUERA=1000

MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PORT+"/"

try:
    cliente=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
    cliente.server_info()
    print("Concexion a Mongo exitosa")
    cliente.close()
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo exedido"+errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mogobd"+errorConexion)