import re
from datetime import datetime


from flask import Flask, request, jsonify
from flask_cors import CORS
import database as db

app = Flask(__name__)
CORS(app)

# To-do List
# create requirement.txt
# create pytest file
# a front-end simple page for playing

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=80, debug=True)


@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content


@app.route("/create_account", method=['POST'])
def post_create_account():
    info = request.get_json()
    data = [
        (info["username"], info["password"])
    ]
    # username = info["username"]  # 確定會不會有得不倒的情況 是不是應該用get
    # password = info["password"]  # 處理加密
    db.insert_data(data)
    response = jsonify({'success': True})
    return response


@app.route("/initial_DB")
def initial_DB():
    db.init_db()
