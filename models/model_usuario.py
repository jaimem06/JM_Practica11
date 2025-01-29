from pymongo import MongoClient
import uuid
from config import MONGODB_URI, MONGODB_DB

client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000, tls=True)
db = client[str(MONGODB_DB)]
usuarios_collection = db['usuarios']

class Usuario:
    def __init__(self, nombre, apellido, correo, contraseña, ubicacion, external_id=None, estado=True):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contraseña = contraseña
        self.ubicacion = ubicacion
        self.external_id = external_id or str(uuid.uuid4())
        self.estado = estado

    def save(self):
        usuario_data = {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "correo": self.correo,
            "contraseña": self.contraseña,
            "ubicacion": self.ubicacion,
            "external_id": self.external_id,
            "estado": self.estado
        }
        result = usuarios_collection.insert_one(usuario_data)
        return str(result.inserted_id)