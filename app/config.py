# config.py

class Config:
    # Configuración de la base de datos MySQL
    SQLALCHEMY_DATABASE_URI = 'mysql://root:chuancao26@localhost/eleccion'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desactivar el seguimiento de modificaciones
