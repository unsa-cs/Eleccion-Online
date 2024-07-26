#!/usr/bin/python
#-*- coding: utf-8 -*-
from app import db
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
    def get_candidatos_by_eleccion(self):
        all_candidatos = db.session.query(Candidato.nombres, ListaCandidato.nombre).join(ListaCandidato, ListaCandidato.id_lista == Candidato.id_lista_candidato).all()
        return all_candidatos


