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

    if file:  # Here, you can add file type checking logic
        filename = secure_filename(file.filename)
        save_path = os.path.join(current_app.config['UPLOAD_FOLDER'], username)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        file.save(os.path.join(save_path, filename))
        return jsonify({"message": "File uploaded successfully"})

    return jsonify({"message": "Something went wrong"}), 500


@practice_blueprint.route('/feedback', methods=['POST'])
@jwt_required()  
def post_feedback():
    username = get_jwt_identity()  
    user = User.query.filter_by(username=username).first()

    if not user:
        return jsonify({"message": "User not found"}), 404

    feedback_data = request.json.get('feedback')
    if not feedback_data:
        return jsonify({"message": "Feedback content is required"}), 400


    history = History.query.filter_by(user_id=user.id).order_by(History.id.desc()).first()
    if history:
        history.field = feedback_data  # Update the field with feedback to save in history table
    else:
        new_history = History(user_id=user.id, progress="Feedback", field=feedback_data)
        db.session.add(new_history)

    db.session.commit()
    return jsonify({"message": "Feedback submitted successfully"})
