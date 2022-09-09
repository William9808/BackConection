from flask import Flask, jsonify, request, Blueprint
from Controladores.ControladorCandidato import ControladorCandidato

miControladorCandidato=ControladorCandidato()

candidato = Blueprint('candidato', __name__)

@candidato.route('/candidatos', methods=['GET'])
def getCandidatos():
    json = miControladorCandidato.index()
    return jsonify(json)


@candidato.route("/candidato",methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json=miControladorCandidato.create(data)
    return jsonify(json)


@candidato.route("/candidato/<string:id>",methods=['GET'])
def getCandidato(id):
    json=miControladorCandidato.show(id)
    return jsonify(json)


@candidato.route("/candidato/<string:id>",methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json=miControladorCandidato.update(id,data)
    return jsonify(json)


@candidato.route("/candidato/<string:id>",methods=['DELETE'])
def eliminarCandidato(id):
    json=miControladorCandidato.delete(id)
    return jsonify(json)
