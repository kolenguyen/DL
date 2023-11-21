from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
import os

practice_blueprint = Blueprint('practice', __name__)

@practice_blueprint.route('/upload', methods=['POST'])
@jwt_required()
def upload_video():
    username = get_jwt_identity()
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400

    if file:  
        filename = secure_filename(file.filename)
        save_path = os.path.join(current_app.config['UPLOAD_FOLDER'], username)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        file.save(os.path.join(save_path, filename))
        return jsonify({"message": "File uploaded successfully"})

    return jsonify({"message": "Something went wrong"}), 500




