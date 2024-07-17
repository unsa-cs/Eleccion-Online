# config.py

class Config:
    # Configuración de la base de datos MySQL
    SQLALCHEMY_DATABASE_URI = 'mysql://root:admin@localhost/eleccion'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desactivar el seguimiento de modificaciones
