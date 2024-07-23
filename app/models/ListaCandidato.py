from app import db
from app import ma

class ListaCandidato(db.Model):
    __tablename__ = 'lista_candidato'
    id_lista = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.Integer, nullable=True)
    id_eleccion = db.Column(db.Integer, db.ForeignKey('eleccion.id_eleccion'), nullable=True)
    lista_voto = db.relationship('voto', backref=("lista_voto"))
    lista_candidato = db.relationship('candidato', backref=("canditado_lista"))

    def __init__(self, nombre, id_eleccion):
        self.nombre = nombre
        self.id_eleccion = id_eleccion

class ListaCanditadoSchema(ma.Schema):
    class Meta:
        fields = (
            'id_lista',
            'nombre',
            'id_eleccion',
            'lista_voto'
        )