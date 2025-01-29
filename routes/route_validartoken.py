from flask import Blueprint, jsonify, make_response
from controllers.authenticate import token_required

api_validarToken = Blueprint("api_validarToken", __name__)

# Ruta protegida para validar el token
@api_validarToken.route("/token", methods=['GET'])
@token_required
def validate_token():
    return make_response(
        jsonify({"msg": "OK", "code": 200, "datos": "Token válido"}),
        200
    )
