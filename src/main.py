"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db
from models import Family
import uuid
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route("/new_member", methods=["POST"])
def create_new_member():
    data = request.get_json()
    new_member = Family(public_id=str(uuid.uuid4()), first_name=data["first_name"], last_name=data["last_name"],age=data["age"],lucky_numbers=data["lucky_numbers"])
    db.session.add(new_member)
    db.session.commit()
    return jsonify({"message":"New User Created!"})

@app.route("/Family_members", methods=["GET"])
def get_all_family():

    family = Family.query.all()
    output = []

    for member in family:
        member_data = {}
        member_data["public_id"] = member.public_id

        member_data["last_name"] = member.last_name
        member_data["first_name"] = member.first_name
        member_data["age"] = member.age
        member_data["lucky_numbers"] = member.lucky_numbers
        output.append(member_data)

    return jsonify({"Family" : output})

@app.route("/Family_members/<public_id>", methods=["GET"])
def get_one_member(public_id):
    member = Family.query.filter_by(public_id=public_id).first()

    if not member:
        return jsonify({"message" : "No such family member was born!"}), 404

    member_data = {}
    output = []
    member_data["public_id"]=member.public_id
    member_data["last_name"]=member.last_name
    member_data["first_name"]=member.first_name
    member_data["age"]=member.age
    member_data["lucky_numbers"]=member.lucky_numbers
    output.append(member_data)

    return jsonify({"Family_member":member_data})

@app.route("/Family_members/<public_id>", methods=["DELETE"])
def delete_member(public_id):
    member = Family.query.filter_by(public_id=public_id).first()

    if not member:
        return jsonify({"message" : "No such family member was born!"}), 404

    db.session.delete(member)
    db.session.commit()

    return jsonify({"message" : "That one shell never return, exiled forever!"})
    

@app.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "hello": "world"
    }

    return jsonify(response_body), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
