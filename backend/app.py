from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from . import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=False, port = 8000)

@app.route("/")

def index():
    return render_template('index.html')

