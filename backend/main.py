from re import A, M
import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import traceback
import json

keyLocation = './jwtKey.json'
try:
    f = open(keyLocation, 'r')
    jwtKey = json.load(f)
    f.close()
except:
    print('Error loading jwtKey.json,please make a new one')
    exit()
jwt = JWTManager()

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
app.config['JWT_SECRET_KEY'] = jwtKey['key']
CORS(app, resources={r'/*': {'origins': '*'}})

data = {}
dataLocation = "./data"
dataName = "userInfo.json"


@app.route('/login', methods=['POST'])
def login():
    global data
    if request.method == 'POST':
        message = {"status": "success"}
        f = open(dataLocation + "/" + dataName, "r")
        try:
            data = json.load(f)
        except:
            pass
        try:
            post_data = request.get_json()
            if post_data['email'] in data and post_data['password'] == data[post_data['email']]['password']:
                message['token'] = create_access_token(
                    identity=post_data['email'])
                message['name'] = data[post_data['email']]['firstname'] + \
                    " " + data[post_data['email']]['lastname']
                message['tasks'] = data[post_data['email']]['tasks']
            else:
                message['status'] = "fail"
                message['message'] = "Wrong email or password"
        except Exception as err:
            message = {"status": "error", "message": "Error in login"}

        return jsonify(message)


@app.route('/register', methods=['POST'])
def register():
    global data
    if request.method == 'POST':

        message = {'status': 'success'}
        post_data = request.get_json()
        f = open(dataLocation + "/" + dataName, "w+")
        try:
            data = json.load(f)
        except:
            pass
        print(post_data)
        message = {"status": "success"}
        try:
            if(post_data['email'] in data):
                message = {"status": "failure",
                           "message": "Email already been registered"}
            else:
                data[post_data['email']] = {"firstname": post_data['first_name'],
                                            "lastname": post_data["last_name"], "password": post_data['password']}
                f.write(json.dumps(data))
                f.close()
        except Exception:
            print(traceback.format_exc())
            message = {"status": "failure",
                       "message": "Error in registering user"}

        return jsonify(message)


@app.route("/user", methods=['GET'])
@jwt_required(optional=False)
def returnUser():
    global data
    if request.method == 'GET':
        try:
            f = open(dataLocation + "/" + dataName, "r")
            data = json.load(f)
            f.close()
            current_user = get_jwt_identity()
            message = {"status": "success",
                       "name": data[current_user]['firstname'] + " " + data[current_user]['lastname'], "email": current_user, "tasks": data[current_user]['tasks']}
            return jsonify(message)
        except Exception:
            print(traceback.format_exc())
            message = {"status": "failure",
                       "message": "Error in getting user info"}
            return jsonify(message)


@app.route("/update", methods=['POST'])
@jwt_required(optional=False)
def update():
    global data
    if request.method == 'POST':
        message = {"status": "success"}
        post_data = request.get_json()
        try:
            f = open(dataLocation + "/" + dataName, "r")
            data = json.load(f)
            f.close()
            current_user = get_jwt_identity()
            data[current_user]['tasks'] = post_data
            f = open(dataLocation + "/" + dataName, "w+")
            f.write(json.dumps(data))
            f.close()
        except Exception:
            print(traceback.format_exc())
            message = {"status": "failure",
                       "message": "Error in updating user info"}
            return jsonify(message)
        return jsonify(message)


if __name__ == '__main__':
    jwt.init_app(app)
    app.run(port=8081)
