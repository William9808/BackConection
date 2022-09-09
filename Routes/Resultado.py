from flask import Flask, jsonify, request, Blueprint
from Controladores.ControladorResultado import ControladorResultado

miControladorResultado=ControladorResultado()

resultado = Blueprint('resultado', __name__)

@resultado.route('/resultados', methods=['GET'])
def getResultados():
    json = miControladorResultado.index()
    return jsonify(json)


@resultado.route("/resultado",methods=['POST'])
def crearResultado():
    data = request.get_json()
    json=miControladorResultado.create(data)
    return jsonify(json)


@resultado.route("/resultado/<string:id>",methods=['GET'])
def getCandidato(id):
    json=miControladorResultado.show(id)
    return jsonify(json)


@resultado.route("/resultado/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json=miControladorResultado.update(id,data)
    return jsonify(json)


'''@candidato.route("/candidato/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    json=miControladorCandidato.delete(id)
    return jsonify(json)'''