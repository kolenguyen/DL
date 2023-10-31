from flask import Flask, request, jsonify
from config import Configuration
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from models import User, db
from serializers import UserSerializer, ma

#initialize app and configurate based on config.py
#config.py is based on .flaskenv
app = Flask(__name__)
app.config.from_object(Configuration)

#initializer db and serializer (connect and make tables if needed)
db.init_app(app)
ma.init_app(app)
us = UserSerializer()
migrate = Migrate(app,db)

# ma = Marshmallow(app)
bcrypt = Bcrypt(app)
api = Api(app)
CORS(app)

@app.route('/')
def home():
    # db.drop_all()
    # db.create_all()
    new_user = User(username="john6", email="john6@example.com", password="john")
    db.session.add(new_user)
    db.session.commit()
    us.dump(new_user)
    response_body = {}
    return response_body

@app.route("/user", methods=["GET"])
def getAllUsers():
    us = UserSerializer(many=True)
    allUsers = User.query.all()
    results = us.dump(allUsers)
    # print(us.validate(allUsers))
    print(results)
    return jsonify(results)
