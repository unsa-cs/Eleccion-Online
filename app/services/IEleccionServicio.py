#!/usr/bin/python
#-*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class IEleccionServicio(ABC):
    @abstractmethod
    def get_all_eleccion(self):
        pass
    @abstractmethod
    def get_candidatos_by_eleccion(self, int):
        pass
    @abstractmethod
    def get_all_eleccion_abiertas(self):
        pass
    @abstractmethod
    def insert_eleccion(self, eleccion):
        pass
    
