# coding=utf8
from flask import Flask, render_template, jsonify, request ,session, app
from flask_cors import CORS, cross_origin
from flask_mysqldb import MySQL
from datetime import timedelta
import MySQLdb.cursors
import re

app = Flask(__name__)
app.secret_key = 'SoftDev'
app.config['MYSQL_HOST'] = 'computerengineering.3bbddns.com'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'SD'
app.config['MYSQL_PORT'] = 34674
mysql = MySQL(app)
cors = CORS(app, resources={r"/api/*": {"origins": "localhost:8080/*"}})


Testform = [
     {'name': 'BURGER', 'ingredients': ['this', 'that', 'blah']},
     {'name': 'HOTDOG', 'ingredients': ['Chicken', 'Bread']}
 ]


@app.route("/register", methods = ['GET', 'POST'])
@cross_origin()
def register():
    # Output message if something goes wrong...
    form = {'result' : False,'msg' : ''}
    content = request.get_json()
    print("get in stage 1")
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and content['username'] and content['password'] and content['email'] and content['firstname'] and content['lastname']:
        # Create variables for easy access
        
        print("get in stage 2")
        username = content['username']
        password = content['password']
        email = content['email']
        firstname = content['firstname']
        lastname = content['lastname']
        print("username =",username,"password",password,"email",email)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Users WHERE BINARY Username = %s or BINARY email = %s', (username,email))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            form['msg'] = 'Account already exists!'
            print('Account already exists!')
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            form['msg'] = 'Invalid email address!'
            print('Invalid email address!')
        elif not re.match(r'[A-Za-z0-9]+', username):
            form['msg'] = 'Username must contain only characters and numbers!'
            print('Username must contain only characters and numbers!')
        elif not username or not password or not email:
            form['msg'] = 'Please fill out the form!'
            print('Please fill out the form!')
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO Users (username,password,email,role,FirstName,LastName) VALUES (%s, %s, %s, %s, %s, %s)', (username, password, email,"user",firstname,lastname))
            mysql.connection.commit()
            form['result'] = True
            form['msg'] = 'You have successfully registered!'
            print('You have successfully registered!')
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        print("get in stage 3")
        form['msg'] = 'Please fill out the form!'
    # Show registration form with message (if any)
    print(jsonify(form))
    return jsonify(form)

@app.route("/login", methods = ['POST'])
@cross_origin()
def login():
    # Output message if something goes wrong...
    # Check if "username" and "password" POST requests exist (user submitted form)
    form = {'Username' : "", 'FirstName' : "", 'LastName' : "" , 'Nickname' : "" , "Email" : "" , "Tel" : "" ,"Tag" : "","Rating" : "","Checkin" : "","Favorite" : "","Role" : "","Picture" : "","msg" : ""}
    if request.method == 'POST':
        content = request.get_json()
        username = content['username']
        password = content['password']
        # Create variables for easy access
        # Check if account exists using MySQL
        if username and password:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM Atrip_Users WHERE BINARY username = %s AND  BINARY password = %s', (username, password))
            # Fetch one record and return result
            account = cursor.fetchone()
            # If account exists in accounts table in out database
            if account:
                # Create session data, we can access this data in other routes
                form['Username'] = account['Username']
                form['FirstName'] = account['FirstName']
                form['LastName'] = account['LastName']
                form['Nickname'] = account['Nickname']
                form['Email'] = account['Email']
                form['Tel'] = account['Tel']
                form['Tag'] = account['Tag']
                form['Rating'] = account['Rating']
                form['Checkin'] = account['Checkin']
                form['Favorite'] = account['Favorite']
                form['Role'] = account['Role']
                form['Picture'] = account['Picture']
                form['msg'] = 'Logged in successfully!'
                session['Email'] = account['Email']
            else:
                # Account doesnt exist or username/password incorrect
                form['msg'] = 'Incorrect username/password!'
    # Show the login form with message (if any)
        else:
            form['msg'] = 'Please fill out the form!'
        print(form)
        return jsonify(form)

@app.route("/location", methods = ['GET', 'POST'])
@cross_origin()
def location():
    if request.method == 'POST':
        content = request.get_json()
        print(content)
        if content["query"] == "":
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM Atrip_Places ORDER BY keyID')
            account = cursor.fetchall()
            print(account)
    return jsonify(account)

@app.route("/trip", methods = ['GET', 'POST'])
@cross_origin()
def trip():
    if request.method == 'POST':
        content = request.get_json()
        if content["query"] == "":
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM Atrip_Trips ORDER BY keyID')
            account = cursor.fetchall()
            print(account)
    return jsonify(account)

@app.route("/province", methods = ['GET'])
@cross_origin()
def province():
    if request.method == 'GET':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Atrip_Provinces ORDER BY keyID')
        account = cursor.fetchall()
        print(account)
    return jsonify(account)

@app.route("/tripInfo/<keyID>", methods = ['GET'])
@cross_origin()
def tripInfo(keyID):
    if request.method == 'GET':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Atrip_Trips WHERE keyID = %s',[keyID])
        account = cursor.fetchall()
        print(account)
    return jsonify(account)


@app.route("/getPlace", methods = ['GET', 'POST'])
@cross_origin()
def getPlace():
    if request.method == 'POST':
        content = request.get_json()
        print(content["place"])
        print(len(content["place"]))
        if content["place"]:
            contentinput = content["place"].split(",")
            form = "SELECT * FROM Atrip_Places WHERE keyID = " + " or keyID = ".join(contentinput)
            print(form)
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute(form)
            account = cursor.fetchall()
            return jsonify(account)
        else:
            return jsonify(Testform)

@app.route("/getTrip", methods = ['GET', 'POST'])
@cross_origin()
def getTrip():
    if request.method == 'POST':
        content = request.get_json()
        print(content["trip"])
        print(len(content["trip"]))
        if content["trip"]:
            contentinput = content["trip"].split(",")
            form = "SELECT * FROM Atrip_Trips WHERE keyID = " + " or keyID = ".join(contentinput)
            print(form)
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute(form)
            account = cursor.fetchall()
            return jsonify(account)
        else:
            return jsonify(Testform)

@app.route("/addLocation", methods = ['GET', 'POST'])
@cross_origin()
def addLocation():
    form = {"isSuccess" : False , "msg" : ""}
    if request.method == 'POST':
        content = request.get_json()
        print(content)
        if content["placeName"]:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM Atrip_Places WHERE nameTH = %s',[content["placeName"]])
            account = cursor.fetchall()
            if account:
                print("enter")
                form["isSuccess"] = False
                form["msg"] = "Already have data"
            else:
                form["isSuccess"] = True
                form["msg"] = "Successfully add to database"
                cursor.execute('INSERT INTO Atrip_Places (website,phoneNumber,nameTH,provinceTH,descriptionTH) VALUES (%s, %s, %s, %s, %s)', (content["website"], content["phone"], content["placeName"],content["province"],content["description"]))
                mysql.connection.commit()
            return jsonify(form)

        else:
            form["msg"] = "Error no PlaceName :d"
            return jsonify(form)



if __name__ == '__main__':
   app.run(host="0.0.0.0", port=34673, debug=True)
