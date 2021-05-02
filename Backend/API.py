# coding=utf8
from flask import Flask, render_template, jsonify, request ,session, app
from flask_cors import CORS, cross_origin
from flask_mysqldb import MySQL
from datetime import timedelta
import MySQLdb.cursors
import re

import googlemaps
from findRoute import allResults,sortResult


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
        cursor.execute('SELECT * FROM Atrip_Users WHERE BINARY Username = %s or email = %s', (username,email))
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
            cursor.execute('INSERT INTO Atrip_Users (username,password,email,role,FirstName,LastName) VALUES (%s, %s, %s, %s, %s, %s)', (username, password, email,"user",firstname,lastname))
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
    form = {'id' : "",'Username' : "", 'FirstName' : "", 'LastName' : "" , 'Nickname' : "" , "Email" : "" , "Tel" : "" ,"Tag" : "","Rating" : "","Checkin" : "","Favorite" : "","Role" : "","Picture" : "","msg" : ""}
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
                form['id'] = account['ID']
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
        if content["query"] == "":
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM Atrip_Places ORDER BY keyID')
            account = cursor.fetchall()
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

@app.route("/placeInfo/<keyID>", methods = ['GET'])
@cross_origin()
def placeInfo(keyID):
    if request.method == 'GET':
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Atrip_Places WHERE keyID = %s',[keyID])
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
            print(contentinput)
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
                cursor.execute('INSERT INTO Atrip_Places (website,phoneNumber,nameTH,provinceTH,descriptionTH) VALUES (%s, %s, %s, %s, %s)', (content["website"], content["phone"], content["placeName"],content["province"],content["description"]))
                mysql.connection.commit()
                form["isSuccess"] = True
                form["msg"] = "Successfully add to database"
                cursor.execute('INSERT INTO Atrip_Places (website,phoneNumber,nameTH,provinceTH,descriptionTH) VALUES (%s, %s, %s, %s, %s)', (content["website"], content["phone"], content["placeName"],content["province"],content["description"]))
                mysql.connection.commit()
            return jsonify(form)

        else:
            form["msg"] = "Error no PlaceName :d"
            return jsonify(form)

@app.route("/makeTrip", methods = ['GET', 'POST'])
@cross_origin()
def makeTrip():
    form = {"isSuccess" : False , "msg" : ""}
    if request.method == 'POST':
        content = request.get_json()
        if content['userID'] and content["tripName"] and content["placesInTrip"]:
            key = ""
            for i in range(0,len(content["placesInTrip"]),1):
                key = key + str(content["placesInTrip"][i]["keyID"]) + ","
            key = key[0:len(key)-1]
            qkey = key.split(",")
            sqlform = "SELECT provinceTH FROM Atrip_Places WHERE keyID = " + " or keyID = ".join(qkey)
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute(sqlform)
            account = cursor.fetchall()
            sqlprovince = ""
            for i in range(len(account)):
                sqlprovince = sqlprovince + account[i]["provinceTH"] + ","
            sqlprovince = sqlprovince[0:len(sqlprovince)-1]
            cursor.execute('INSERT INTO Atrip_Trips (nameTH,placeList,owner,provinceTH_List) VALUES (%s, %s, %s, %s)', (content['tripName'],key,content["userID"],sqlprovince))
            mysql.connection.commit()
            form["isSuccess"] = True
            form["msg"] = "Successfully add to database"
            return jsonify(form)
        else:
            form["msg"] = "Error"
            return jsonify(form)

@app.route("/myTrip", methods = ['GET', 'POST'])
@cross_origin()
def myTrip():
    if request.method == 'POST':
        content = request.get_json()
        print(content)
        if content["query"] == "":
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM Atrip_Trips where owner = %s ORDER BY keyID',[content["id"]])
            account = cursor.fetchall()
            print(account)
    return jsonify(account)

@app.route("/makeRoute", methods = ['GET', 'POST'])
@cross_origin()
def makeRoute():
    if request.method == 'POST':
        #print("HelloWorld")
        content = request.get_json()
        #print(len(content["placesInTrip"]))
        #print(content["placesInTrip"][0]["keyID"],end = " ")
        #print(content["placesInTrip"][0]["coordinate"])

        numPlace = len(content["placesInTrip"])
        placeIDList = list()
        coordinateList = list()
        for i in range(numPlace):
            placeIDList.append(content["placesInTrip"][i]["keyID"])
            coordinateList.append(content["placesInTrip"][i]["coordinate"])
        #ListOfAllOutcomeBetweenKeyOfPointToKeyOfPoint = makeList_Of_ListOfAllOutcomeBetweenKeyOfPointToKeyOfPoint_From_ListOfKeyOfSelectedPlace(placeIDList)
        #dictFromGooglemapsAPI = gmaps.distance_matrix(coordinateList,coordinateList,mode='driving')
        #DistanceBetweenPointToPoint = makeList_Of_DistanceBetweenPointToPoint_From_DictFromGooglemapsAPI(dictFromGooglemapsAPI)
        #print(allResults(placeIDList,gmaps.distance_matrix(coordinateList,coordinateList,mode='driving')))
        #print(ListOfAllOutcomeBetweenKeyOfPointToKeyOfPoint)
        #print(makeList_of_ListOfAllOutcomeBetweenKeyOfPointToKeyOfPoint_And_DistanceBetweenPointToPoint(ListOfAllOutcomeBetweenKeyOfPointToKeyOfPoint,gmaps.distance_matrix(coordinateList,coordinateList,mode='driving')))
        #print(DistanceBetweenPointToPoint)
        #ListOfAllOutcomeBetweenKeyOfPointToKeyOfPoint = makeList_of_ListOfAllOutcomeBetweenKeyOfPointToKeyOfPoint_And_DistanceBetweenPointToPoint(ListOfAllOutcomeBetweenKeyOfPointToKeyOfPoint,DistanceBetweenPointToPoint)
        #print(ListOfAllOutcomeBetweenKeyOfPointToKeyOfPoint)
        #x = makeList_Of_ListOf_AllListOfRoute_ListofDistance_And_SumOfDistance(numPlace,ListOfAllOutcomeBetweenKeyOfPointToKeyOfPoint,list() ,list(), list())
        #print(x)
        results = dict()
        results["results"] = sortResult(allResults(placeIDList,gmaps.distance_matrix(coordinateList,coordinateList,mode='driving')))
        for i in results["results"]:
            print(i)

    return jsonify(results)

if __name__ == '__main__':
    gmaps = googlemaps.Client(key='AIzaSyCIHRdrSY885ctMMj_cvL-Ga69IktvnLs0')
    app.run(host="0.0.0.0", port=34673, debug=True)

