<<<<<<< HEAD
Buenas Prácticas de Clean Code
1. Nombres Claros y Significativos
Modelos y Campos: Los nombres como Precandidato, Prepropuesta, id_precandidato, y propuesta son claros y descriptivos, lo que facilita entender el propósito de cada modelo y campo.
Métodos y Funciones: Los nombres de métodos como get_candidatos_con_propuestas, get_precandidatos_denegados, y get_precandidatos_inscritos son autoexplicativos y reflejan claramente la acción que realizan.
2. Separación de Responsabilidades
Modelos: Los modelos Precandidato y Prepropuesta tienen responsabilidades bien definidas y se encargan de representar y gestionar los datos de la base de datos.
Servicios: La clase EleccionServicioImpl está encargada de la lógica de negocio para obtener los datos necesarios. Esto separa la lógica de la base de datos del código de la aplicación, facilitando el mantenimiento y la comprensión.
3. Uso de Relaciones y Claves Foráneas
Relaciones Claras: La relación entre Precandidato y Prepropuesta está claramente definida mediante db.relationship y db.ForeignKey, lo que asegura que SQLAlchemy pueda manejar correctamente las relaciones entre tablas.
Esquemas: La relación en los esquemas también está clara, facilitando la serialización y el manejo de datos complejos.
4. Métodos de Servicio Bien Definidos
Modularidad: Cada método en EleccionServicioImpl tiene una responsabilidad única, lo que facilita la lectura y el mantenimiento del código.
Estructura de Datos: Los métodos devuelven estructuras de datos claras (listas de diccionarios) que pueden ser fácilmente utilizadas en las vistas o para otros propósitos.
5. Manejo de Errores y Verificación
Consultas: Se utilizan filtros y opciones de carga anticipada (db.joinedload) para garantizar que las consultas sean eficientes y correctas. La adición de filtros como Precandidato.denegado == -1 asegura que los datos obtenidos cumplan con los criterios deseados.
6. Uso de backref en Relaciones
Bidireccionalidad: El uso de backref en db.relationship proporciona una forma sencilla de acceder a la relación inversa, lo que simplifica el código y mejora la legibilidad.
7. Estructura de Código Consistente
Estilo y Formato: El código sigue un estilo consistente y está bien formateado, facilitando su lectura y comprensión.
Principios SOLID
Single Responsibility Principle (SRP) - Principio de Responsabilidad Única
Modelos: Los modelos Precandidato y Prepropuesta tienen la responsabilidad única de representar datos en la base de datos. Cada modelo se enfoca solo en una entidad específica.
Servicios: La clase EleccionServicioImpl tiene métodos que se encargan de obtener datos relacionados con elecciones y candidatos. Cada método en la clase tiene una responsabilidad clara y específica.
Open/Closed Principle (OCP) - Principio de Abierto/Cerrado
Modelos y Servicios: El código está diseñado para ser extendido sin modificar el código existente. Por ejemplo, se puede agregar nuevos métodos al servicio o nuevas relaciones a los modelos sin cambiar el código base. Las clases están abiertas a la extensión (agregar nuevas funcionalidades) pero cerradas a la modificación (no se necesita cambiar el código existente para agregar nuevas funcionalidades).
Dependency Inversion Principle (DIP) - Principio de Inversión de Dependencias
Servicios y Modelos: El código sigue el principio de inversión de dependencias al depender de abstracciones (IEleccionServicio) en lugar de depender directamente de implementaciones concretas. Esto facilita la flexibilidad y la capacidad de prueba del código, permitiendo sustituir implementaciones sin afectar el resto del sistema.
=======

## Buenas Prácticas de Clean Code


