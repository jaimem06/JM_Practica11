from flask import Flask, jsonify
from pymongo import MongoClient, errors
from config import MONGODB_URI
from routes.route_usuario import usuario_bp
from routes.route_login import login_bp
from routes.route_validartoken import api_validarToken
from routes.route_ubicaciones import api_ubicaciones
from flask_cors import CORS
import os

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

    CORS(app)  # Enable CORS for all routes

    try:
        client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000, tls=True)
        client.admin.command('ping')
        connection_status = {"message": "MongoDB conectado correctamente", "status": "success"}
    except errors.ServerSelectionTimeoutError as e:
        connection_status = {"message": f"Error al conectar con MongoDB: {e}", "status": "failure"}

    @app.route('/')
    def index():
        return jsonify(connection_status)
    
    app.register_blueprint(usuario_bp, url_prefix='/usuario')
    app.register_blueprint(login_bp, url_prefix='/home')
    app.register_blueprint(api_validarToken, url_prefix='/validaciones')
    app.register_blueprint(api_ubicaciones, url_prefix='/ubicacion')

    return app