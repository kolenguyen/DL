from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models.user import User
from .. import db

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/profile', methods=['GET'])
# @jwt_required()
def get_user_details():
    username = get_jwt_identity()
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify(user.to_dict())
    else:
        return jsonify({"message": "User not found"}), 404

@user_blueprint.route('/update/name', methods=['PUT'])
# @jwt_required()
def update_user_name():
    username = get_jwt_identity()
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "User not found"}), 404

    new_username = request.json.get('username')
    if not new_username:
        return jsonify({"message": "New username is required"}), 400

    user.username = new_username
    db.session.commit()
    return jsonify({"message": "Username updated successfully"})

@user_blueprint.route('/update/password', methods=['PUT'])
# @jwt_required()
def update_password():
    username = get_jwt_identity()
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "User not found"}), 404

    current_password = request.json.get('current_password')
    new_password = request.json.get('new_password')
    if not all([current_password, new_password]):
        return jsonify({"message": "Current and new password are required"}), 400

    if not check_password_hash(user.password, current_password):
        return jsonify({"message": "Invalid current password"}), 401

    user.password = generate_password_hash(new_password)
    db.session.commit()
    return jsonify({"message": "Password updated successfully"})

@user_blueprint.route('/update/email', methods=['PUT'])
# @jwt_required()
def update_email():
    username = get_jwt_identity()
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "User not found"}), 404

    new_email = request.json.get('email')
    if not new_email:
        return jsonify({"message": "New email is required"}), 400

    if User.query.filter_by(email=new_email).first():
        return jsonify({"message": "Email already in use"}), 409

    user.email = new_email
    db.session.commit()
    return jsonify({"message": "Email updated successfully"})

