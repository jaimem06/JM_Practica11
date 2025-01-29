from flask import request, jsonify, make_response, current_app
from pymongo import MongoClient
import jwt
from functools import wraps
from config import MONGODB_URI, MONGODB_DB

client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000, tls=True)
db = client[str(MONGODB_DB)]
usuarios_collection = db['usuarios']

def token_required(f):
    @wraps(f)
    # Es un componente para validar el token
    def decored(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            if auth_header.startswith('Bearer '):
                token = auth_header.split(' ')[1]
        if not token:
            return make_response(
                jsonify({"msg": "Token is missing!", "code": 401}),
                401
            )
        try:
            secret_key = current_app.config['JWT_SECRET_KEY']
            data = jwt.decode(token, key=secret_key, algorithms=["HS256"])
            user = usuarios_collection.find_one({"external_id": data['external']})
            if not user:
                return make_response(
                    jsonify({"msg": "User not found", "code": 401}),
                    401
                )
        except jwt.ExpiredSignatureError:
            return make_response(
                jsonify({"msg": "Token has expired", "code": 401}),
                401
            )
        except jwt.InvalidTokenError as e:
            print(f"Invalid token: {e}")
            return make_response(
                jsonify({"msg": f"Invalid token: {e}", "code": 401}),
                401
            )
        return f(*args, **kwargs)
    return decored