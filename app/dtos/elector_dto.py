# app/dtos/elector_dto.py

class ElectorDTO:
    def __init__(self, nombres, apellido_paterno, apellido_materno, fecha_nacimiento, usuario, contrasena):
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.fecha_nacimiento = fecha_nacimiento
        self.usuario = usuario
        self.contrasena = contrasena
