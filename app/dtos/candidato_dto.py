# app/dtos/candidato_dto.py

class CandidatoDTO:
    def __init__(self, nombres, apellido_paterno, apellido_materno, propuesta):
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.propuesta = propuesta
