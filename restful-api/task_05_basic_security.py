#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt

from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret'  # Secret key for JWT

# Sample users stored in memory with hashed passwords
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("admin_password"), "role": "admin"}
}

# Initialize Flask-HTTPAuth
basic_auth = HTTPBasicAuth()
# Initialize Flask-JWT-Extended
jwt = JWTManager(app)


# Basic authentication callback
@basic_auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users[username]["password"], password):
        return username


# JWT authentication callback
@jwt.user_identity_loader
def user_identity_lookup(username):
    return users.get(username)


# Login route for JWT token generation
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Username or password is missing"}), 400

    if username in users and check_password_hash(users[username]['password'], password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401


# Protected route using Basic Authentication
@app.route('/basic-protected')
@basic_auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"}), 200


# Protected route using JWT Authentication
@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    return jsonify({"message": "JWT Auth: Access Granted"}), 200


# Role-based protected route
@app.route('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user['role'] == 'admin':
        return jsonify({"message": "Admin Access: Granted"}), 200
    else:
        return jsonify({"message": "Admin access required"}), 403


if __name__ == '__main__':
    app.run(debug=True)
