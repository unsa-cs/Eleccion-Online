from flask import Blueprint, request, jsonify
from services.PersonaServicioImpl import PersonaServicioImpl
from domain.persona.modelo.Persona import Persona

persona_controller = Blueprint('persona_controller', __name__)
persona_service = PersonaServicioImpl()

@persona_controller.route('/persona', methods=['POST'])
def crear_persona():
    data = request.json
    nueva_persona = Persona(nombre=data['nombre'], edad=data['edad'], ocupacion=data['ocupacion'])
    persona_service.crear_persona(nueva_persona)
    return jsonify({'message': 'Persona creada'}), 201

@persona_controller.route('/persona/<int:id>', methods=['GET'])
def obtener_persona(id):
    persona = persona_service.buscar_persona(id)
    if persona:
        return jsonify(persona), 200
    return jsonify({'message': 'Persona no encontrada'}), 404

@persona_controller.route('/persona/<int:id>', methods=['PUT'])
def actualizar_persona(id):
    data = request.json
    persona = persona_service.buscar_persona(id)
    if persona:
        persona.nombre = data['nombre']
        persona.edad = data['edad']
        persona.ocupacion = data['ocupacion']
        persona_service.actualizar_persona(persona)
        return jsonify({'message': 'Persona actualizada'}), 200
    return jsonify({'message': 'Persona no encontrada'}), 404

@persona_controller.route('/persona/<int:id>', methods=['DELETE'])
def eliminar_persona(id):
    persona = persona_service.buscar_persona(id)
    if persona:
        persona_service.eliminar_persona(persona)
        return jsonify({'message': 'Persona eliminada'}), 200
    return jsonify({'message': 'Persona no encontrada'}), 404
