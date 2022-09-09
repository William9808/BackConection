from flask import Flask, jsonify, request, Blueprint
from Controladores.ControladorMesa import ControladorMesa

miControladorMesa=ControladorMesa()

mesa = Blueprint('mesa', __name__)

@mesa.route('/mesas', methods=['GET'])
def getMesas():
    json = miControladorMesa.index()
    return jsonify(json)


@mesa.route("/mesa",methods=['POST'])
def crearMesa():
    data = request.get_json()
    json=miControladorMesa.create(data)
    return jsonify(json)


@mesa.route("/mesa/<string:id>",methods=['GET'])
def getMesa(id):
    json=miControladorMesa.show(id)
    return jsonify(json)


@mesa.route("/mesa/<string:id>",methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json=miControladorMesa.update(id,data)
    return jsonify(json)


@mesa.route("/mesa/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    json=miControladorMesa.delete(id)
    return jsonify(json)