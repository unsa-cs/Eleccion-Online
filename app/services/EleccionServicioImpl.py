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

from app.models.Elector import Elector
from app.models.Voto import Voto

from app.models.Propuesta import Propuesta
from app.models.Propuesta import PropuestaSchema

from app.models.Prepropuesta import Prepropuesta
from app.models.Prepropuesta import PrepropuestaSchema
from app.models.Precandidato import Precandidato
from app.models.Precandidato import PrecandidatoSchema


from app.services.IEleccionServicio import IEleccionServicio

import logging
logger = logging.getLogger(__name__)

eleccion_schema = EleccionSchema()
eleccion_schemas = EleccionSchema(many = True)
candidato_schema = CandidatoSchema()

propuesta_schema = PropuestaSchema()
precandidato_schema = PrecandidatoSchema()
prepropuesta_schema = PrepropuestaSchema()

class EleccionServicioImpl(IEleccionServicio):
    def get_all_eleccion(self):
        try:
            all_eleccion = Eleccion.query.all()
            result = eleccion_schemas.dump(all_eleccion)
            return result
        except Exception as e:
            logger.error(f'Error al obtener todas las elecciones: {str(e)}')
            raise e
    
    def get_candidatos_by_eleccion(self, id_eleccion):
        try:
            all_candidatos = db.session.query(
                Candidato.nombres, 
                Candidato.apellido_paterno, 
                Candidato.apellido_materno, 
                ListaCandidato.nombre, 
                Candidato.id
            ).join(
                ListaCandidato, ListaCandidato.id_lista == Candidato.id_lista_candidato
            ).filter(
                ListaCandidato.id_eleccion == id_eleccion
            ).all()
            result = [{"Candidato": '%s %s %s' % (tupla[0], tupla[1], tupla[2]), "Lista": tupla[3], "id_candidato": tupla[4]} for tupla in all_candidatos]
            return result
        except Exception as e:
            logger.error(f'Error al obtener los candidatos por elección: {str(e)}')
            raise e
    
    def get_lista_by_eleccion(self, id_eleccion):
        try:
            all_listas = db.session.query(
                ListaCandidato.nombre, 
                ListaCandidato.id_lista
            ).filter(
                ListaCandidato.id_eleccion == id_eleccion
            ).all()
            result = [{"nombre": tupla[0], "id_lista": tupla[1]} for tupla in all_listas]
            return result
        except Exception as e:
            logger.error(f'Error al obtener las listas por elección: {str(e)}')
            raise e
    
    def get_all_eleccion_abiertas(self):
        try:
            all_eleccion = Eleccion.query.filter(Eleccion.estado == "abierto").all()
            result = eleccion_schemas.dump(all_eleccion)
            return result
        except Exception as e:
            logger.error(f'Error al obtener todas las elecciones abiertas: {str(e)}')
            raise e

    def insert_eleccion(self, eleccion):
        try:
            db.session.add(eleccion)
            db.session.commit()
            logger.info(f'Elección insertada correctamente: {eleccion}')
        except Exception as e:
            db.session.rollback()
            logger.error(f'Error al insertar la elección: {str(e)}')
            raise e

    def votar(self, id_lista, id_elector):
        try:
            voto = Voto(id_elector, id_lista)
            db.session.add(voto)
            db.session.commit()
            logger.info(f'Voto registrado correctamente: {voto}')
        except Exception as e:
            db.session.rollback()
            logger.error(f'Error al registrar el voto: {str(e)}')
            raise e

    def get_elector_by_email(self, email):
        try:
            elector = Elector.query.filter_by(correo=email).first()
            return elector
        except Exception as e:
            logger.error(f'Error al obtener el elector por email: {str(e)}')
            raise e

    def get_voto_by_elector(self, id_elector):
        try:
            voto = db.session.query(Elector.nombres).join(Voto, Elector.id == Voto.id_elector).filter(Elector.id == id_elector).all()
            result = [{"nombre": tupla[0]} for tupla in voto]
            return result
        except Exception as e:
            logger.error(f'Error al obtener el voto del elector: {str(e)}')
            raise e
    def get_candidatos_con_propuestas(self):
       
        candidatos = Candidato.query.options(db.joinedload(Candidato.propuestas)).all()
        
        result = []
        for candidato in candidatos:
            candidato_data = candidato_schema.dump(candidato)
            propuestas_data = propuesta_schema.dump(candidato.propuestas, many=True)
            candidato_data['propuestas'] = propuestas_data
            result.append(candidato_data)
        
        return result
    
    def get_precandidatos_denegados(self):
        precandidatos = Precandidato.query \
            .filter(Precandidato.denegado == -1) \
            .options(db.joinedload(Precandidato.prepropuestas)) \
            .all()
        
        result = []
        for precandidato in precandidatos:
            precandidato_data = precandidato_schema.dump(precandidato)
            prepropuestas_data = prepropuesta_schema.dump(precandidato.prepropuestas, many=True)
            precandidato_data['prepropuestas'] = prepropuestas_data
            result.append(precandidato_data)
        
        return result

    
    def get_precandidatos_inscritos(self):
        precandidatos = Precandidato.query\
            .filter(Precandidato.denegado == 0) \
            .options(db.joinedload(Precandidato.prepropuestas))\
            .all()

        result = []
        for precandidato in precandidatos:
            precandidato_data = precandidato_schema.dump(precandidato)
            prepropuestas_data = prepropuesta_schema.dump(precandidato.prepropuestas, many=True)
            precandidato_data['prepropuestas'] = prepropuestas_data
            result.append(precandidato_data)
        
        return result

