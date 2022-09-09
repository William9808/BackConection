from sesions.db import db
from Modelos.ModeloMesa import ModeloMesa


class ControladorMesa():
    def __init__(selfself):
        print("Creando ControladorMesa")

    def index(self):
        try:
            mesas = ModeloMesa.query.all()
            datos = []
            for i in mesas:
                datos.append(i.resultado())
            return datos
        except Exception as ex:
            return {'message': str(ex)}, 500

    def create(self, elMesa):
        try:
            idmesa = elMesa.get('idmesa')
            cant_inscritos = elMesa.get('cant_inscritos')
            mesa_create = ModeloMesa(idmesa, cant_inscritos)
            result_create = db.session.add(mesa_create)
            db.session.commit()
            print(result_create)
            if result_create != 1:
                return {'message': 'Mesa Creada'}
            else:
                return {'message': 'Error al registrar'}, 500

        except Exception as ex:
            return {'message': str(ex)}, 500

    def show(self, id):
        print("Mostrando un Mesa con número: ", id)
        mesa_show = ModeloMesa.query.get(id)
        if mesa_show is not None:
            result_show = ModeloMesa.resultado(mesa_show)
            return result_show
        else:
            return {'message': 'no existe número de mesa: ' + id}

    def update(self, id, elMesa):
        try:
            print("Actualizando número de Mesa: ", id)
            mesaupdate = ModeloMesa.query.get(id)
            mesaupdate.idmesa = elMesa.get('idmesa')
            mesaupdate.cant_inscritos = elMesa.get('cant_inscritos')
            db.session.add(mesaupdate)
            db.session.commit()
            return {'message': 'Mesa número: '+ id +' ha sido Actualizada'}

        except Exception as ex:
            return {'message': 'Mesa con número: '+ id +' no existe'}

    def delete(self, id):
        try:
            print("Elimiando Mesa con id ", id)
            mesadelete = ModeloMesa.query.get(id)
            db.session.delete(mesadelete)
            db.session.commit()
            return {'message': 'Mesa número: '+ id +' ha sido Eliminada'}

        except Exception as ex:
            return {'message': 'Mesa número: '+ id +' no existe'}