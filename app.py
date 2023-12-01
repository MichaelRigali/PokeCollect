from flask import Flask, render_template, json, redirect, request
from flask_mysqldb import MySQL
import os

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

# database connection info
app.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
app.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
app.config["MYSQL_CURSORCLASS"] = os.environ.get("MYSQL_CURSORCLASS")

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

@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        # Retrieve form data
        username = request.form['username']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        birthday = request.form['birthday']
        address = request.form['address']

        # Execute the SQL query for inserting a new user
        query = "INSERT INTO Users (username, password, first_name, last_name, email, birthday, address) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        user_data = (username, password, first_name, last_name, email, birthday, address)
        cur = mysql.connection.cursor()
        cur.execute(query, user_data)
        mysql.connection.commit()

        # Redirect to the main page after adding the user
        return redirect('/users')

@app.route("/edit_user/<int:user_id>", methods=["POST", "GET"])
def edit_user(user_id):
    if request.method == "GET":
        # mySQL query to grab the info of the person with our passed id
        query = "SELECT * FROM Users WHERE user_id = %s" % (user_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render edit_people page passing our query data and homeworld data to the edit_people template
        return render_template("edit_user.j2", data=data)

    # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit Person' button

            # grab user form inputs
        user_id = request.form["user_id"]
        username = request.form["username"]
        password = request.form["password"]
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        birthday = request.form['birthday']
        email = request.form['email']
        address = request.form['address']

        # call update query
        query = "UPDATE Users SET Users.username = %s, Users.password = %s, Users.first_name = %s, Users.last_name = %s, Users.birthday = %s, Users.email = %s, Users.address = %s WHERE user_id = %s"
        cur = mysql.connection.cursor()
        cur.execute(query, (username, password, first_name, last_name, birthday, email, address, user_id))
        mysql.connection.commit()

        return redirect("/users")

@app.route('/delete_user/<int:id>', methods=['GET'])
def delete_user(id):
    # mySQL query to delete the user with the passed id
    query = "DELETE FROM Users WHERE user_id = %s;"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()
    # Redirect back to the users page
    return redirect("/users")

@app.route('/orders', methods=["POST", "GET"])
def orders():

    # Grab orders data so we send it to our template to display
    if request.method == "GET":
        # mySQL query to grab all orders data
        query = "SELECT * FROM Orders"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render template
        return render_template("orders.j2", data=data)
    return render_template('orders.j2')

@app.route('/shipments', methods=["POST", "GET"])
def shipments():

    # Grab shipments data so we send it to our template to display
    if request.method == "GET":
        # mySQL query to grab all shipments data
        query = "SELECT * FROM Shipments"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render template
        return render_template("shipments.j2", data=data)
    return render_template('shipments.j2')

@app.route('/add_shipment', methods=['POST'])
def add_shipment():
    if request.method == 'POST':
        # Retrieve form data
        shipping_id = request.form['shipping_id']
        user_id = request.form['user_id']
        delivery_time = request.form['delivery_time']
        carrier = request.form['carrier']
        tracking_number = request.form['tracking_number']

        # Execute the SQL query for inserting a new user
        query = "INSERT INTO Shipments (shipping_id, user_id, delivery_time, carrier, tracking_number) VALUES (%s, %s, %s, %s, %s);"
        shipping_data = (shipping_id, user_id, delivery_time, carrier, tracking_number)
        cur = mysql.connection.cursor()
        cur.execute(query, shipping_data)
        mysql.connection.commit()

        # Redirect to the main page after adding the user
        return redirect('/shipments')

@app.route("/edit_shipment/<int:shipping_id>", methods=["POST", "GET"])
def edit_shipment(shipping_id):
    if request.method == "GET":
        # mySQL query to grab the info of the person with our passed id
        query = "SELECT * FROM Shipments WHERE shipping_id = %s" % (shipping_id)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render edit_shipment page passing our query data to the edit_shipment template
        return render_template("edit_shipment.j2", data=data)

    # meat and potatoes of our update functionality
    if request.method == "POST":
        # fire off if user clicks the 'Edit Person' button

        # grab shipment form inputs
        shipping_id = request.form['shipping_id']
        user_id = request.form['user_id']
        delivery_time = request.form['delivery_time']
        carrier = request.form['carrier']
        tracking_number = request.form['tracking_number']

        # call update query
        query = "UPDATE Shipments SET Shipments.shipping_id = %s, Shipments.user_id = %s, Shipments.delivery_time = %s, Shipments.carrier = %s, Shipments.tracking_number = %s WHERE shipping_id = %s"
        cur = mysql.connection.cursor()
        cur.execute(query, (shipping_id, user_id, delivery_time, carrier, tracking_number, shipping_id))
        mysql.connection.commit()

        return redirect("/shipments")

@app.route('/delete_shipment/<int:id>', methods=['GET'])
def delete_shipment(id):
    # mySQL query to delete the shipment with the passed id
    query = "DELETE FROM Shipments WHERE shipping_id = %s;"
    cur = mysql.connection.cursor()
    cur.execute(query, (id,))
    mysql.connection.commit()
    # Redirect back to the users page
    return redirect("/shipments")

@app.route('/payments', methods=["POST", "GET"])
def payments():

    # Grab payments data so we send it to our template to display
    if request.method == "GET":
        # mySQL query to grab all payments data
        query = "SELECT * FROM Payments"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render template
        return render_template("payments.j2", data=data)
    return render_template('payments.j2')

@app.route('/pokemoncardspecs', methods=["POST", "GET"])
def pokemoncardspecs():

    # Grab pokemoncardspecs data so we send it to our template to display
    if request.method == "GET":
        # mySQL query to grab all pokemoncardspecs data
        query = "SELECT * FROM PokemonCardSpecs"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        # render template
        return render_template("pokemoncardspecs.j2", data=data)
    return render_template('pokemoncardspecs.j2')

# Listener
# change the port number if deploying on the flip servers
if __name__ == "__main__":
    app.run(port=41027 , debug=True)