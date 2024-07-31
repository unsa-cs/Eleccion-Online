## Estilos de Programacion
## 1. Error/Exception Handling 

El manejo de errores es esencial para que cualquier aplicación sea sólida y confiable. Cuando implementé el manejo de excepciones en mi código, me aseguré de que el sistema pudiera gestionar errores inesperados de forma controlada. Esto no solo previene que la aplicación se caiga, sino que también permite mostrar mensajes de error claros y amigables para el usuario. Así, si algo sale mal, el usuario recibe una notificación útil en lugar de un fallo inesperado.

## Implementación:


    @home_bp.route('/inscripcion', methods=['GET', 'POST'])
    def listas():
        if request.method == 'POST':
            try:
                for i in range(3):
                    nombre = request.form[f'nombre{i}']
                    estado = request.form[f'estado{i}']
                    id_eleccion = request.form[f'eleccion{i}']

                    if not nombre or not estado or not id_eleccion:
                        raise ValueError("Todos los campos deben ser llenados.")

                    nuevo_candidato = crear_candidato(nombre, estado, id_eleccion)
                    guardar_en_bd(nuevo_candidato)
                return redirect(url_for('success_page'))
            except ValueError as e:
                flash(f"Error en los datos del formulario: {e}", "error")
            except Exception as e:
                db.session.rollback()
                flash(f"Se produjo un error al guardar los datos: {e}", "error")
            finally:
                db.session.remove()
        return render_template('inscripcion.html')

## 2. Persistent-Tables
El uso de SQLAlchemy para definir modelos como ListaCandidato, Propuesta, y Candidato refleja el concepto de "Persistent-Tables". Este patrón se refiere a la práctica de definir estructuras de datos persistentes (tablas) que se almacenan en una base de datos. Los objetos de Python mapeados a estas tablas (a través de clases de modelo) permiten la persistencia de datos entre las ejecuciones de la aplicación.

## Implementación:

    class ListaCandidato(db.Model):
        __tablename__ = 'listacandidato'
        
        id_lista = db.Column(db.Integer, primary_key=True, autoincrement=True)
        nombre = db.Column(db.String(100), nullable=True)
        estado = db.Column(Enum(EstadoListaEnum), nullable=True, default=EstadoListaEnum.pendiente)
        id_eleccion = db.Column(db.Integer, db.ForeignKey('eleccion.id_eleccion'), nullable=True)


## 3. Restful 

En una arquitectura RESTful, cada URL representa un recurso y utilizo los métodos HTTP (GET, POST, PUT, DELETE) para interactuar con esos recursos. Cuando adapté el código a un estilo más RESTful, me aseguré de que cada URL representara un recurso específico y de que los métodos HTTP correspondieran a las operaciones correctas: GET para obtener información, POST para crear nuevos recursos, PUT para actualizar recursos existentes y DELETE para eliminarlos. Así, el código se ajusta a los principios REST y facilita la gestión de los recursos de manera más estructurada y clara.

## Implementación:


    @home_bp.route('/candidatos', methods=['POST'])
    def crear_candidato():
        data = request.get_json()
        try:
            nombre = data.get('nombre')
            estado = data.get('estado', EstadoListaEnum.pendiente.value)
            id_eleccion = data.get('id_eleccion')

            if not nombre or not id_eleccion:
                abort(400, description="Todos los campos requeridos deben ser proporcionados.")

            nuevo_candidato = Candidato(nombre=nombre, estado=estado, id_eleccion=id_eleccion)
            db.session.add(nuevo_candidato)
            db.session.commit()
            return jsonify({'id': nuevo_candidato.id_lista}), 201
        except Exception as e:
            db.session.rollback()
            abort(500, description=f"Error al crear el candidato: {e}")

    @home_bp.route('/candidatos/<int:id>', methods=['GET'])
    def obtener_candidato(id):
        candidato = Candidato.query.get(id)
        if candidato is None:
            abort(404, description="Candidato no encontrado.")
        return jsonify({
            'id': candidato.id_lista,
            'nombre': candidato.nombre,
            'estado': candidato.estado.value,
            'id_eleccion': candidato.id_eleccion
        })

    @home_bp.route('/candidatos/<int:id>', methods=['DELETE'])
    def eliminar_candidato(id):
        candidato = Candidato.query.get(id)
        if candidato is None:
            abort(404, description="Candidato no encontrado.")
        try:
            db.session.delete(candidato)
            db.session.commit()
            return '', 204
        except Exception as e:
            db.session.rollback()
            abort(500, description=f"Error al eliminar el candidato: {e}")

## Principios SOLID

## 1.Single Responsibility Principle (SRP) - Principio de Responsabilidad Única

    La clase Candidato es una clase que tiene una responsabilidad clara y específica. A diferencia de otras clases similares como el de Elector

class Candidato(db.Model):
    __tablename__ = 'candidato'
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(100), nullable=False)
    apellido_paterno = db.Column(db.String(100), nullable=False)
    apellido_materno = db.Column(db.String(100), nullable=False)
    id_lista_candidato = db.Column(db.Integer, db.ForeignKey('lista_candidato.id_lista'),nullable=True)

## 2.Open/Closed Principle (OCP) - Principio de Abierto/Cerrado
El código está diseñado para ser extendido sin modificar alguna clase o metodo, manteniendo su codigo original.

## 3.Interface Segregation Principle - ISP

Tenemos nuestra interfaz ElectroService que posee relativamente pocos metodos, evitando una division en otras interfaces.

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
