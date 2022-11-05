from flask import Flask, render_template
import datetime
from api.main import api
from table_from_api.main import table_from_api
# python -m flask --app hello run is how you call flask
# when the file being called is named app.py you just need to use "python -m flask run" when in the app's folder
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# / is for the home page ("/" is optional)
@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

# http://127.0.0.1:5000/home gives the below
@app.route("/simple")
def simple():
    return render_template('simple.html', utc_dt=datetime.datetime.utcnow())

@app.route("/")
def index():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@app.route("/api")
def api_call():
    return api()

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/table")
def api_table():
    return render_template('api_table.html', api_data=table_from_api())
