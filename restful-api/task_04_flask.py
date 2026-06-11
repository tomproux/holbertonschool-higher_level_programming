#!/usr/bin/python3
"""Simple Flask API with user storage and JSON endpoints."""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user storage.
users = {}


@app.route("/", methods=["GET"])
def home():
    """Return the welcome message for the API."""
    return "Welcome to the Flask API!"


@app.route("/data", methods=["GET"])
def data():
    """Return the list of stored usernames."""
    return jsonify(list(users.keys()))


@app.route("/status", methods=["GET"])
def status():
    """Return the API status."""
    return "OK"


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return the full user object for a given username."""
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user from a JSON request body."""
    try:
        data = request.get_json(silent=False)
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    user = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city"),
    }
    users[username] = user

    return jsonify({"message": "User added", "user": user}), 201


if __name__ == "__main__":
    app.run(debug=True)
