from sesions.db import db

class ModeloPartido(db.Model):
    __tablename__ = "Partido"
    idpartido = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String())
    lema = db.Column(db.String())

    def __init__(self, nombre, lema):
        self.nombre = nombre
        self.lema = lema

    def resultado(self):
        return {
            "nombre": self.nombre,
            "lema": self.lema
        }

    def __repr__(self):
        return f" nombre : {self.nombre} , lema : {self.lema} "
