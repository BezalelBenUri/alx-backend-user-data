#!/usr/bin/env python3
"""
A simple Flask app with user authentication features.
"""

from db import DB
from user import User

from auth import Auth

from flask.helpers import make_response
from flask import Flask, abort, jsonify, redirect, request

AUTH = Auth()

app = Flask(__name__)

@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """
    GET /
    Return:
        - JSON payload containing a welcome message.
    """
    return jsonify({"message": "Bienvenue"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
