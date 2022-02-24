from form import *
from flask import Blueprint, request, jsonify
from app import db
from form import *
from flask_peewee.db import Database
api = Blueprint("route_api", __name__)
from models.user import User




@api.route('/register_user', methods=['GET', 'POST'])
def register():

    user_request_data = request.get_json()
    
    with db.database.atomic():
        user = User.create(username=user_request_data["username"], password=user_request_data["password"],
                           )

    return jsonify({"message": "Registration successfull."})



@api.route('/validate_user', methods=['GET', 'POST'])
def validate_user():

    user_request_data = request.get_json()

    with db.database.atomic():
        user = User.select().where(User.username == user_request_data["username"]).first()

    if not user:
        return jsonify({"status" : "fail", "message" : "user not found"})
    return jsonify({"status": "success" , "message" : "login successfull"})
    