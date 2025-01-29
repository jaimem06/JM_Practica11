from flask import Blueprint, request, jsonify
from controllers.usuarioController import crear_usuario , obtener_usuarios, obtener_usuario_por_external_id

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/crear', methods=['POST'])
def add_user():
    data = request.get_json()
    nombre = data.get('nombre')
    apellido = data.get('apellido')
    correo = data.get('correo')
    contraseña = data.get('contraseña')
    ubicacion = data.get('ubicacion')

    response = crear_usuario(nombre, apellido, correo, contraseña, ubicacion)
    return jsonify(response)

@usuario_bp.route('/obtener', methods=['GET'])
def listar_usuarios():
    usuarios = obtener_usuarios()
    return jsonify(usuarios)

@usuario_bp.route('/obtener/<external_id>', methods=['GET'])
def listar_usuario_por_external_id(external_id):
    usuario = obtener_usuario_por_external_id(external_id)
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404