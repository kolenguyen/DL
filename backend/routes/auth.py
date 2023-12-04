from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token,jwt_required, get_jwt
from ..models.user import User
from .. import db
from ..serializers import UserSerializer
from marshmallow import ValidationError
#base code for this is used from Kole's branch
from flask_cors import CORS, cross_origin

revoked_tokens = set()
auth_blueprint = Blueprint('auth', __name__)
CORS(auth_blueprint, resources={r"/*": {"origins": "http://127.0.0.1:3000"}})

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({'message': 'User already exists'}), 409

    hashed_password = generate_password_hash(password)

    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201


@cross_origin(origin='http://127.0.0.1:3000', headers=['Content-Type', 'Authorization'])
@auth_blueprint.route('/login', methods=['POST','OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        # Handle preflight request
        response = jsonify({"test": "test"})
        response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        return response,200
    data = request.get_json()

    loginSerializer = UserSerializer(only=("username", "password"))

    try:
        loginData = loginSerializer.load(data)
    except ValidationError as err:
        return jsonify({
            'message': 'invalid input data',
            'errors': err.messages
        }), 400
    
    username = loginData.get('username')
    password = data.get('password')
    print(username)
    print(password)

    user = User.query.filter_by(username=username).first()
    print(user.username)
    print(user.password)
    print(check_password_hash(user.password, password))
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=username)
        return jsonify({'access_token': access_token}), 200
    response = jsonify(data)
    return response, 401

@auth_blueprint.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()['jti']  # Get the unique identifier of the JWT
    revoked_tokens.add(jti)  # Add it to the set of revoked tokens
    return jsonify({'message': 'User logged out successfully'}), 200