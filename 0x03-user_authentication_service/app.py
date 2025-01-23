#!/usr/bin/env python3
"""
module: app
description: application entry point.
"""
from flask import Flask, jsonify


app = Flask(__name__)
app.strict_slashes = False


@app.route("/", methods=['GET'])
def home() -> str:
    """ implements: GET / method.
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
