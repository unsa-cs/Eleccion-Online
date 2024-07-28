from flask import render_template, Blueprint, request, jsonify


from app.services.PersonaServicioImpl import ElectorServiceImpl
from app.services.EleccionServicioImpl import EleccionServicioImpl
from app.services.EleccionServicioImpl import ListaServicioImpl

from app.models.Elector import Elector
from app.models.Eleccion import Eleccion
from app.models.ListaCandidato import ListaCandidato
from app.models.Candidato import Candidato

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

REGISTER_TEMPLATE = 'register.html'

home_bp = Blueprint('home_bp', __name__, template_folder='templates')


elector_service = ElectorServiceImpl()
eleccion_servicio = EleccionServicioImpl()
lista_servicio = ListaServicioImpl()

@home_bp.route('/Admin')
def home():
    return render_template('Admin/home.html')

@home_bp.route('/ListasCandidatos', methods=['GET'])
def listar_candidatos():
    listas_json = lista_servicio.obtener_listas_pendientes()
    return render_template('ListaCandidato/lista_candidatos.html', listas=listas_json)

@home_bp.route('/emitir_voto', methods=['GET'])
def listar_elecciones():
    eleccion_json = eleccion_servicio.get_all_eleccion()
    return render_template('ListaCandidato/lista_candidatos.html', listas=eleccion_json)

@home_bp.route('/VerCandidatos', methods=['GET'])
def ver_candidatos():
    result = eleccion_servicio.get_candidatos_by_eleccion()
    for nombres, nombre_lista in result:
        print(f"Candidato: {nombres}, Lista: {nombre_lista}")
    return 'received'

    

@home_bp.route('/')
def index():
    return render_template('index.html')

@home_bp.route('/login')
def login():
    return render_template('login.html')

@home_bp.route('/register')
def register():
    return render_template(REGISTER_TEMPLATE)

@home_bp.route('/electores', methods=['POST'])
def crear_elector():
    try:
        data = request.form
        elector = Elector(
            nombres=data.get('nombres'),
            apellido_paterno=data.get('apellido_paterno'),
            apellido_materno=data.get('apellido_materno'),
            fecha_nacimiento=data.get('fecha_nacimiento'),
            usuario=data.get('usuario'),
            contrasena=data.get('contrasena')
        )
        
        elector_service.create_elector(elector)
        mensaje = 'Elector creado correctamente'

        return render_template(REGISTER_TEMPLATE, mensaje=mensaje)
    except Exception as e:
        mensaje_error = f"Error al crear el elector: {str(e)}"
        logger.error(mensaje_error)
        return render_template(REGISTER_TEMPLATE, mensaje=mensaje_error)

@home_bp.route('/electores/<int:id>', methods=['GET'])
def get_elector(id):
    return

@home_bp.route('/electores/<int:id>', methods=['PUT'])
def actualizar_elector(id):
    return

@home_bp.route('/electores/<int:id>', methods=['DELETE'])
def eliminar_elector(id):
    return
