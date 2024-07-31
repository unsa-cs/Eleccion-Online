## 1. Error/Exception Handling (Manejo de Errores/Excepciones)

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

## 2. Pipeline (Flujo de Datos)

 El patrón Pipeline se basa en procesar los datos a través de varias etapas secuenciales. Cuando lo implementé, lo utilicé para validar y procesar la información paso a paso antes de almacenarla en la base de datos. Cada etapa del pipeline se encarga de una tarea específica, lo que permite un flujo de datos más ordenado y controlado, asegurando que cada pieza de información sea tratada correctamente antes de llegar a su destino final.

## Implementación:

def crear_candidato(nombre, estado, id_eleccion):
    nuevo_candidato = Candidato(nombre=nombre, estado=estado, id_eleccion=id_eleccion)
    return nuevo_candidato

def guardar_en_bd(candidato):
    db.session.add(candidato)
    db.session.commit()

## 3. Restful 

En una arquitectura RESTful, cada URL representa un recurso y utilizo los métodos HTTP (GET, POST, PUT, DELETE) para interactuar con esos recursos. Cuando adapté el código a un estilo más RESTful, me aseguré de que cada URL representara un recurso específico y de que los métodos HTTP correspondieran a las operaciones correctas: GET para obtener información, POST para crear nuevos recursos, PUT para actualizar recursos existentes y DELETE para eliminarlos. Así, el código se ajusta a los principios REST y facilita la gestión de los recursos de manera más estructurada y clara.

## Implementación:
```python

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