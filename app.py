from flask import Flask, request, jsonify
from config import Configuration
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from models import User, db
from serializers import UserSerializer, ma
from marshmallow import ValidationError
from sqlalchemy.orm.exc import NoResultFound
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token

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
jwt=JWTManager(app)
bcrypt = Bcrypt(app)
api = Api(app)
CORS(app)

@app.route('/')

@app.route("/user", methods=["GET"])
def getAllUsers():
    us = UserSerializer(many=True)
    allUsers = User.query.all()
    results = us.dump(allUsers)
    # print(us.validate(allUsers))
    print(results)
    return jsonify(results)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    try:
        data['password'] = generate_password_hash(data['password'])
        newUser = User(username=data['username'], email=data['email'], password=data['password'])
    except ValidationError as err:
        return jsonify({
            'message':'Invalid input data',
            'errors': err.messages
        }), 400
    
    db.session.add(newUser)
    db.session.commit()
    return jsonify({'message':'User added successfuly'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    loginSerializer = UserSerializer(only=("username", "password"))

    #validate data 
    try:
        loginData = loginSerializer.load(data)
    except ValidationError as err:
        return jsonify({
            'message': 'invalid input data',
            'errors': err.messages
        }), 400

    #check username and password
    username = loginData.get('username')
    password = loginData.get('password')

    try:
        user= db.session.query(User).filter(User.username == username).one()
    except NoResultFound:
        return jsonify({'message':'User not found'}), 404
    
    if check_password_hash(user.password,password):
        access_token = create_access_token(identity=user.id)
        return jsonify({'message':'Login succesful', 'access_token': access_token}), 200
    else: 
        return jsonify({'message':'Invalid password'}), 401
   

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    return jsonify({'message':'Testing authentication', 'user_id': current_user_id})