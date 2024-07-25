from app import db
from app.models.Eleccion import Eleccion
from app.models.Eleccion import EleccionSchema
from app.models.Candidato import Candidato
from app.models.Candidato import CandidatoSchema
from app.models.ListaCandidato import ListaCandidato

from app.services.IEleccionServicio import IEleccionServicio
from app.services.IEleccionServicio import IListaServicio

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


