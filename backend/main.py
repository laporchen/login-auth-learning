import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS
import traceback
import json

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

CORS(app, resources={r'/*': {'origins': '*'}})
data = {}
dataLocation = "./data"
dataName = "userInfo.json"


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


if __name__ == '__main__':
    app.run(port=8081)
