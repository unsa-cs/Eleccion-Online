# Clean Code

## Nombres

En los siguientes codigos se muestras las aplicaciones del clean code, como es indicado por el Naming Convetions.

1. Las clases en Python en deben ser en CamelCase.
2. Las variables en Pyhton usan el estilo de snake_case.
3. Descripcion clara de nombres aplicados.

```
class Elector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(100), nullable=False)
    apellido_paterno = db.Column(db.String(100), nullable=False)
    apellido_materno = db.Column(db.String(100), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    contrasena = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
```

## Funciones

En el siguiente codigo aplicamos clean code en funciones, deben ser pequeñas y realizar un tarea especifica.

```
def hash_constrasena(self, contrasena):
    return bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def revisar_contrasena(self, contrasena):
    return bcrypt.checkpw(contrasena.encode('utf-8'), self.contrasena.encode('utf-8'))

```

## Comentarios

El codigo debe ser claro para que los comentarios extensos no sean necesarios. Los comentarios, deben agregar valor explicativo.

```
def emitir_voto(self, candidato_id):
    # Lógica para emitir el voto
    pass
```

## Errores

En el siguiente codigo se maneja los errore con Unchecked Exceptions.

```
def create_elector(self, elector_modelo):
    elector = Elector(
        nombres=elector_modelo.nombres,
        apellido_paterno=elector_modelo.apellido_paterno,
        apellido_materno=elector_modelo.apellido_materno,
        fecha_nacimiento=elector_modelo.fecha_nacimiento,
        usuario=elector_modelo.usuario,
        contrasena=elector_modelo.contrasena,
        correo=elector_modelo.correo
    )
    try:
        db.session.add(elector)
        db.session.commit()
        logger.info(f'Elector creado correctamente: {elector}')
        return elector
    except Exception as e:
        db.session.rollback()
        logger.error(f'Error al crear el elector: {str(e)}')
        raise e

def update_elector(self, elector: Elector):
    try:
        db.session.merge(elector)
        db.session.commit()
        logger.info(f'Elector actualizado correctamente: {elector}')
    except Exception as e:
        db.session.rollback()
        logger.error(f'Error al actualizar el elector: {str(e)}')
        raise e

def delete_elector(self, elector: Elector):
    try:
        db.session.delete(elector)
        db.session.commit()
        logger.info(f'Elector eliminado correctamente: {elector}')
    except Exception as e:
        db.session.rollback()
        logger.error(f'Error al eliminar el elector: {str(e)}')
        raise e
```

```
@home_bp.route('/electores', methods=['GET','POST'])
def crear_elector():
    try:
        data = request.form
        elector = Elector(
            ...
            correo=data.get('correo')
        )

        elector_service.create_elector(elector)
        mensaje = 'Elector creado correctamente'

        return render_template('register.html', mensaje=mensaje)
    except Exception as e:
        mensaje_error = f"Error al crear el elector: {str(e)}"
        logger.error(mensaje_error)
        return render_template('register.html', mensaje=mensaje_error)
```

# Principios SOLID

## Principio de Responsabilidad Unica (SRP)

Se ha separado la logica de manejo de formularios y la logica de negocios en diferentes clases.

```
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
```

## Principio de Sustitucion de Liskov (LSP)

Se implemento la clase ElectorService como base para que luego puedan ser implementadas sin alterar su funcionamiento, con clases Derivadas.

```
from abc import ABC, abstractmethod

class ElectorService(ABC):
    @abstractmethod
    def get_elector_by_id(self, id):
        pass

    @abstractmethod
    def create_elector(self, elector_dto):
        pass

    @abstractmethod
    def update_elector(self, elector):
        pass

    @abstractmethod
    def delete_elector(self, elector):
        pass

```

## Principio Abierto/Cerrado (OCP)

Se usa un interfaz para ElectorServiceImpl que permite extender la funcionalidad sin necesidad de modificar el codigo existente

```
class ElectorServiceImpl(ElectorService):
    def get_elector_by_id(self, id):
        try:
            return Elector.query.get(id)
        except Exception as e:
            logger.error(f'Error al obtener el elector por ID: {str(e)}')
            raise e

    def create_elector(self, elector_modelo, contrasena:str):
        elector = Elector(
            nombres=elector_modelo.nombres,
            apellido_paterno=elector_modelo.apellido_paterno,
            apellido_materno=elector_modelo.apellido_materno,
            fecha_nacimiento=elector_modelo.fecha_nacimiento,
            usuario=elector_modelo.usuario,
            contrasena=contrasena,
            correo=elector_modelo.correo
        )
        try:
            db.session.add(elector)
            db.session.commit()
            logger.info(f'Elector creado correctamente: {elector}')
            return elector
        except Exception as e:
            db.session.rollback()
            logger.error(f'Error al crear el electbor: {str(e)}')
            raise e

    def update_elector(self, elector: Elector):
        try:
            db.session.merge(elector)
            db.session.commit()
            logger.info(f'Elector actualizado correctamente: {elector}')
        except Exception as e:
            db.session.rollback()
            logger.error(f'Error al actualizar el elector: {str(e)}')
            raise e

    def delete_elector(self, elector: Elector):
        try:
            db.session.delete(elector)
            db.session.commit()
            logger.info(f'Elector eliminado correctamente: {elector}')
        except Exception as e:
            db.session.rollback()
            logger.error(f'Error al eliminar el elector: {str(e)}')
            raise e
```
