from app import db
from app import ma

class Precandidato(db.Model):
    __tablename__ = 'precandidato'
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(100), nullable=False)
    apellido_paterno = db.Column(db.String(100), nullable=False)
    apellido_materno = db.Column(db.String(100), nullable=False)
    id_lista_precandidato = db.Column(db.Integer, db.ForeignKey('lista_precandidato.id_lista'),nullable=True)
    denegado = db.Column(db.Integer, nullable=False)
    def __init__(self, nombres, apellido_paterno, apellido_materno, id_lista_precandidato, denegado):
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.id_lista_precandidato = id_lista_precandidato
        self.denegado = denegado

    prepropuestas = db.relationship('Prepropuesta', backref='precandidato', lazy=True)
    
class PrecandidatoSchema(ma.Schema):
    class Meta:
        fields = (
            'id',
            'nombres',
            'apellido_paterno',
            'apellido_materno',
            'id_lista_precandidato',
            'denegado'
        )