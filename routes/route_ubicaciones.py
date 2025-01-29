from flask import Blueprint
from controllers.ubicaciones_controller import agregar_poligono, obtener_poligonos, eliminar_poligono

api_ubicaciones = Blueprint('ubicaciones', __name__)

@api_ubicaciones.route('/poligonos', methods=['POST'])
def route_agregar_poligono():
    return agregar_poligono()

@api_ubicaciones.route('/listar', methods=['GET'])
def route_obtener_poligonos():
    return obtener_poligonos()

@api_ubicaciones.route('/eliminar/<string:id>', methods=['DELETE'])
def route_eliminar_poligono(id):
    return eliminar_poligono(id)
