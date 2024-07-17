#!/usr/bin/python
#-*- coding: utf-8 -*-

class IPersonaRepositorio:
    pass
from abc import ABC, abstractmethod
from domain.persona.modelo.Elector import Elector

class IPersonaRepositorio(ABC):
    
    @abstractmethod
    def create(self, elector: Elector) -> Elector:
        pass
    
    @abstractmethod
    def get_by_id(self, id: int) -> Elector:
        pass
    
    @abstractmethod
    def update(self, elector: Elector) -> Elector:
        pass
    
    @abstractmethod
    def delete(self, elector: Elector) -> None:
        pass
