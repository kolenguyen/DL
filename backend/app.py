from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from . import create_app
from flask_cors import CORS

app = create_app()
CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:3000"}})

if __name__ == "__main__":
    app.run(debug=False, port = 8000)

@app.route("/")

def index():
    return render_template('index.html')

