from peewee import CharField, BooleanField
# from flask_peewee.auth import BaseUser
from app import db
from flask import current_app

class User(db.Model):
    username = CharField(unique=True)
    password = CharField()
    class Meta:
        table_name = "user"

