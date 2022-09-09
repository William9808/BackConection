from sesions.db import db
from .ModeloMesa import ModeloMesa
from .ModeloCandidato import ModeloCandidato


class ModeloResultado(db.Model):
    __tablename__ = "Resultado"
    idresultado = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idmesa = db.Column(db.Integer, db.ForeignKey(ModeloMesa.idmesa))
    idcandidato = db.Column(db.Integer, db.ForeignKey(ModeloCandidato.idcandidato))

    def __init__(self, idmesa, idcandidato):
        self.idmesa = idmesa
        self.idcandidato = idcandidato

    def resultado(self):
        return {
            "idresultado": self.idresultado,
            "idmesa": self.idmesa,
            "idcandidato": self.idcandidato
        }

    def __repr__(self):
        return f" idmesa : {self.idmesa}, idcandidato : {self.idcandidato}"
