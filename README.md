**CLEAN CODE**

-Nombres:
  
  En el siguiente codigo se muestran buenas practicas de clean code, como indica Naming Conventions:
  
  1.Las clases en python deben seguir el estilo **CamelCase**, en este caso si se aplica.
  
  2.Las variables deben usar el estilo **snake_case**, el ejemplo ya sigue esta convención.
  
  3.Es importante que los nombres sean **descriptivos y claros**. En este caso, los nombres de los atributos de la clase Elector son claros y descriptivos.
  ```
  class Elector(db.Model):
      __tablename__ = 'elector'

      id = db.Column(db.Integer, primary_key=True)
      nombres = db.Column(db.String(100), nullable=False)
      apellido_paterno = db.Column(db.String(100), nullable=False)
      apellido_materno = db.Column(db.String(100), nullable=False)
      fecha_nacimiento = db.Column(db.Date, nullable=False)
      usuario = db.Column(db.String(50), unique=True, nullable=False)
      contrasena = db.Column(db.String(100), nullable=False)
  ```

-Funciones:

  En el siguiente codigo seguimos clean code en funciones, que nos indica que cada función no debe tener varios parametros como se muestra este sigue la **forma diádica**
  ```
  class IPersonaRepositorio(ABC):
    
    @abstractmethod
    def create(self, elector: Elector) -> Elector:
        pass
    
    @abstractmethod
    def get_by_id(self, id: int) -> Elector:
        pass
  ```
  
-Errores:

  En este fragmento de codigo se muestra el manejo de errores con **Unchecked Exceptions**
  ```
  @home_bp.route('/electores', methods=['POST'])
  def crear_elector():
      try:
          data = request.form
          ...
          elector_creado = elector_service.create_elector(elector_dto)
          mensaje = 'Elector creado correctamente'
  
          return render_template('register.html', mensaje=mensaje)
      except Exception as e:
          mensaje_error = f"Error al crear el elector: {str(e)}"
          logger.error(mensaje_error)
          return render_template('register.html', mensaje=mensaje_error)
  ```

  
