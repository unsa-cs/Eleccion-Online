# Aplicación de Principios de Clean Code y SOLID

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