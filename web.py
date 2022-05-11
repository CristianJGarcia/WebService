#!/usr/bin/env python3
import flask
import flask_api
from flask_api import status
import pymysql.cursors
from flask import Flask, request, redirect, jsonify
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from threading import Thread
import time

# Init app
app = Flask('app2')
app2 = Flask('app')
# CORS sets up with defaults inlcuding Access-Control-Allow-Origin: *
CORS(app)
CORS(app2)

# add mysql creds
MYSQL_USER = 'myuser'
MYSQL_PASSWORD = 'root'                      # '4zMka4K96LzGhpHk0A4t'
# 'hqc265-db1'                    # 'easel2.fulgentcorp.com'
MYSQL_HOST = '10.0.147.80'
MYSQL_DB = 'hqc265'

# Secret-Key
SECRET_KEY = "cs4783FTW"

# When data is received make it a Dictionary
#app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Configure swagger to work with flask

print("*******SLEEPING********")
time.sleep(20)
print("*******DONE SLEEP********")

mysql = pymysql.connect(host=MYSQL_HOST,
                        user=MYSQL_USER,
                        password=MYSQL_PASSWORD,
                        db=MYSQL_DB,
                        port=3306,
                        auth_plugin_map='root',
                        cursorclass=pymysql.cursors.DictCursor)

mysql.ping(reconnect=True)


# TODO check if the table already exists
cur = mysql.cursor()

try:
    with mysql.cursor() as cursor:
        # See if everything is there
        sql = '''SELECT * FROM hqc265.Properties ORDER BY id ASC'''
        cursor.execute(sql)
        #results = cur.fetchall()
except:
    # if results == "":
    # SQL query string
    sqlQuery = "CREATE TABLE Properties(id int(1) NOT NULL, address text NOT NULL, city text NOT NULL, state char(2) NOT NULL, zip text NOT NULL)"
    #"CREATE TABLE Employee(id int, LastName varchar(32), FirstName varchar(32), DepartmentCode int)"

    # Execute the sqlQuery
    cur.execute(sqlQuery)

    data = '''INSERT INTO Properties (id,address, city, state, zip) VALUES (6, '15801 chase hill blvd', 'San antonio', 'TX', '78256'), (7, '456 Example St.', 'Fort Sill', 'OK', '83230')'''
    cur.execute(data)
    data2 = '''ALTER TABLE Properties ADD PRIMARY KEY (id)'''
    cur.execute(data2)
    data3 = '''ALTER TABLE Properties MODIFY id int (1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=119'''
    cur.execute(data3)
    mysql.commit()
    cur.close()
    # Grab the Authorization header will be of type None if nothing exists


def getAPIKEY():
    API_KEY = str(request.headers.get('Authorization')).split(" ")
    return API_KEY

# Auth may have type in header
# Authorization: Basic xxxxx
# Authorization: Bearer xxxxx
# Authorizatoin: xxxxx


def validAPIKEY(API_KEY):
    for token in API_KEY:
        if token == SECRET_KEY:
            return True
    return False


@app.route('/accept', methods=['GET'])
def certA():
    return jsonify({'message': 'Certificate Trusted by User. Continue.'}), status.HTTP_200_OK


@app.route('/hello', methods=['GET'])
@app2.route('/hello', methods=['GET'])
def get():
    return jsonify({'message': 'hello yourself'}), status.HTTP_200_OK

# Swagger UI Route
@app.route('/static/<path:path>')
@app2.route('/static/<path:path>')
def send_static(path):
    return flask.send_from_directory('static', path)


SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.yaml'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Devops Assignment"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
app2.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Get all and insert properties
@app.route('/properties', methods=['GET', 'POST'])
@app2.route('/properties', methods=['GET', 'POST'])
def getProperties():
    API_KEY = getAPIKEY()
    # POST METHOD
    if request.method == 'POST':
        if validAPIKEY(API_KEY) == True:
            # Grab input from user
            newAddress = str(request.json['address'])
            newCity = str(request.json['city'])
            newState = str(request.json['state'])
            newZip = str(request.json['zip'])

            # Check if input is valid
            if len(newAddress) not in range(1, 201):
                return jsonify({'message': 'address is not between 1 and 200 characters'}), status.HTTP_400_BAD_REQUEST
            if len(newCity) not in range(1, 51):
                return jsonify({'message': 'city is not between 1 and 50 characters'}), status.HTTP_400_BAD_REQUEST
            if len(newState) != 2:
                return jsonify({'message': 'state is not exactly 2 characters'}), status.HTTP_400_BAD_REQUEST
            if len(newZip) not in range(5, 11):
                return jsonify({'message': 'zip is not between 5 and 10 characters'}), status.HTTP_400_BAD_REQUEST

            # Add new row to database
            else:
                cur = mysql.cursor()
                data = '''INSERT INTO hqc265.Properties(address,city,state,zip) VALUES (%s,%s,%s,%s)'''
                cur.execute(data, (newAddress, newCity, newState, newZip))
                mysql.commit()
                cur.close()
                return jsonify({'message': 'added'}), status.HTTP_200_OK
        else:
            return jsonify({'message': 'Authorization needed.'}), status.HTTP_401_UNAUTHORIZED

    # GET METHOD
    if request.method == 'GET':
        cur = mysql.cursor()
        cur.execute('''SELECT * FROM hqc265.Properties ORDER BY id ASC''')
        results = cur.fetchall()
        return jsonify(results), status.HTTP_200_OK

