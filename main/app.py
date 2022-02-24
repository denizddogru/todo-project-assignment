from form import *
from flask import Flask, jsonify, Blueprint
from flask_peewee.db import Database
# from webargs.flaskparser import use_args
from marshmallow import fields
from flask import request



# configure our database

DATABASE = {
    'name': 'database.db',
    'engine': 'peewee.SqliteDatabase',
}
DEBUG = True
SECRET_KEY = 'ssshhhh'

# configure application
app = Flask(__name__)
app.config.from_object(__name__)


# app'içinde db var
db = Database(app)
from api.routes import api as route_api
app.register_blueprint(route_api, url_prefix="/api")
  



if __name__ == '__main__':
    app.run()
