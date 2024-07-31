# Aplicación de Principios de Clean Code, SOLID y Estilos de Programacion
Este documento detalla cómo se aplican los principios de Clean Code y SOLID en el proyecto actual, utilizando Python y SQLAlchemy para modelar una base de datos y Flask-RESTful para el manejo de servicios.

## Aplicación de Principios SOLID
## 1. Principio de Responsabilidad Única (SRP)
Cada clase debe tener una única responsabilidad. Esto significa que cada clase debe hacer una sola cosa y hacerla bien.
```python
class Eleccion(db.Model):
    __tablename__ = 'eleccion'
    
    id_eleccion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha = db.Column(db.Date, nullable=True)
    hora_inicio = db.Column(db.Time, nullable=True)
    hora_fin = db.Column(db.Time, nullable=True)
    estado = db.Column(Enum('abierto', 'cerrado', name='estado_enum'), nullable=True)
    descripcion = db.Column(db.String(100), nullable=True)
    listas = db.relationship('ListaCandidato', backref="eleccion")
    
    def __init__(self, fecha, hora_inicio, hora_fin, estado, descripcion):
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = self.hora_fin
        self.estado = estado
        self.descripcion = descripcion

```
La clase Eleccion maneja únicamente la información de una elección, cumpliendo así con el principio de responsabilidad única.
## 2. Principio de Abierto/Cerrado (OCP)
Las entidades de software (clases, módulos, funciones, etc.) deben estar abiertas para la extensión, pero cerradas para la modificación. Esto significa que se debe poder añadir nuevo comportamiento sin modificar el código existente.

Ejemplo:
```python
class EleccionServicioImpl(IEleccionServicio):
    def get_all_eleccion(self):
        try:
            all_eleccion = Eleccion.query.all()
            result = eleccion_schemas.dump(all_eleccion)
            return result
        except Exception as e:
            logger.error(f'Error al obtener todas las elecciones: {str(e)}')
            raise e
```
Si se necesita agregar un nuevo método para manejar elecciones, se puede extender EleccionServicioImpl sin modificar los métodos existentes.

## 3. Principio de Sustitución de Liskov (LSP)
Los objetos de un programa deben ser reemplazables por instancias de sus subtipos sin alterar el funcionamiento del programa.

Ejemplo:
```python
class EleccionServicioImpl(IEleccionServicio):
    def get_all_eleccion(self):
        try:
            all_eleccion = Eleccion.query.all()
            result = eleccion_schemas.dump(all_eleccion)
            return result
        except Exception as e:
            logger.error(f'Error al obtener todas las elecciones: {str(e)}')
            raise e
```
EleccionServicioImpl puede ser sustituida por cualquier otra implementación de IEleccionServicio sin alterar el funcionamiento del programa.
# Aplicación de Principios de Clean Code
## 1. Nombres Descriptivos
Ejemplo en la clase Eleccion:
```python
class Eleccion(db.Model):
    __tablename__ = 'eleccion'
    
    id_eleccion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha = db.Column(db.Date, nullable=True)
    hora_inicio = db.Column(db.Time, nullable=True)
    hora_fin = db.Column(db.Time, nullable=True)
    estado = db.Column(Enum('abierto', 'cerrado', name='estado_enum'), nullable=True)
    descripcion = db.Column(db.String(100), nullable=True)
    listas = db.relationship('ListaCandidato', backref="eleccion")
    
    def __init__(self, fecha, hora_inicio, hora_fin, estado, descripcion):
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.estado = estado
        self.descripcion = descripcion

```
Ejemplo en la clase ListaCandidato:
```python
class ListaCandidato(db.Model):
    __tablename__ = 'lista_candidato'
    
    id_lista = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=True)
    id_eleccion = db.Column(db.Integer, db.ForeignKey('eleccion.id_eleccion'), nullable=True)
    lista_voto = db.relationship('Voto', backref="lista_candidato")

    def __init__(self, nombre, id_eleccion):
        self.nombre = nombre
        self.id_eleccion = id_eleccion

```
## 2. Cohesión
Responsabilidad Única:
Cada clase tiene una sola responsabilidad:

1. La clase Eleccion maneja la información de una elección.
2. La clase ListaCandidato maneja la información de las listas de candidatos.

Ejemplo:
```python
class Eleccion(db.Model):
    # Definición de atributos y métodos relacionados con elecciones

class ListaCandidato(db.Model):
    # Definición de atributos y métodos relacionados con listas de candidatos

```
## 3. Encapsulación
Atributos Privados:
Los atributos se acceden y modifican a través de métodos. Aunque no se muestran explícitamente como privados, se sigue la convención de encapsulamiento.

Ejemplo en la clase Eleccion:

