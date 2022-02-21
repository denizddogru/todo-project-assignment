from form import *
from flask import Flask,jsonify
# flask-peewee bindings
from flask_peewee.db import Database


# configure our database

DATABASE = {
    'name': 'database.db',
    'engine': 'peewee.SqliteDatabase',
}
DEBUG = True
SECRET_KEY = 'ssshhhh'

app = Flask(__name__)
app.config.from_object(__name__)

db = Database(app)


#routing


from models.user import User


@app.route('/register_user', methods=['POST'])
def register():
    with db.database.atomic():
        user = User.create(username="yasin2",password = "pass123",email="email@test.com",is_superuser=True)
        
    return jsonify({"username" : "xyz"})




if __name__ == '__main__':
    app.run()
