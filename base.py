from flask import Flask

api = Flask(__name__)

@api.route('/')

#exameple of how data is returned with a simple API
def home():
    response_body = {}
    return response_body