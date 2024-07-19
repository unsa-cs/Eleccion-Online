#!/usr/bin/python
#-*- coding: utf-8 -*-

from domain.persona.modelo.Persona import Persona

class Candidato(Persona):
    __tablename__ = 'candidato'

    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(100), nullable=False)
    apellido_paterno = db.Column(db.String(100), nullable=False)
    apellido_materno = db.Column(db.String(100), nullable=False)
    propuesta = db.Column(db.string(250), nullable=False)


    def __init__(self, nombres, apellido_paterno, apellido_materno, propuesta):
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.propuesta = propuesta

    def registrar_lista(self, elector_id):
        # Lógica para registrar lista
        pass