python
```python
class Eleccion(db.Model):
    # Definición de atributos y métodos relacionados con elecciones
```
## 4. Consistencia
Convenciones de Nombres:
Las tablas en la base de datos están nombradas en formato snake_case, y las clases en formato CamelCase.

Ejemplo:
```python
class Eleccion(db.Model):
    __tablename__ = 'eleccion'
    # ...

class ListaCandidato(db.Model):
    __tablename__ = 'lista_candidato'
    # ...
```
## 5. Evitar Código Duplicado
Uso de Esquemas:
El esquema EleccionSchema se define una sola vez y se reutiliza para serializar datos.

Ejemplo:

```python
class EleccionSchema(ma.Schema):
    class Meta:
        fields = (
            'id_eleccion',
            'fecha',
            'hora_inicio',
            'hora_fin',
            'estado',
            'descripcion',
            'listas'
        )
```
## 6. Separación de Preocupaciones
Servicios y Modelos:
El código está dividido en modelos y servicios. Los modelos (Eleccion, ListaCandidato) definen la estructura de la base de datos, mientras que los servicios (EleccionServicioImpl) manejan la lógica de negocio.

Ejemplo en EleccionServicioImpl:

```python
from app.models import Eleccion, EleccionSchema
from app import ma
from app.services.IEleccionServicio import IEleccionServicio

eleccion_schema = EleccionSchema()
eleccion_schemas = EleccionSchema(many=True)

class EleccionServicioImpl(IEleccionServicio):
    def get_all_eleccion(self):
        all_eleccion = Eleccion.query.all()
        result = eleccion_schemas.dump(all_eleccion)
        return result
```
# Estilos de Programación
## 1. Things (Uso de Interfaces y Clases Abstractas)
Estás utilizando interfaces (clases abstractas) para definir el comportamiento esperado de diferentes servicios en tu sistema. Esto es un ejemplo claro del estilo Things, ya que encapsulas comportamientos en abstracciones claras y reutilizables.
```python
from abc import ABC, abstractmethod

class IEleccionServicio(ABC):
    @abstractmethod
    def get_all_eleccion(self):
        pass
    @abstractmethod
    def get_candidatos_by_eleccion(self, int):
        pass
    @abstractmethod
    def get_all_eleccion_abiertas(self):
        pass
    @abstractmethod
    def insert_eleccion(self, eleccion):
        pass
    @abstractmethod
    def get_elector_by_email(self, email):
        pass
    @abstractmethod
    def get_elecciones_hechas_por_elector(self, id_elector):
        pass

class IVotoServicio(ABC):
    @abstractmethod
    def get_voto_by_elector(self, id_elector):
        pass 
    @abstractmethod
    def votar(self, id_lista, id_elector):
        pass
    @abstractmethod
    def get_all_votos(self):
        pass
def ver_votos():
    votos = voto_servicio.get_all_votos()
    return render_template("ProcesoVotacion/votos.html", data = votos)

@home_bp.route('/Votar', methods=['POST'])
@login_required
def votar():
    id_lista = request.form['id_lista']
    elector = eleccion_servicio.get_elector_by_email(session['correo'])
    voto_servicio.votar(id_lista, elector.id)
    return redirect(url_for('home_bp.dashboard'))
```
## 2. Error/Exception Handling (Gestión de Errores y Excepciones)
Estás manejando errores en varias partes de tu código usando bloques try y except. Esto asegura que las excepciones sean capturadas y gestionadas adecuadamente, proporcionando información útil en los logs.
```python
class EleccionServicioImpl(IEleccionServicio):
    def get_all_eleccion(self):
        try:
            all_eleccion = Eleccion.query.all()
            result = eleccion_schemas.dump(all_eleccion)
            return result
        except Exception as e:
            logger.error(f'Error al obtener todas las elecciones: {str(e)}')
            raise e

    def get_candidatos_by_eleccion(self, id_eleccion):
        try:
            all_candidatos = db.session.query(
                Candidato.nombres, 
                Candidato.apellido_paterno, 
                Candidato.apellido_materno, 
                ListaCandidato.nombre, 
                Candidato.id
            ).join(
                ListaCandidato, ListaCandidato.id_lista == Candidato.id_lista_candidato
            ).filter(
                ListaCandidato.id_eleccion == id_eleccion
            ).all()
            result = [{"Candidato": '%s %s %s' % (tupla[0], tupla[1], tupla[2]), "Lista": tupla[3], "id_candidato": tupla[4]} for tupla in all_candidatos]
            return result
        except Exception as e:
            logger.error(f'Error al obtener los candidatos por elección: {str(e)}')
            raise e
```
## 3. Restful (Implementación de Servicios Web REST)
Estás implementando rutas en Flask que responden a diferentes métodos HTTP, lo cual es un ejemplo claro del estilo Restful. Cada ruta define un recurso y las operaciones que se pueden realizar sobre él.
```python
@home_bp.route('/Votos')
def ver_votos():
    votos = voto_servicio.get_all_votos()
    return render_template("ProcesoVotacion/votos.html", data = votos)

@home_bp.route('/EleccionVotacion', methods=['GET'])
@login_required
def seleccionar_eleccion_votacion():
    elector = eleccion_servicio.get_elector_by_email(session['correo'])
    elecciones = eleccion_servicio.get_all_eleccion()
    elecciones_hechas = eleccion_servicio.get_elecciones_hechas_por_elector(elector.id)
    elecciones_restantes = len(elecciones) - len(elecciones_hechas)
    return render_template('ProcesoVotacion/lista_eleccion_votacion.html', data = elecciones, elecciones_hechas = elecciones_hechas, elecciones_restantes = elecciones_restantes)

@home_bp.route('/CandidatosVotacion', methods=['POST'])
@login_required
def ver_candidatos_votacion():
    id_eleccion = request.form['voto']
    candidatos = lista_servicio.get_lista_by_eleccion(id_eleccion)
    return render_template('ProcesoVotacion/votacion.html', data = candidatos)

@home_bp.route('/Resumen', methods=['POST'])
@login_required
def resumir_votacion():
    id_lista = request.form['id_lista']
    lista = lista_servicio.get_lista_by_id(id_lista)
    return render_template('ProcesoVotacion/resumen.html', data = lista)

@home_bp.route('/Votar', methods=['POST'])
@login_required
def votar():
    id_lista = request.form['id_lista']
    elector = eleccion_servicio.get_elector_by_email(session['correo'])
    voto_servicio.votar(id_lista, elector.id)
    return redirect(url_for('home_bp.dashboard'))

```
## 4. Persistent-Tables (Tablas Persistentes)   
Este estilo se refiere a la creación y manejo de tablas en una base de datos que persisten datos a través de las sesiones. Aquí, la clase Eleccion es un modelo de SQLAlchemy que define una tabla en la base de datos, con sus columnas y relaciones.
```python
class Eleccion(db.Model):
    __tablename__ = 'eleccion'

    id_eleccion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha = db.Column(db.Date, nullable=True)
    hora_inicio = db.Column(db.Time, nullable=True)
    hora_fin = db.Column(db.Time, nullable=True)
    estado = db.Column(Enum('abierto', 'cerrado', name='estado_enum'), nullable=True)
    descripcion = db.Column(db.String(100), nullable=True)
    listas = db.relationship('ListaCandidato', backref=("eleccion"))
    
    def __init__(self, fecha, hora_inicio, hora_fin, estado, descripcion):
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.estado = estado
        self.descripcion = descripcion
class Elector(db.Model):
    __tablename__ = 'elector'

    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(100), nullable=False)
    apellido_paterno = db.Column(db.String(100), nullable=False)
    apellido_materno = db.Column(db.String(100), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    contrasena = db.Column(db.String(80), nullable=False)
    correo = db.Column(db.String(100), nullable=False)

    def __init__(self, nombres, apellido_paterno, apellido_materno, fecha_nacimiento, usuario, contrasena, correo):
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.fecha_nacimiento = fecha_nacimiento
        self.usuario = usuario
        self.contrasena = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        self.correo = correo

class Candidato(db.Model):
    __tablename__ = 'candidato'
    id_candidato  = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(100), nullable=False)
    apellido_paterno = db.Column(db.String(100), nullable=False)
    apellido_materno = db.Column(db.String(100), nullable=False)
    id_lista = db.Column(db.Integer, db.ForeignKey('listacandidato.id_lista'), nullable=True)

    def __init__(self, nombres, apellido_paterno, apellido_materno, id_lista_candidato):
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.id_lista_candidato = id_lista_candidato
```
## 5. Cookbook (Patrones Comunes)
Definir un esquema de serialización usando marshmallow es un ejemplo de un patrón común, donde defines cómo se deben serializar/deserializar los datos de tu modelo. Aquí, EleccionSchema es un esquema que especifica los campos que se deben incluir al serializar una instancia de Eleccion.
```python
class EleccionSchema(ma.Schema):
    class Meta:
        fields = (
            'id_eleccion',
            'fecha',
            'hora_inicio',
            'hora_fin',
            'estado',
            'descripcion',
            'listas'
        )
class VotoSchema(ma.Schema):
    class Meta:
        fields = (
            'id_voto',
            'id_elector',
            'id_lista_candidato'
        )
```