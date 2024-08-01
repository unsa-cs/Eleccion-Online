# **Proyecto Final: Votaciones Online**

**Equipo:** Los Refugiados

**Miembros:**

-   Arleen Maritza Ferro Vasquez
-   Wilson Isaac Mamani Casilla
-   Jazmin Gabriela Perez Villasante
-   Cristhian David Huanca Olazabal
-   Sebastian Andres Mendoza Fernandez
-   Edilson Bonet Mamani Yucra

## Especificación del Proyecto

El Proyecto Final debe implementar una aplicación web con las siguientes características:

### Funcionalidades

-   **Interfaz gráfica de usuario**: Utilizando cualquier lenguaje, biblioteca o framework.
-   **Persistencia en bases de datos**: Soporte para MySQL, SQLite, MongoDB u otro sistema de bases de datos.

### Requisitos de desarrollo

-   **Patrones/Estilos de arquitectura de software**:
    -   Uso de patrones de diseño adecuados.
    -   Arquitectura escalable y mantenible.
-   **Prácticas de desarrollo de software**:
    -   **Estilos de codificación**: Adherencia a guías de estilo para el lenguaje elegido.
    -   **Codificación Limpia (Clean Code)**: Código legible, mantenible y con buena organización.
    -   **Principios SOLID**: Aplicación de los principios de diseño de software.
    -   **Domain-Driven Design (DDD)**: Diseño orientado al dominio para modelar el negocio de manera efectiva.

## Entregible

### Proyecto (codigo fuente y documentacion) en Github

