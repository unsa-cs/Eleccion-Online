from app import db
from app import ma

class ListaCandidato(db.Model):
    __tablename__ = 'lista_candidato'
    id_lista = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=True)
    id_eleccion = db.Column(db.Integer, db.ForeignKey('eleccion.id_eleccion'), nullable=True)
    
    votos = db.relationship('Voto', backref=("lista_candidato"))
    lista_candidato = db.relationship('Candidato', backref=("lista_candidato"))

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