- **1.Nombre claros y descriptivos:** Los nombres como `Propuesta`, `id_candidato`, y `propuesta` son claros y descriptivos, lo que facilita entender el propósito de cada modelo y campo.
- **2.Notacion variables** Los nombres de métodos como `get_candidatos_con_propuestas` ustilizan la notacion snake_case.
- **3. Espacios e indentacion** No dejar espacios entre parentesis o corchetes, respetar la indentacion, se recomienda dejar espacios antes y despues de una asiganacion que no sea como argumento.
```python
class Propuesta(db.Model):
    __tablename__ = 'propuesta'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_candidato = db.Column(db.Integer, db.ForeignKey('candidato.id'), nullable=False)
    propuesta = db.Column(db.Text, nullable=False)
    
```
```python
    def get_candidatos_con_propuestas(self):
       
        candidatos = Candidato.query.options(db.joinedload(Candidato.propuestas)).all()
        
        result = []
        for candidato in candidatos:
            candidato_data = candidato_schema.dump(candidato)
            propuestas_data = propuesta_schema.dump(candidato.propuestas, many=True)
            candidato_data['propuestas'] = propuestas_data
            result.append(candidato_data)
        
        return result
```
- **4. Jerarquia de las importaciones** El orden de en el grupo de importaciones debe tener primero a los modulos estandar, luego los terceros y por ultimo los del proyecto. El orden alfabetico es opcional'

```python
    import logging

    from flask import render_template, Blueprint, request, jsonify, session, redirect, url_for, make_response

    from app.models.Elector import Elector
    from app.models.Eleccion import Eleccion
    from app.models.ListaCandidato import ListaCandidato
    from app.models.Candidato import Candidato
    from app.services.PersonaServicioImpl import ElectorServiceImpl
    from app.services.EleccionServicioImpl import EleccionServicioImpl
```

- **5. Estilo y Estructura**: Las separacion entre las clases y funciones debe ser de 2 espacios en blanco y , un espacio en blanco entre los metodos
```python
class EleccionServicioImpl(IEleccionServicio):
    def get_all_eleccion(self):
        all_eleccion = Eleccion.query.all()
        result = eleccion_schemas.dump(all_eleccion)
        return result
    
    def get_candidatos_by_eleccion(self, id_eleccion):
        all_candidatos = db.session.query(Candidato.nombres, Candidato.apellido_paterno, Candidato.apellido_materno, ListaCandidato.nombre, Candidato.id).join(ListaCandidato, ListaCandidato.id_lista == Candidato.id_lista_candidato).filter(ListaCandidato.id_eleccion == id_eleccion).all()
        result = [{"Candidato": '%s %s %s' % (tupla[0], tupla[1], tupla[2]), "Lista": tupla[3], "id_candidato": tupla[4]} for tupla in all_candidatos]
        return result
    
    def get_all_eleccion_abiertas(self):
        all_eleccion = Eleccion.query.filter(Eleccion.estado == "abierto").all()
        result = eleccion_schemas.dump(all_eleccion)
        return result
    
    def insert_eleccion(self, eleccion):
        db.session.add(eleccion)
        db.session.commit()
```

## Principios SOLID

### 1.Single Responsibility Principle (SRP) - Principio de Responsabilidad Única

- La clase **Candidato** es una  clase que tiene una responsabilidad clara y específica. A diferencia de otras clases similares como el de **Elector**
```python
class Candidato(db.Model):
    __tablename__ = 'candidato'
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(100), nullable=False)
    apellido_paterno = db.Column(db.String(100), nullable=False)
    apellido_materno = db.Column(db.String(100), nullable=False)
    id_lista_candidato = db.Column(db.Integer, db.ForeignKey('lista_candidato.id_lista'),nullable=True)
```
### 2.Open/Closed Principle (OCP) - Principio de Abierto/Cerrado

- El código está diseñado para ser extendido sin modificar alguna clase o metodo, manteniendo su codigo original.

### 3.Interface Segregation Principle - ISP 
- Tenemos nuestra interfaz **ElectroService** que posee relativamente pocos metodos, evitando una division en otras interfaces.

```python
class ElectorService(ABC):
    @abstractmethod
    def get_elector_by_id(self, id):
        pass

    @abstractmethod
    def create_elector(self, elector):
        pass

    @abstractmethod
    def update_elector(self, elector):
        pass

    @abstractmethod
    def delete_elector(self, elector):
        pass
```
>>>>>>> desarrollo
