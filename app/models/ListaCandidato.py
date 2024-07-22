from app import db
from app import ma

class ListaCandidato(db.Model):
    __tablename__ = 'listaCandidato'
    id_lista = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.Integer, nullable=True)
    id_eleccion = db.Column(db.Integer, db.ForeignKey('eleccion.id_eleccion'), nullable=True)
    lista_voto = db.relationship('Voto', backref=("lista_voto"))

    def __init__(self, nombre, id_eleccion):
        self.nombre = nombre
        self.id_eleccion = id_eleccion

