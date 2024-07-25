from abc import ABC, abstractmethod

class IEleccionServicio(ABC):
    @abstractmethod
    def get_all_eleccion(self):
        pass
    @abstractmethod
    def get_candidatos_by_eleccion(self, int):
        pass

class IListaServicio(ABC):
    @abstractmethod
    def obtener_listas_pendientes(self):
        pass