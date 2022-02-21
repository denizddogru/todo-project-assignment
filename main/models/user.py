from peewee import CharField, BooleanField
from app import db


class User(db.Model):
    username = CharField()
    password = CharField()
    email = CharField()

    #our custom fields
    is_superuser = BooleanField()
    class Meta:
        table_name = "user"
