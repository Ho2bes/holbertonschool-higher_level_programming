#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample users stored in memory
users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
}

# Root endpoint
@app.route("/")
def home():
    return "Welcome to the Flask API!"

# Serving JSON data of all users
@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))

# Status endpoint
@app.route("/status")
def get_status():
    return "OK"

# Get user by username
@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return "User not found", 404

# Add user endpoint
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.json
    if "username" in data:
        username = data["username"]
        if username not in users:
            users[username] = {
                "name": data.get("name", ""),
                "age": data.get("age", ""),
                "city": data.get("city", "")
            }
            return jsonify({"message": "User added successfully", "user": users[username]}), 201
        else:
            return "User already exists", 400
    else:
        return "Username not provided", 400

if __name__ == "__main__":
    app.run(debug=True)
