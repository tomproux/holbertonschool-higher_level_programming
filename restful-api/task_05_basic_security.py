#!/usr/bin/python3
"""Flask API with basic authentication and JWT-based security."""

from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt_identity,
    jwt_required,
)
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "this-is-a-very-strong-secret-key-for-jwt-auth-2026"
app.config["JWT_ALGORITHM"] = "HS256"

jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


@jwt.unauthorized_loader
def unauthorized_loader(_error):
    """Return a 401 response for missing or invalid JWT tokens."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def invalid_token_loader(_error):
    """Return a 401 response for malformed or invalid JWT tokens."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def expired_token_loader(_header, _payload):
    """Return a 401 response for expired JWT tokens."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def revoked_token_loader(_jwt_header, _jwt_payload):
    """Return a 401 response for revoked JWT tokens."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def needs_fresh_token_loader(_jwt_header, _jwt_payload):
    """Return a 401 response when a fresh token is required."""
    return jsonify({"error": "Fresh token required"}), 401


@app.route("/basic-protected", methods=["GET"])
def basic_protected():
    """Protect a route using HTTP basic authentication."""
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({"error": "Basic authentication required"}), 401

    user = users.get(auth.username)
    if user is None or not check_password_hash(user["password"], auth.password):
        return jsonify({"error": "Invalid credentials"}), 401

    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Authenticate a user and return a JWT token."""
    data = request.get_json(silent=True) or {}
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    user = users.get(username)
    if user is None or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(
        identity=username,
        additional_claims={"role": user["role"]},
    )
    return jsonify({"access_token": token})


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """Protect a route using JWT authentication."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Allow only admins to access the route."""
    current_user = users.get(get_jwt_identity())
    if current_user is None or current_user.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run(debug=True)
