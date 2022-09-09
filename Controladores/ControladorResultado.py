from sesions.db import db
from Modelos.ModeloResultado import ModeloResultado

class ControladorResultado():
    def __init__(selfself):
        print("Creando ControladorResultado")

    def index(self):
        try:
            resultados = ModeloResultado.query.all()
            datos = []
            for i in resultados:
                datos.append(i.resultado())
            return datos
        except Exception as ex:
            return {'message': str(ex)}, 500

    def create(self, elResultado):
        try:
            idmesa = elResultado.get('idmesa')
            idcandidato = elResultado.get('idcandidato')
            resultado_create = ModeloResultado(idmesa, idcandidato)
            result_create = db.session.add(resultado_create)
            db.session.commit()
            if result_create != 1:
                return {'message': 'Resultado Registrado'}
            else:
                return {'message': 'Error al registrar'}, 500

        except Exception as ex:
            return {'message': str(ex)}, 500

    def show(self, id):
        print("Mostrando Resultado con id ", id)
        resultado_show = ModeloResultado.query.get(id)
        if resultado_show is not None:
            result_show = ModeloResultado.resultado(resultado_show)
            return result_show
        else:
            return {'message': 'no existe registro con id: ' + id}

    def update(self, id, elResultado):
        try:
            print("Actualizando Resultado con id ", id)
            resultadoupdate = ModeloResultado.query.get(id)
            resultadoupdate.idmesa = elResultado.get('idmesa')
            resultadoupdate.idcandidato = elResultado.get('idcandidato')
            db.session.add(resultadoupdate)
            db.session.commit()
            return {'message': 'Resultado con id: '+ id +' ha sido Actualizado'}

        except Exception as ex:
            return {'message': 'Resultado con id: '+ id +' no existe'}

    '''def delete(self,id):
        print("Elimiando Partido con id ",id)'''