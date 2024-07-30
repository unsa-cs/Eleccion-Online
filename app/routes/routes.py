import logging

from flask import render_template, Blueprint, request, jsonify, session, redirect, url_for, make_response

from app.models.Elector import Elector
from app.models.Eleccion import Eleccion
from app.models.ListaCandidato import ListaCandidato
from app.models.Candidato import Candidato
from app.services.PersonaServicioImpl import ElectorServiceImpl
from app.services.EleccionServicioImpl import EleccionServicioImpl


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

REGISTER_TEMPLATE = 'register.html'

home_bp = Blueprint('home_bp', __name__, template_folder='templates')

elector_service = ElectorServiceImpl()
eleccion_servicio = EleccionServicioImpl()


@home_bp.route('/EleccionesActivas', methods=['GET'])
def listar_elecciones():
    elecciones_json = eleccion_servicio.get_all_eleccion()
    return render_template('lista_eleccion.html', elecciones = elecciones_json)

@home_bp.route('/VerCandidatos', methods=['POST'])
def ver_candidatos():
    id_eleccion = request.form['eleccion_id']
    result = eleccion_servicio.get_candidatos_by_eleccion(id_eleccion)
    return render_template("lista_candidatos.html", data = result)

@home_bp.route('/FormularioEleccion', methods=['GET'])
def agregar_eleccion():
    return render_template("ProcesoVotacion/form_eleccion.html")

@home_bp.route('/InsertEleccion', methods=['POST'])
def insert_eleccion():
    fecha = request.form['fecha']
    hora_inicio = request.form['hora_inicio']
    hora_fin = request.form['hora_fin']
    estado = request.form['estado']
    descripcion = request.form['descripcion']
    eleccion = Eleccion(fecha, hora_inicio, hora_fin, estado, descripcion)
    eleccion_servicio.insert_eleccion(eleccion)
    return url_for('home_bp.listar_elecciones')

@home_bp.route('/EleccionVotacion', methods=['GET'])
def seleccionar_eleccion_votacion():
    elecciones_abiertas_json = eleccion_servicio.get_all_eleccion_abiertas()
    return render_template('ProcesoVotacion/lista_eleccion_votacion.html', data = elecciones_abiertas_json)

@home_bp.route('/CandidatosVotacion', methods=['POST'])
def ver_candidatos_votacion():
    id_eleccion = request.form['voto']
    candidatos = eleccion_servicio.get_candidatos_by_eleccion(id_eleccion)
    return render_template('ProcesoVotacion/vota2.html', data = candidatos)

@home_bp.route('/')
def index():
    return render_template('index.html')


@home_bp.route('/register', methods=['GET','POST'])
def register():
    REGISTER_HTML = 'register.html'
    try:
        if request.method == 'POST':
            data = request.form
            elector = Elector(
                nombres=data.get('nombres'),
                apellido_paterno=data.get('apellido_paterno'),
                apellido_materno=data.get('apellido_materno'),
                fecha_nacimiento=data.get('fecha_nacimiento'),
                usuario=data.get('usuario'),
                contrasena=data.get('contrasena'),
                correo=data.get('correo')
            )

            elector_service.create_elector(elector,data.get('contrasena'))
            mensaje = 'Elector creado correctamente'
            return render_template(REGISTER_HTML, mensaje=mensaje)

        return render_template(REGISTER_HTML)
    except Exception as e:
        mensaje_error = f"Error al crear el elector: {str(e)}"
        logger.error(mensaje_error)
        return render_template(REGISTER_HTML, mensaje=mensaje_error)

@home_bp.route('/login', methods=['GET','POST'])
def login():
    LOGIN_HTML = 'login.html'
    try:
        if request.method == 'POST':
            data = request.form
            correo = data.get('correo')
            contrasena = data.get('contrasena')

            elector = Elector.query.filter_by(correo=correo).first()
            if elector and elector.revisar_contrasena(contrasena):
                session['correo'] = elector.correo
                logger.info(f'El elector {elector.nombres} ha iniciado sesión')
                return render_template('dashboard.html', elector=elector)
            else:
                mensaje = 'Correo o contraseña incorrectos'
                return render_template(LOGIN_HTML, mensaje=mensaje)
        return render_template(LOGIN_HTML)
    except Exception as e:
        mensaje_error = f"Error al iniciar sesión: {str(e)}"
        logger.error(mensaje_error)
        return render_template(LOGIN_HTML, mensaje=mensaje_error)

@home_bp.route('/dashboard')
def dashboard():
    if 'correo' in session:
        elector = Elector.query.filter_by(correo=session['correo']).first()
        response = make_response(render_template('dashboard.html', elector=elector))
        response.headers['Cache-Control'] = 'no-store'
        response.headers['Pragma'] = 'no-cache'
        return response
    logger.warning('El usuario no ha iniciado sesión')
    return redirect(url_for('home_bp.login'))

@home_bp.route('/logout')
def logout():
    if 'correo' in session:
        logger.info(f'El elector {session["correo"]} ha cerrado sesión')
        session.pop('correo', None)
        session.clear()
    return redirect(url_for('home_bp.login'))

@home_bp.route('/electores/<int:id>', methods=['GET'])
def get_elector(id):
    return

@home_bp.route('/electores/<int:id>', methods=['PUT'])
def actualizar_elector(id):
    return

@home_bp.route('/electores/<int:id>', methods=['DELETE'])
def eliminar_elector(id):
    return

@home_bp.route('/candidatos')
def mostrar_candidatos():
    servicio = EleccionServicioImpl()  
    candidatos_con_propuestas = servicio.get_candidatos_con_propuestas()
    precandidatos_denegados = servicio.get_precandidatos_denegados()
    precandidatos_inscritos = servicio.get_precandidatos_inscritos()

    return render_template(
        'a/candidatos.html', 
        candidatos=candidatos_con_propuestas,
        precandidatos_denegados=precandidatos_denegados,
        precandidatos_inscritos=precandidatos_inscritos
    )

