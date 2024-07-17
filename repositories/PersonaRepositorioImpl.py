from app import db
from domain.persona.modelo.Elector import Elector
from domain.persona.IPersonaRepositorio import IPersonaRepositorio

class ElectorRepository(IPersonaRepositorio):
    
    def create(self, elector: Elector) -> Elector:
        db.session.add(elector)
        db.session.commit()
        return elector
    
    def get_by_id(self, id: int) -> Elector:
        return Elector.query.get(id)
    
    def update(self, elector: Elector) -> Elector:
        db.session.commit()
        return elector
    
    def delete(self, elector: Elector) -> None:
        db.session.delete(elector)
        db.session.commit()
