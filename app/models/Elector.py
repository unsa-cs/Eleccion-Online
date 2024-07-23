from app import db
from app import ma

class Elector(db.Model):
    __tablename__ = 'elector'

    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(100), nullable=False)
    apellido_paterno = db.Column(db.String(100), nullable=False)
    apellido_materno = db.Column(db.String(100), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    usuario = db.Column(db.String(50), unique=True, nullable=False)
    contrasena = db.Column(db.String(100), nullable=False)
    voto = db.relationship('voto', backref=("voto"))

    def __init__(self, nombres, apellido_paterno, apellido_materno, fecha_nacimiento, usuario, contrasena):
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.fecha_nacimiento = fecha_nacimiento
        self.usuario = usuario
        self.contrasena = contrasena

class ElectorSchema(ma.Schema):
    class Meta:
        fields = (
            'id',
            'nombres',
            'apellido_paterno',
            'apellido_materno',
            'fecha_nacimiento',
            'usuario',
            'voto',
        )