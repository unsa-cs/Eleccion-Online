from app import db
from app import ma
class Propuesta(db.Model):
    __tablename__ = 'propuesta'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_candidato = db.Column(db.Integer, db.ForeignKey('candidato.id'), nullable=False)
    propuesta = db.Column(db.Text, nullable=False)

    def __init__(self, id_candidato, propuesta):
        self.id_candidato = id_candidato
        self.propuesta = propuesta
    from app import ma

class PropuestaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Propuesta
        fields = (
            'id',
            'id_candidato',
            'propuesta'
        )


