# app/services/persona_service_impl.py

import logging
from repositories.mysql_persona_repository import MySqlElectorRepository
from services.IPersonaServicio import ElectorService
from domain.persona.modelo.Elector import Elector
from app.dtos.elector_dto import ElectorDTO

elector_repository = MySqlElectorRepository()
logger = logging.getLogger(__name__) 

class ElectorServiceImpl(ElectorService):
    def get_elector_by_id(self, id):
        return elector_repository.get_elector_by_id(id)

    def create_elector(self, elector_dto: ElectorDTO):
        elector = Elector(
            nombres=elector_dto.nombres,
            apellido_paterno=elector_dto.apellido_paterno,
            apellido_materno=elector_dto.apellido_materno,
            fecha_nacimiento=elector_dto.fecha_nacimiento,
            usuario=elector_dto.usuario,
            contrasena=elector_dto.contrasena
        )
        try:
            elector_repository.create_elector(elector)
            logger.info(f'Elector creado correctamente: {elector}')  # Log para la creación exitosa
            return elector
        except Exception as e:
            logger.error(f'Error al crear el elector: {str(e)}')
            raise e

    def update_elector(self, elector):
        elector_repository.update_elector(elector)

    def delete_elector(self, elector):
        elector_repository.delete_elector(elector)
