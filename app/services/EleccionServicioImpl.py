#!/usr/bin/python
#-*- coding: utf-8 -*-
from app import db
from flask import jsonify

from app.models.Eleccion import Eleccion
from app.models.Eleccion import EleccionSchema
from app.models.Candidato import Candidato
from app.models.Candidato import CandidatoSchema
from app.models.ListaCandidato import ListaCandidato
from app.models.ListaCandidato import ListaCanditadoSchema



from app.services.IEleccionServicio import IEleccionServicio

eleccion_schema = EleccionSchema()
eleccion_schemas = EleccionSchema(many = True)


class EleccionServicioImpl(IEleccionServicio):
    def get_all_eleccion(self):
        all_eleccion = Eleccion.query.all()
        result = eleccion_schemas.dump(all_eleccion)
        return result
    
    def get_candidatos_by_eleccion(self, id_eleccion):
        all_candidatos = db.session.query(Candidato.nombres, Candidato.apellido_paterno, Candidato.apellido_materno, ListaCandidato.nombre, Candidato.id).join(ListaCandidato, ListaCandidato.id_lista == Candidato.id_lista_candidato).filter(ListaCandidato.id_eleccion == id_eleccion).all()
        result = [{"Candidato": '%s %s %s' % (tupla[0], tupla[1], tupla[2]), "Lista": tupla[3], "id_candidato": tupla[4]} for tupla in all_candidatos]
        return result
    
    def get_all_eleccion_abiertas(self):
        all_eleccion = Eleccion.query.filter(Eleccion.estado == "abierto").all()
        result = eleccion_schemas.dump(all_eleccion)
        return result
    

    def insert_eleccion(self, eleccion):
        db.session.add(eleccion)
        db.session.commit()

