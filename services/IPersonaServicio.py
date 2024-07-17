# app/services/persona_service.py

from abc import ABC, abstractmethod
from app.dtos.elector_dto import ElectorDTO
from domain.persona.modelo.Elector import Elector

class ElectorService(ABC):
    @abstractmethod
    def get_elector_by_id(self, id):
        pass

    @abstractmethod
    def create_elector(self, elector_dto: ElectorDTO):
        pass

    @abstractmethod
    def update_elector(self, elector):
        pass

    @abstractmethod
    def delete_elector(self, elector):
        pass
