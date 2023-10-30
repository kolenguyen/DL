from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
db.init_app(app)
bcrypt = Bcrypt(app)
api = Api(app)
CORS(app)

@app.route('/')

#exameple of how data is returned with a simple API
def home():
    response_body = {}
    return response_body