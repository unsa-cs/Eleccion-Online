# app/repositories/mysql_persona_repository.py

from domain.persona.modelo.Elector import Elector
from app import db

class MySqlElectorRepository:
    def create_elector(self, elector):
        try:
            db.session.add(elector)
            db.session.commit()
            return elector
        except Exception as e:
            db.session.rollback()
            raise e

    def get_elector_by_id(self, id):
        return Elector.query.get(id)

    def update_elector(self, updated_elector):
        try:
            elector = Elector.query.get(updated_elector.id)
            if elector:
                elector.nombres = updated_elector.nombres
                elector.apellido_paterno = updated_elector.apellido_paterno
                elector.apellido_materno = updated_elector.apellido_materno
                elector.fecha_nacimiento = updated_elector.fecha_nacimiento
                elector.usuario = updated_elector.usuario
                db.session.commit()
                return elector
            else:
                return None
        except Exception as e:
            db.session.rollback()
            raise e

    def delete_elector(self, elector):
        try:
            db.session.delete(elector)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
