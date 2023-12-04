from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configurations
    app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change this!
    # app.config['UPLOAD_FOLDER'] = '/path/to/upload_folder'  # Specify the upload folder path
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    # Initialize components
    jwt = JWTManager(app)
    db.init_app(app)

    from .routes.user import user_blueprint
    from .routes.auth import auth_blueprint
    from .routes.practice import practice_blueprint
    from .routes.training import training_blueprint
   
    app.register_blueprint(user_blueprint, url_prefix='/user')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(practice_blueprint, url_prefix='/practice')
    app.register_blueprint(training_blueprint, url_prefix='/training')

    return app
