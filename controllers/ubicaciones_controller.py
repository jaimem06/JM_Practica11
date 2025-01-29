from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from config import MONGODB_URI, MONGODB_DB
from bson import ObjectId

client = MongoClient(MONGODB_URI)
db = client[str(MONGODB_DB)]
ubicaciones_collection = db['ubicaciones']

api_ubicaciones = Blueprint('api_ubicaciones', __name__)

def agregar_poligono():
    data = request.get_json()
    nombre = data.get('nombre')
    geojson = data.get('geojson')

    if not nombre or not geojson:
        return jsonify({"error": "Faltan datos"}), 400

    poligono = {
        "_id": str(ObjectId()),
        "nombre": nombre,
        "geojson": geojson
    }

    ubicaciones_collection.insert_one(poligono)
    return jsonify({"message": "Polígono agregado correctamente", "id": poligono["_id"]}), 201

def obtener_poligonos():
    poligonos = list(ubicaciones_collection.find({}))
    return jsonify(poligonos), 200

def eliminar_poligono(id):
    result = ubicaciones_collection.delete_one({"_id": id})
    if result.deleted_count == 0:
        return jsonify({"error": "Polígono no encontrado"}), 404
    return jsonify({"message": "Polígono eliminado correctamente"}), 200