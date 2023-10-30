import os
from dotenv import load_dotenv

#used to find and load .env or .flaskenv from the root
load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))

class Configuration(object):
    #secret key can be written here for development but for production, it should separated into a .env file
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    