#!/usr/bin/python
#-*- coding: utf-8 -*-
from app.models.Eleccion import Eleccion
from app import db
from app.services.IEleccionServicio import IEleccionServicio

class EleccionServicioImpl(IEleccionServicio):
    def get_all_eleccion(self):
        return Eleccion.query.all()