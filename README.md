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
  class ElectorService(ABC):
      @abstractmethod
      def get_elector_by_id(self, id):
          pass
  
      @abstractmethod
      def create_elector(self, elector_dto):
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
          elector_creado = elector_service.create_elector(elector)
          mensaje = 'Elector creado correctamente'
  
          return render_template('register.html', mensaje=mensaje)
      except Exception as e:
          mensaje_error = f"Error al crear el elector: {str(e)}"
          logger.error(mensaje_error)
          return render_template('register.html', mensaje=mensaje_error)
  ```
**SOLID**

1. Single Responsibility Principle:La clase **ElectorService** se enfoca únicamente en definir una interfaz para operaciones relacionadas con el manejo de objetos Elector. No tiene otras responsabilidades, lo que cumple con el SRP.
   ```
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
2. Open/Closed Principle:La **IListaServicio** está abierta para extensión (se puede crear nuevas implementaciones), pero cerrada para modificación. No se necesita modificar la interfaz para agregar nuevas funcionalidades.
    ```
    class IListaServicio(ABC):
    @abstractmethod
    def obtener_listas_pendientes(self):
        pass
    ```
3. Liskov Substitution Principle: **ListaServicioImpl** puede ser sustituida por cualquier otra implementación de **IListaServicio** sin alterar el comportamiento correcto del programa. Esto es asumido si todas las implementaciones de la interfaz siguen el contrato definido por **IListaServicio**.
   ```
    class ListaServicioImpl(IListaServicio):
    def obtener_listas_pendientes(self):
        listas = ListaCandidato.query.all()
        resultado = []
        
        for lista in listas:
            lista_info = {
                'id_lista': lista.id_lista,
                'nombre': lista.nombre,
                'estado': lista.estado.value,
                'id_eleccion': lista.id_eleccion,
                'propuestas': [{'descripcion': propuesta.descripcion} for propuesta in lista.propuestas],
                'candidatos': [{'nombre': f"{candidato.nombres} {candidato.apellido_paterno} {candidato.apellido_materno}"} for candidato in lista.candidatos]
            }
            
            resultado.append(lista_info)
        
        return resultado
   ```
4. Interface Segregation Principle: **ElectorServiceImpl** implementa todos los métodos definidos en **ElectorService.** Aunque la implementación actual utiliza todos los métodos, la interfaz podría estar segmentada para cumplir completamente con ISP
5. Dependency Inversion Principle:**ElectorServiceImpl** depende de la abstracción **ElectorService**
   ```
   class ElectorServiceImpl(ElectorService):
      def get_elector_by_id(self, id):
          try:
              return Elector.query.get(id)
          except Exception as e:
              logger.error(f'Error al obtener el elector por ID: {str(e)}')
              raise e
    
      def create_elector(self, elector_modelo):
          elector = Elector(
              nombres=elector_modelo.nombres,
              apellido_paterno=elector_modelo.apellido_paterno,
              apellido_materno=elector_modelo.apellido_materno,
              fecha_nacimiento=elector_modelo.fecha_nacimiento,
              usuario=elector_modelo.usuario,
              contrasena=elector_modelo.contrasena
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
   ```

