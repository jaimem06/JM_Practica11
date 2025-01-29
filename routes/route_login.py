from flask import Blueprint, request, jsonify
from controllers.login_controller import LoginControl
from flask_expects_json import expects_json

login_bp = Blueprint('login', __name__)
login_control = LoginControl()

schema_sesion = {
    "type": "object",
    'properties': {
        "correo": {"type": "string"},
        "contraseña": {"type": "string"},
    },
    'required': ["correo", "contraseña"]
}

# API para iniciar sesion
@login_bp.route('/login', methods=['POST'])
@expects_json(schema_sesion)
def login():
    data = request.get_json()
    response, status_code = login_control.inicio_sesion(data)
    return response, status_code