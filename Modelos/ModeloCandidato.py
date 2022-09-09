from sesions.db import db
from .ModeloPartido import ModeloPartido


class ModeloCandidato(db.Model):
    __tablename__ = "Candidato"
    idcandidato = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.String(), unique=True)
    nombre = db.Column(db.String())
    apellido = db.Column(db.String())
    numlista = db.Column(db.Integer)
    idpartido = db.Column(db.Integer, db.ForeignKey(ModeloPartido.idpartido))

    def __init__(self, cedula, nombre, apellido, numlista, idpartido):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.numlista = numlista
        self.idpartido = idpartido

    def resultado(self):
        return {
            "cedula": self.cedula,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "numlista": self.numlista,
            "idpartido": self.idpartido
        }


    def __repr__(self):
        return f" cedula : {self.cedula}, nombre : {self.nombre}," \
               f"apellido : {self.apellido}, numlista : {self.numlista}, idpartido : {self.idpartido}"
