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