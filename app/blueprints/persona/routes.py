from flask import Blueprint, flash, redirect, request, jsonify, render_template, url_for

from services.IPersonaServicio import IPersonaServicio
from domain.persona.modelo import Persona

persona_bp = Blueprint('persona', __name__, url_prefix='/persona')

persona_servicio = IPersonaServicio()

@persona_bp.route('/crear', methods=['POST'])
def crear_persona():
    data = request.json
    nueva_persona = Persona(nombre=data['nombre'], edad=data['edad'], ocupacion=data['ocupacion'])
    persona_servicio.crear_persona(nueva_persona)
    return jsonify({'message': 'Persona creada'}), 201

@persona_bp.route('/<int:id>', methods=['GET'])
def obtener_persona(id):
    persona = persona_servicio.buscar_persona(id)
    if persona:
        return jsonify(persona), 200
    return jsonify({'message': 'Persona no encontrada'}), 404

@persona_bp.route('/<int:id>', methods=['PUT'])
def actualizar_persona(id):
    data = request.json
    persona = persona_servicio.buscar_persona(id)
    if persona:
        persona.nombre = data['nombre']
        persona.edad = data['edad']
        persona.ocupacion = data['ocupacion']
        persona_servicio.actualizar_persona(persona)
        return jsonify({'message': 'Persona actualizada'}), 200
    return jsonify({'message': 'Persona no encontrada'}), 404

@persona_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_persona(id):
    persona = persona_servicio.buscar_persona(id)
    if persona:
        persona_servicio.eliminar_persona(persona)
        return jsonify({'message': 'Persona eliminada'}), 200
    return jsonify({'message': 'Persona no encontrada'}), 404

@persona_bp.route('/listar', methods=['GET'])
def listar_personas():
    personas = persona_servicio.listar_personas()
    return render_template('persona/listar.html', personas=personas)

@persona_bp.route('/nuevo', methods=['GET', 'POST'])
def nuevo_persona():
    if request.method == 'POST':
        data = request.form
        nueva_persona = Persona(nombre=data['nombre'], edad=data['edad'], ocupacion=data['ocupacion'])
        persona_servicio.crear_persona(nueva_persona)
        return redirect(url_for('persona.listar_personas'))
    return render_template('persona/nuevo.html')

@persona_bp.route('/mostrar/<int:id>', methods=['GET'])
def mostrar_persona(id):
    persona = persona_servicio.buscar_persona(id)
    if persona:
        return render_template('persona/mostrar.html', persona=persona)
    else:
        flash('Persona no encontrada.', 'warning')
        return redirect(url_for('persona.listar_personas'))

# Aquí podrías definir más rutas y funciones auxiliares según las necesidades de tu aplicación
