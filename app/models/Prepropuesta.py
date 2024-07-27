from app import db
from app import ma

class Prepropuesta(db.Model):
    __tablename__ = 'prepropuesta'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_precandidato = db.Column(db.Integer, db.ForeignKey('precandidato.id'), nullable=False)
    prepropuesta = db.Column(db.Text, nullable=False)

    def __init__(self, id_precandidato, prepropuesta):
        self.id_precandidato = id_precandidato
        self.prepropuesta = prepropuesta
    from app import ma

class PrepropuestaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Prepropuesta
        fields = (
            'id',
            'id_precandidato',
            'prepropuesta'
        )


