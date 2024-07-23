from app import db
from sqlalchemy import Enum

class Eleccion(db.Model):
    id_eleccion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha = db.Column(db.Date, nullable=True)
    hora_inicio = db.Column(db.Time, nullable=True)
    hora_fin = db.Column(db.Time, nullable=True)
    estado = db.Column(Enum('abierto', 'cerrado', name='estado_enum'), nullable=True)
    descripcion = db.Column(db.String(100), nullable=True)
    listas = db.relationship('ListaCandidato', backref=("eleccion"))
    def __init__(self, fecha, hora_inicio, hora_fin, estado, descripcion):
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.estado = estado
        self.descripcion = descripcion