from app import db
from flask import jsonify

from app.models.Eleccion import Eleccion
from app.models.Eleccion import EleccionSchema
from app.models.Candidato import Candidato
from app.models.Candidato import CandidatoSchema
from app.models.ListaCandidato import ListaCandidato
from app.models.Propuesta import Propuesta
from app.models.Propuesta import PropuestaSchema
from app.models.Prepropuesta import Prepropuesta
from app.models.Prepropuesta import PrepropuestaSchema
from app.models.Precandidato import Precandidato
from app.models.Precandidato import PrecandidatoSchema

from app.services.IEleccionServicio import IEleccionServicio
from app.services.IEleccionServicio import IListaServicio

candidato_schema = CandidatoSchema()
eleccion_schema = EleccionSchema()
eleccion_schemas = EleccionSchema(many = True)
propuesta_schema = PropuestaSchema()
precandidato_schema = PrecandidatoSchema()
prepropuesta_schema = PrepropuestaSchema()

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

class ListaServicioImpl(IListaServicio):
    def obtener_listas_pendientes(self):
        listas = ListaCandidato.query.all()
        resultado = []
        
        for lista in listas:
            lista_info = {
                'id_lista': lista.id_lista,
                'nombre': lista.nombre,
                'estado': lista.estado.value,
                'id_eleccion': lista.id_eleccion,
                'propuestas': [{'descripcion': propuesta.descripcion} for propuesta in lista.propuestas],
                'candidatos': [{'nombre': f"{candidato.nombres} {candidato.apellido_paterno} {candidato.apellido_materno}"} for candidato in lista.candidatos]
            }
            
            resultado.append(lista_info)
        
        return resultado

