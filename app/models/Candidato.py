from app import db
from app import ma

class Candidato(db.Model):
    __tablename__ = 'candidato'
    id_candidato  = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(100), nullable=False)
    apellido_paterno = db.Column(db.String(100), nullable=False)
    apellido_materno = db.Column(db.String(100), nullable=False)
<<<<<<< HEAD
    denegado = db.Column(db.Boolean, nullable=True, default=False)
    id_lista = db.Column(db.Integer, db.ForeignKey('listacandidato.id_lista'),nullable=True)
    
    def __init__(self, nombres, apellido_paterno, apellido_materno, id_lista_canditado,denegado=False):
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.id_lista_candidato = id_lista_canditado
        self.denegado = denegado
=======
    rol = db.Column(db.String(100), nullable=False)
    id_lista = db.Column(db.Integer, db.ForeignKey('lista_candidato.id_lista'),nullable=True)
    
    def __init__(self, nombres, apellido_paterno, apellido_materno, rol, id_lista):
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.rol = rol
        self.id_lista = id_lista
    
>>>>>>> 5dab012c8a63bedde4edc3f7c992bb60918a129e
    
class CandidatoSchema(ma.Schema):
    class Meta:
        fields = (
            'id_candidato',
            'nombres',
            'apellido_paterno',
            'apellido_materno',
<<<<<<< HEAD
            'denegado',
=======
            'rol',
>>>>>>> 5dab012c8a63bedde4edc3f7c992bb60918a129e
            'id_lista'
        )