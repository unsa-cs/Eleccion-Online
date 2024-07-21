#!/usr/bin/python
#-*- coding: utf-8 -*-
from flask import jsonify
from app.models.Eleccion import Eleccion
from app.models.Eleccion import EleccionSchema

from app import ma

from app.services.IEleccionServicio import IEleccionServicio

eleccion_schema = EleccionSchema()
eleccion_schemas = EleccionSchema(many = True)


class EleccionServicioImpl(IEleccionServicio):
    def get_all_eleccion(self):
        all_eleccion = Eleccion.query.all()
        result = eleccion_schemas.dump(all_eleccion)
        return jsonify(result)