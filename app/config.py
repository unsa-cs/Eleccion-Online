import os

class Config:
    # Configuración de la base de datos MySQL
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI_S')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desactivar el seguimiento de modificaciones
    SECRET_KEY = os.environ.get('SECRET_KEY_S', 'default_secret_key')  # Obtener desde variables de entorno