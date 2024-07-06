from flask import Flask
from app.blueprints.home.routes import home_bp

def create_app():
    app = Flask(__name__)
    
    # Configuración de otros aspectos de la aplicación, como bases de datos, etc.

    # Registrar blueprints
    app.register_blueprint(home_bp)

    return app
