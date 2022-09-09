from sesions.db import db
from Modelos.ModeloPartido import ModeloPartido


class ControladorPartido():
    def __init__(selfself):
        print("Creando ControladorPartido")

    def index(self):
        try:
            partidos = ModeloPartido.query.all()
            datos = []
            for i in partidos:
                datos.append(i.resultado())
            return datos
        except Exception as ex:
            return {'message': str(ex)}, 500

    def create(self, elPartido):
        try:
            nombre = elPartido.get('nombre')
            lema = elPartido.get('lema')
            partido_create = ModeloPartido(nombre, lema)
            result_create = db.session.add(partido_create)
            db.session.commit()
            if result_create != 1:
                return {'message': 'Partido Creado'}
            else:
                return {'message': 'Error al registrar'}, 500

        except Exception as ex:
            return {'message': str(ex)}, 500

    def show(self, id):
        print("Mostrando un Partido con id ", id)
        partido_show = ModeloPartido.query.get(id)
        if partido_show is not None:
            result_show = ModeloPartido.resultado(partido_show)
            return result_show
        else:
            return {'message': 'no existe partido con id: ' + id}

    def update(self, id, elPartido):
        try:
            print("Actualizando Partido con id ", id)
            partidoupdate = ModeloPartido.query.get(id)
            partidoupdate.nombre = elPartido.get('nombre')
            partidoupdate.lema = elPartido.get('lema')
            db.session.add(partidoupdate)
            db.session.commit()
            return {'message': 'Partido con id: '+ id +' ha sido Actualizado'}

        except Exception as ex:
            return {'message': 'Partido con id: '+ id +' no existe'}

    def delete(self, id):
        try:
            print("Elimiando Partido con id ", id)
            partidodelete = ModeloPartido.query.get(id)
            db.session.delete(partidodelete)
            db.session.commit()
            return {'message': 'Partido con id: '+ id +' ha sido Eliminado'}

        except Exception as ex:
            return {'message': 'Partido con id: '+ id +' no existe'}



