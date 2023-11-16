from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os


app = Flask(__name__)

# database connection info
app.config["MYSQL_HOST"] = "classmysql.engr.oregonstate.edu"
app.config["MYSQL_USER"] = "cs340_higginde"
app.config["MYSQL_PASSWORD"] = "6560"
app.config["MYSQL_DB"] = "cs340_higginde"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

# Specify the location of the templates folder
app.template_folder = os.path.abspath('templates')

# Routes
# have homepage route to /people by default for convenience, generally this will be your home route with its own template
@app.route('/')
def index():

    if request.method == "GET":
        # mySQL query to grab all user data
        query = "SELECT * FROM Users"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render edit_people page passing our query data and homeworld data to the edit_people template
        return render_template("users.j2", data=data)
    return render_template('users.j2')

@app.route('/users', methods=["POST", "GET"])
def users():

    # Grab Users data so we send it to our template to display
    if request.method == "GET":
        # mySQL query to grab all user data
        query = "SELECT * FROM Users"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render edit_people page passing our query data and homeworld data to the edit_people template
        return render_template("users.j2", data=data)
    return render_template('users.j2')

@app.route('/orders.html')
def orders():
    return render_template('/orders.html')

@app.route('/shipments.html')
def shipments():
    return render_template('/shipments.html')

@app.route('/payments.html')
def payments():
    return render_template('/payments.html')

@app.route('/pokemoncardspecs.html')
def pokemoncardspecs():
    return render_template('/pokemoncardspecs.html')


####### delete routes #######
# delete from Users
@app.route("/delete_user/<int:id>")
def delete_people(id):
    # mySQL query to delete the person with our passed id
    query = "DELETE FROM Users WHERE id = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()

    # redirect back to people page
    return redirect("/people")

# Listener
# change the port number if deploying on the flip servers
if __name__ == "__main__":
    app.run(port=41025, debug=True)