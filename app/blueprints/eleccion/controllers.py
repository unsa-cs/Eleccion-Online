from flask import Blueprint, request, jsonify
from services.EleccionServicioImpl import EleccionServicioImpl
from domain.eleccion.modelo.Eleccion import Eleccion

eleccion_controller = Blueprint('eleccion_controller', __name__)
eleccion_service = EleccionServicioImpl()

@eleccion_controller.route('/eleccion', methods=['POST'])
def iniciar_eleccion():
    data = request.json
    nueva_eleccion = Eleccion(id=data['id'], nombre=data['nombre'], lista_candidatos=data['lista_candidatos'])
    eleccion_service.iniciar_eleccion(nueva_eleccion)
    return jsonify({'message': 'Elección iniciada'}), 201

@eleccion_controller.route('/eleccion/<int:id>', methods=['GET'])
def obtener_eleccion(id):
    eleccion = eleccion_service.buscar_eleccion(id)
    if eleccion:
        return jsonify(eleccion), 200
    return jsonify({'message': 'Elección no encontrada'}), 404

@eleccion_controller.route('/eleccion/<int:id>', methods=['PUT'])
def actualizar_eleccion(id):
    data = request.json
    eleccion = eleccion_service.buscar_eleccion(id)
    if eleccion:
        eleccion.nombre = data['nombre']
        eleccion.lista_candidatos = data['lista_candidatos']
        eleccion_service.actualizar_eleccion(eleccion)
        return jsonify({'message': 'Elección actualizada'}), 200
    return jsonify({'message': 'Elección no encontrada'}), 404

@eleccion_controller.route('/eleccion/<int:id>', methods=['DELETE'])
def eliminar_eleccion(id):
    eleccion = eleccion_service.buscar_eleccion(id)
    if eleccion:
        eleccion_service.eliminar_eleccion(eleccion)
        return jsonify({'message': 'Elección eliminada'}), 200
    return jsonify({'message': 'Elección no encontrada'}), 404
