from flask import Flask
from flask import jsonify
from flask_cors import CORS
import json
from waitress import serve
from sesions.db import db
from flask_sqlalchemy import SQLAlchemy
from Routes.Partido import partido
from Routes.Mesa import mesa
from Routes.Candidato import candidato
from Routes.Resultado import resultado

app = Flask(__name__)
cors = CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:cRX8POI1@localhost:5432/registraduria2"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

SQLAlchemy(app)

app.register_blueprint(partido)
app.register_blueprint(mesa)
app.register_blueprint(candidato)
app.register_blueprint(resultado)


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
        return data


with app.app_context():
    db.create_all()


def test():  # put application's code here
    json = {}
    json["message"]="Server running..."
    return jsonify(json)


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url_backend"]+":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url_backend"], port=dataConfig["port"])