# Sample Flask application for a BSG database, snapshot of BSG_people

from flask import Flask, render_template, json, redirect
# from flask_mysqldb import MySQL
from flask import request
import os


app = Flask(__name__)

# database connection info
app.config["MYSQL_HOST"] = "classmysql.engr.oregonstate.edu"
app.config["MYSQL_USER"] = "cs340_higginde"
app.config["MYSQL_PASSWORD"] = "6560"
app.config["MYSQL_DB"] = "cs340_higginde"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

# Specify the location of the templates folder
app.template_folder = os.path.abspath('templates')

# Routes
# have homepage route to /people by default for convenience, generally this will be your home route with its own template
@app.route('/')
def index():
    return render_template('/people.html')

@app.route('/planets.html')
def planets():
    return render_template('/planets.html')

@app.route('/people.html')
def people():
    return render_template('/people.html')
# Listener
# change the port number if deploying on the flip servers
if __name__ == "__main__":
    app.run(port=7337, debug=True)