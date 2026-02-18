#!/usr/bin/python3

"""This module is using flask to run a local server. It's using a virtual
environment, to do tests. It manages some endpoints and permits to store, adds
and retrieve users data"""
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users = {}


@app.route("/", methods=["GET"])
def home():
    '''When there is no endpoint, this function print a simple sentence'''
    return "Welcome to the Flask API!", 200


@app.route("/data", methods=["Get"])
def data():
    '''On the endpoint /data, this function retrieves all the registered users
    '''
    users_list = list((users.keys()))
    return jsonify(users_list), 200


@app.route("/status", methods=["Get"])
def status():
    '''On the endpoint /status, this function retrieves the status of the
    server'''
    return "OK", 200


@app.route("/users/<username>", methods=["Get"])
def get_user(username):
    '''On the endpoint /users/<username> it retrieves the data of the username
    given, if no username is corresponding, it returns an error message'''
    search_user = users.get(username)
    if search_user is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify(search_user), 200


@app.route("/add_user", methods=["Post"])
def add_user():
    '''On the endpoint add_user it permits to add a user and save it into the
    data, if one field is missing it returns an error message'''
    new_user = request.get_json()
    user_model = {"username": "alice",
                  "name": "Alice",
                  "age": 25,
                  "city": "San Francisco"}
    for i in user_model:
        if i not in new_user:
            return jsonify({"error": "Username is required"}), 400

    users[new_user["username"]] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run()
