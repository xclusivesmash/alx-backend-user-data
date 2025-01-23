#!/usr/bin/env python3
"""
module: app
description: application entry point.
"""
from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()
app = Flask(__name__)
app.strict_slashes = False


@app.route("/", methods=['GET'])
def home() -> str:
    """ implements: GET / method.
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'])
def users() -> str:
    """ implements: POST /users
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = AUTH.register_user(email, password)
        if user is None:
            return
        return jsonify({"email": user.email, "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