# Get, Delete, and Update a property based on id
@app.route('/properties/<id>', methods=['GET', 'DELETE', 'PUT'])
@app2.route('/properties/<id>', methods=['GET', 'DELETE', 'PUT'])
def getProperty(id):
    API_KEY = getAPIKEY()
    # Check if id is int
    if id.isdigit() is False:
        return jsonify({'message': 'id is not an integer'}), status.HTTP_400_BAD_REQUEST

    # GET METHOD
    if request.method == 'GET':
        cur = mysql.cursor()
        cur.execute('''SELECT * FROM hqc265.Properties WHERE id=''' + str(id))
        results = cur.fetchall()
        # Check if dictionary is empty
        if not results:
            return 'not found', status.HTTP_404_NOT_FOUND
        return jsonify(results), status.HTTP_200_OK

    # DELETE METHOD
    if request.method == 'DELETE':
        if validAPIKEY(API_KEY) == True:
            cur = mysql.cursor()
            check = '''SELECT * FROM hqc265.Properties WHERE `id`=%s'''
            cur.execute(check, str(id))
            ret = cur.fetchall()

            # Check if dictionary is empty
            if not ret:
                return jsonify({'message': 'not found'}), status.HTTP_404_NOT_FOUND
                cur.close()

            # Delete row with selected id from table
            data = '''DELETE FROM hqc265.Properties WHERE `id`=%s'''
            cur.execute(data, str(id))
            mysql.commit()
            cur.close()
            return jsonify({'message': 'deleted'}), status.HTTP_200_OK
        else:
            return jsonify({'message': 'Authorization needed.'}), status.HTTP_401_UNAUTHORIZED

    # PUT METHOD
    if request.method == 'PUT':
        if validAPIKEY(API_KEY) == True:
            cur = mysql.cursor()
            check = '''SELECT * FROM hqc265.Properties WHERE `id`=%s'''
            cur.execute(check, str(id))
            ret = cur.fetchall()

            # Check if dictionary is empty
            if not ret:
                return jsonify({'message': 'not found'}), status.HTTP_404_NOT_FOUND
                cur.close()
            # Update
            for k in request.json:
                if k == 'address':
                    newA = str(request.json['address'])
                    if len(newA) > 0:
                        data = '''UPDATE hqc265.Properties SET `address`=%s WHERE `id`=%s'''
                        cur.execute(data, (newA, str(id)))
                if k == 'city':
                    newC = str(request.json['city'])
                    if len(newC) > 0:
                        data = '''UPDATE hqc265.Properties SET `city`=%s WHERE `id`=%s'''
                        cur.execute(data, (newC, str(id)))
                if k == 'state':
                    newS = str(request.json['state'])
                    if len(newS) > 0:
                        data = '''UPDATE hqc265.Properties SET `state`=%s WHERE `id`=%s'''
                        cur.execute(data, (newS, str(id)))
                if k == 'zip':
                    newZ = str(request.json['zip'])
                    if len(newZ) > 0:
                        data = '''UPDATE hqc265.Properties SET `zip`=%s WHERE `id`=%s'''
                        cur.execute(data, (newZ, str(id)))

            mysql.commit()
            cur.close()
            return jsonify({'message': 'updated'}), status.HTTP_200_OK

        else:
            return jsonify({'message': 'Authorization needed.'}), status.HTTP_401_UNAUTHORIZED


@app2.route('/')
def startapp2():
    app2.run(host="0.0.0.0", port=12075)


@app.route('/')
def startapp():
    app.run(host="0.0.0.0", port=12070, ssl_context=(
        'HTTPS/server.crt', 'HTTPS/server.key'))


# Run Server
if __name__ == '__main__':

    Thread(target=startapp2).start()
    startapp()
    #app.run(host="0.0.0.0", port=12070, ssl_context=('HTTPS/server.crt','HTTPS/server.key'))
    #app2.run(host="0.0.0.0", port=12075)
