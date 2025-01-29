from models.model_usuario import Usuario, usuarios_collection
from flask import current_app, jsonify
import jwt
from datetime import datetime, timedelta, timezone
import bcrypt
import logging

logging.basicConfig(level=logging.DEBUG)

class LoginControl:
    def inicio_sesion(self, data):
        try:
            # Buscar la cuenta por correo y estado
            cuentaA = usuarios_collection.find_one({"correo": data.get('correo'), "estado": "activo"})
            if not cuentaA:
                print(f"Usuario no encontrado o inactivo: {data.get('correo')}")
                return jsonify({"code": 400, "datos": {"error": "Correo o contraseña incorrectos"}, "msg": "ERROR"}), 400

            print(f"Usuario encontrado: {cuentaA['correo']}")
            # Verificar la contraseña enviada con la almacenada
            if not bcrypt.checkpw(data["contraseña"].encode('utf-8'), cuentaA['contraseña'].encode('utf-8')):
                print("Contraseña incorrecta")
                return jsonify({"code": 400, "datos": {"error": "Correo o contraseña incorrectos"}, "msg": "ERROR"}), 400

            token = jwt.encode(
                {
                    "external": cuentaA['external_id'],
                    "expiracion": (datetime.now(timezone.utc) + timedelta(minutes=60)).isoformat()
                },
                current_app.config["JWT_SECRET_KEY"],
                algorithm="HS256"
            )
            info = {
                "token": token,
                "user": cuentaA['apellido'] + " " + cuentaA['nombre'],
                "external": cuentaA['external_id'],
            }
            return jsonify({"code": 200, "datos": info, "msg": "SUCCESS"}), 200
        except Exception as e:
            logging.error(f"Error al iniciar sesión: {e}")
            print(f"Error al iniciar sesión: {e}")
            return jsonify({"code": 500, "datos": {"error": "Error interno del servidor"}, "msg": "ERROR"}), 500