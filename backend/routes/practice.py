from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
import os, subprocess
from tensorflow.keras.models import load_model
import numpy as np 
import sys, os, cv2
from PIL import Image
from keras.models import model_from_json

practice_blueprint = Blueprint('practice', __name__)


@practice_blueprint.route('/upload', methods=['POST'])
# @jwt_required()
def upload_video():
    # username = get_jwt_identity()
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400

    file = request.files['file']
    if file.filename == '': 
        return jsonify({"message": "No selected file"}), 400

    # print(os.getcwd())
    json_path = os.path.join(os.getcwd(), "backend/model-01/model-training/model.json")
    model_path = os.path.join(os.getcwd(), "backend/model-01/model-training/model.h5")

    # print(os.path.exists("../../model-01/model-training/model.json"))
    json_file = open(json_path, 'r')
  
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    model.load_weights(model_path)
    model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

    #use image data passed back from request
    ################# To-do
    img_path = file
    img = Image.open(img_path)
    # print(type(img))
    numpy_array = np.asarray(img)
    gimage = cv2.cvtColor(numpy_array, cv2.COLOR_RGB2GRAY)
    # cv2.imshow("BGR Image", gimage)
    image28 = cv2.resize(gimage, (28, 28))
    imagere = image28.reshape(1, 28, 28, 1)  # Reshape to the expected input shape

    # Predict the ASL letter
    output = {i: chr(i + 65) for i in range(25)}
    prediction = model.predict(imagere)
    predicted_class = np.argmax(prediction, axis=-1)  # Find the class with the highest probability
    predicted_letter = output[predicted_class[0]]
    # print(type(predicted_letter))
    #########Return this - to do
    # print(predicted_class)
    # print(predicted_letter)

    if file:  # Here, you can add file type checking logic
        # filename = secure_filename(file.filename)
        # save_path = os.path.join(current_app.config['UPLOAD_FOLDER'], username)
        # if not os.path.exists(save_path):
        #     os.makedirs(save_path)
        # file.save(os.path.join(save_path, filename))
        return jsonify({"message": (predicted_letter)})

    return jsonify({"message": "Something went wrong"}), 500


@practice_blueprint.route('/feedback', methods=['POST'])
# @jwt_required()  
def post_feedback():
    # username = get_jwt_identity()  
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