Puedes encontrar el código fuente y la documentación del proyecto en el siguiente enlace:
[Elección Online - GitHub](https://github.com/Aferrov/Eleccion-Online)

### Planificación de Tareas

La planificación de tareas de implementación se gestiona usando la herramienta Trello. Puedes ver el tablero con todas las tareas del proyecto en el siguiente enlace:
[Sistema de Elecciones - Trello](https://trello.com/b/dr4vfErF/sistema-de-elecciones)

### Documento de requisitos de software actualizado

Enlace

### Documento de arquitectura de software actualizado

Enlace

### Documentacion del Proyecto en GitHub

#### Proposito del proyecto

El propósito de este proyecto es desarrollar una aplicación web de votaciones online que permita a los usarios participar en procesos electorales de manera segura y eficiente. La aplicación está diseñada para:

-   **Facilitar el voto en linea:** Proporcionar una plataforma intuitiva y accesible para que los votantes puedan emitir su voto desde cualquier lugar y momento.
-   **Promover la transparencia:** Asegurar que todo el proceso sea transparente y verificable, permitiendo a los participantes y organizadores auditar y revisar los resultados.
-   **Mejorar la gestion electoral:** Ofrecer herramientas para la administracion y supervision de las votaciones, simplificando la organizacion y el conteo de votos.
-   **Garantizar la integridad y seguridad:** Implementar medidas robustas para asegurar que el proceso de votacion sea seguro y que los resultados sean precisos y confiables.

#### Funcionalidades: Diagrama de Casos de Uso, Funcionalidades de Alto Nivel y Prototipo (o GUI)

![Diagrama](img/img1.jpeg)

#### Modelo de Dominio: Diagrama de Clases y Módulos

![Diagrama](img/img1.jpeg)

#### Arquitectura y Patrones: Diagrama de Componentes o Paquetes

![Diagrama](img/img1.jpeg)

#### **Prácticas de codificación limpia aplicadas:**

**1. Nombres Descriptivos**

Las clases y métodos tienen nombres claros y descriptivos, lo que facilita la comprensión del propósito del código. Ejemplos incluyen:

-   Clases como `Elector`, `Candidato`.
-   Métodos como `hash_contrasena`, `revisar_contrasena`, y `emitir_voto`.

```Python
class Elector(db.Model):
    # ...

    def hash_contrasena(self, contrasena):
        return bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def revisar_contrasena(self, contrasena):
        return bcrypt.checkpw(contrasena.encode('utf-8'), self.contrasena.encode('utf-8'))

    def emitir_voto(self, candidato_id):
        # Lógica para emitir el voto
        pass
```

-   **Nombres Descriptivos:** Las clases y métodos tienen nombres claros y descriptivos, lo que facilita la comprensión del propósito del código. Como por ejemplo, `Elector`, `Candidato`, y `hash_contrasena`.
-   **Funciones Pequeñas:** Los métodos están diseñados para realizar tareas específicas y bien definidas, como `hash_contrasena`, `revisar_contrasena`, y `emitir_voto`.
-   **Encapsulación:** La lógica de manejo de contraseñas y emisión de votos está contenida dentro de las clases `Elector` y `Candidato`.

```Python
class Elector(db.Model):
    # ...

    def hash_constrasena(self, contrasena):
        return bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def revisar_contrasena(self, contrasena):
        return bcrypt.checkpw(contrasena.encode('utf-8'), self.contrasena.encode('utf-8'))

    def emitir_voto(self, candidato_id):
        # Lógica para emitir el voto
        pass
```

-   **Manejo de Excepciones:** El uso de bloques try-except para manejar excepciones y registrar errores es una buena práctica para asegurar que el sistema maneje errores de manera controlada y registre información útil para la depuración.
-   **Nombres Descriptivos:** Los métodos y clases tienen nombres claros que indican su propósito, como get_all_eleccion, insert_eleccion, y votar.
-   **Responsabilidad Única:** Cada clase tiene una sola responsabilidad, como manejar elecciones (EleccionServicioImpl), votos (VotoServicioImpl), candidatos (CandidatoServicioImpl), y listas (ListaServicioImpl).

```Python
class EleccionServicioImpl(IEleccionServicio):
    def get_all_eleccion(self, modo):
        try:
            # Lógica para obtener elecciones según el modo
        except Exception as e:
            logger.error(f'Error al obtener todas las elecciones: {str(e)}')
            raise e
```

#### Estilos de Programación aplicados:

-   **Consistencia:** Se sigue un estilo consistente en la definición de las clases y los métodos.
-   **Uso de ORM:** Se utiliza SQLAlchemy para manejar la persistencia de datos, que es un estilo moderno y limpio para interactuar con bases de datos en Python.

```Python
class Candidato(db.Model):
    __tablename__ = 'candidato'
    id_candidato  = db.Column(db.Integer, primary_key=True)
    # ...

    def __init__(self, nombres, apellido_paterno, apellido_materno, rol, id_lista_candidato, denegado=False):
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.denegado = denegado
        self.rol = rol
        self.id_lista = id_lista_candidato

```

#### Principios SOLID aplicados:

-   **Responsabilidad Única (SRP):** Cada clase tiene una sola responsabilidad. `Elector` maneja la información del votante y su autenticación, mientras que `Candidato` maneja los detalles de un candidato.
-   **Abierto/Cerrado (OCP):** Las clases están abiertas para extensión pero cerradas para modificación. Puedes agregar nuevos métodos sin modificar las clases existentes.
-   **Sustitución de Liskov (LSP):** No se aplican herencias explícitas en este fragmento, pero las clases y métodos están diseñados para ser reemplazables sin alterar el comportamiento del programa.
-   **Segregación de Interfaces (ISP):** Los métodos en las clases están diseñados para cumplir con una sola tarea, evitando la creación de interfaces grandes e inútiles.
-   **Inversión de Dependencias (DIP):** Aunque este código no muestra una dependencia explícita, el uso de la base de datos a través de SQLAlchemy permite abstraer la capa de persistencia.

#### Conceptos DDD aplicados:

-   **Entidades:** Elector y Candidato son ejemplos de entidades que representan objetos del dominio con una identidad propia.
-   **Objetos de Valor:** En este código no se muestran objetos de valor, pero podrían ser implementados para representar conceptos inmutables.
-   **Servicios de Dominio:** La lógica de negocio relacionada con la autenticación y votación podría ser encapsulada en servicios de dominio, aunque en este fragmento no están explícitamente presentes.
-   **Agregados y Módulos:** Elector y Candidato podrían formar parte de un agregado en el dominio electoral, agrupando datos relacionados.
-   **Fábricas y Repositorios:** En este fragmento, la persistencia de datos está manejada por SQLAlchemy, actuando como un repositorio. Las fábricas no están implementadas aquí, pero podrían ser usadas para crear instancias de entidades.
-   **Arquitectura en Capas:** La separación de la lógica de la aplicación y la persistencia de datos muestra una estructura de capas. Elector y Candidato representan el modelo del dominio, mientras que db.Model se encarga de la persistencia.

```Python
class Elector(db.Model):
    # ...

class Candidato(db.Model):
    # ...
```
