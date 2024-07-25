from app import db

class Propuesta(db.Model):
    __tablename__ = 'propuesta'
    id_propuesta = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descripcion = db.Column(db.String(255), nullable=True)
    id_lista = db.Column(db.Integer, db.ForeignKey('listacandidato.id_lista'), nullable=True)
    
    def __init__(self, descripcion, id_lista):
        self.descripcion = descripcion
        self.id_lista = id_lista
