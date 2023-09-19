from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
#printing out a statement
# def home():
#     return "Hello, Flask!"

# Look for a file called index.html from templates folder
def index():
    return render_template('index.html')