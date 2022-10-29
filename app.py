from flask import Flask, render_template
import datetime
# python -m flask --app hello run is how you call flask
# when the file being called is named app.py you just need to use "python -m flask run" when in the app's folder
app = Flask(__name__)

# / is for the home page ("/" is optional)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# http://127.0.0.1:5000/index gives the below
@app.route("/index")
def index():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@app.route("/ext_index")
def ext_index():
    return render_template('ext_index.html', utc_dt=datetime.datetime.utcnow())
