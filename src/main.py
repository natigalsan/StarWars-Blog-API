"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

# ----------------------------------------------------------------------------------------------------------------
# vamos a crear nuevas rutas en este archivo:  PRIMER PUNTO DEL EJERCICIO: 
@app.route('/people', methods=['GET'])
def get_people():
    # conlo siguiente consigo todos los personajes: 
    allpeople = People.query.all()
    # print(allpeople[0].serialize())

    allpeople = list(map(lambda elemento: elemento.serialize(), allpeople))
    # esto es un mapeo en python
    print(allpeople)
    return jsonify({"resultado": allpeople})


@app.route('/planets', methods=['GET'])
def get_planets():
    # conlo siguiente consigo todos los personajes: 
    allplanets = Planets.query.all()
    allplanets = list(map(lambda elemento: elemento.serialize(), allplanets))
    # esto es un mapeo en python
    print(allplanets)
    return jsonify({"resultado": allplanets})


@app.route('/user', methods=['GET'])
def get_user():
    # conlo siguiente consigo todos los personajes: 
    alluser = User.query.all()
    alluser = list(map(lambda elemento: elemento.serialize(), alluser))
    # esto es un mapeo en python
    print(alluser)
    return jsonify({"resultado": alluser})


# -----------------------------------------------------------------------------------------------------------------------------------------------
# CÓMO CONSEGUIR DESDE LA URL DE LA WEB  UN PERSONAJE AÑADIDO O PLANETA AÑADIDO COLOCANDO /PEOPLE/1  Y /PLANETS/2  X EJEMPLO Y ME SALE LA SERIALIZE() CON LOS DATOS
@app.route('/people/<int:id>', methods=['GET'])
# esta parte es para buscar un personaje agregado de mi lista desde la url añadiendo /people/1 --> y me sale luke skwalkler
def get_one_people(id):
    # bajo un parametro especifico
    # query = consultar"
    onepeople = People.query.filter_by(id=id).first()
    # .firts()... me devuelve el primer elemento 
    # .all() me devuelve un array 
    # onepeople = People.query.filter_by(gender = n/a).first()
    onepeople = People.query.get(id).serialize()

    return jsonify({"resultado": onepeople})
   
    # buscar solo por el id


@app.route('/planets/<int:id>', methods=['GET'])
# esta parte es para buscar un personaje agregado de mi lista desde la url añadiendo /people/1 --> y me sale luke skwalkler
def get_one_planets(id):
    # bajo un parametro especifico
    # query = consultar"
# 1 MANERA DE HACERLA
    # oneplanets = Planets.query.filter_by(id=id).first()

    # .firts()... me devuelve el primer elemento 
    # .all() me devuelve un array 
# 2 MANERA DE HACERLO MÁS SENCILLO
    # onepeople = People.query.filter_by(gender = n/a).first()
    oneplanets = Planets.query.get(id).serialize()

    return jsonify({"resultado": oneplanets})



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
