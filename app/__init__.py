from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, static_folder='static', static_url_path='/static')
    app.config.from_object('app.config.Config')

    logging.basicConfig(level=logging.INFO)
    
    db.init_app(app)
    migrate = Migrate(app, db)

    from app.blueprints.home.routes import home_bp
    app.register_blueprint(home_bp)

    return app
