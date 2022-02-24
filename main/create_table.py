from peewee import *
from flask import Flask, jsonify


from app import db
from models.user import User



if __name__ == '__main__':
    db.database.connect()
    db.database.create_tables(
        [User]
        
    )