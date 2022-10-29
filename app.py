from flask import Flask

# python -m flask --app hello run is how you call flask
# when the file being called is named app.py you just need to use "python -m flask run" when in the app's folder
app = Flask(__name__)

# / is for the home page ("/" is optional)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# http://127.0.0.1:5000/hi gives the below
@app.route("/hi")
def hi():
    return "<p>Hi!</p>"
