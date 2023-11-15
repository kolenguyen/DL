from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token,jwt_required, get_jwt
from ..models.user import User
from ..models import db
from ..serializers import UserSerializer
from marshmallow import ValidationError

revoked_tokens = set()

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Check if user already exists
    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({'message': 'User already exists'}), 409

    hashed_password = generate_password_hash(password)

    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

@auth_blueprint.route('/login', methods=['POST'])
def login():
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

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        access_token = create_access_token(identity=username)
        return jsonify({'access_token': access_token}), 200

    return jsonify({'message': 'Invalid username or password'}), 401




@auth_blueprint.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()['jti']  # Get the unique identifier of the JWT
    revoked_tokens.add(jti)  # Add it to the set of revoked tokens
    return jsonify({'message': 'User logged out successfully'}), 200