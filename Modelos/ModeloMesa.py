from sesions.db import db

class ModeloMesa(db.Model):
    __tablename__ = "Mesa"
    idmesa = db.Column(db.Integer, primary_key=True, autoincrement=False)
    cant_inscritos = db.Column(db.Integer)

    def __init__(self, idmesa, cant_inscritos):
        self.idmesa = idmesa
        self.cant_inscritos = cant_inscritos

    def resultado(self):
        return {
            "idmesa": self.idmesa,
            "cant_inscritos": self.cant_inscritos
        }

    def __repr__(self):
        return f" idmesa : {self.idmesa} , cant_inscritos : {self.cant_inscritos} "