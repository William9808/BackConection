from sesions.db import db
from Modelos.ModeloCandidato import ModeloCandidato


class ControladorCandidato():
    def __init__(self):
        print("Creando ControladorCandidato")

    def index(self):
        try:
            candidatos = ModeloCandidato.query.all()
            datos = []
            for i in candidatos:
                datos.append(i.resultado())
            return datos
        except Exception as ex:
            return {'message': str(ex)}, 500

    def create(self, elCandidato):
        try:
            cedula = elCandidato.get('cedula')
            nombre = elCandidato.get('nombre')
            apellido = elCandidato.get('apellido')
            numlista = elCandidato.get('numlista')
            idpartido = elCandidato.get('idpartido')
            candidato_create = ModeloCandidato(cedula, nombre, apellido, numlista, idpartido)
            result_create = db.session.add(candidato_create)
            db.session.commit()
            if result_create != 1:
                return {'message': 'Candidato Creado'}
            else:
                return {'message': 'Error al registrar'}, 500

        except Exception as ex:
            return {'message': 'Error: El candidato Ya existe'}

    def show(self, id):
        print("Mostrando un Candidato con id ", id)
        candidato_show = ModeloCandidato.query.get(id)
        if candidato_show is not None:
            result_show = ModeloCandidato.resultado(candidato_show)
            return result_show
        else:
            return {'message': 'no existe candidato con id: ' + id}

    def update(self, id, elCandidato):
        try:
            print("Actualizando Candidato con id ", id)
            candidatoupdate = ModeloCandidato.query.get(id)
            candidatoupdate.cedula = elCandidato.get('cedula')
            candidatoupdate.nombre = elCandidato.get('nombre')
            candidatoupdate.apellido = elCandidato.get('apellido')
            candidatoupdate.numlista = elCandidato.get('numlista')
            candidatoupdate.idpartido = elCandidato.get('idpartido')
            db.session.add(candidatoupdate)
            db.session.commit()
            return {'message': 'Candidato con id: '+ id +' ha sido Actualizado'}

        except Exception as ex:
            # return {'message': 'Candidato con id: '+ id +' no existe'}
            return {'message': str(ex)}

    def delete(self, id):
        try:
            print("Elimiando candidato con id ", id)
            candidatodelete = ModeloCandidato.query.get(id)
            db.session.delete(candidatodelete)
            db.session.commit()
            return {'message': 'Candidato con id: '+ id +' ha sido Eliminado'}

        except Exception as ex:
            return {'message': 'Candidato con id: '+ id +' no existe'}



