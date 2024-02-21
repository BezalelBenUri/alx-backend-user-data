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

@app.route('/users', methods=['POST'])
def users() -> str:
    """POST /users
    Return:
        - JSON payload of the form containing various information.
    """
    # Get the email and password from form data
    email, password = request.form.get("email"), request.form.get("password")
    try:
        # Register the user
        AUTH.register_user(email, password)
        # Respond with the following JSON payload:
        # {"email": "<registered email>", "message": "user created"}
        return jsonify({"email": email, "message": "user created"})
    # If the user is already registered, catch the exception and return a
    # JSON payload of the form: {"message": "email already registered"}
    # and return a 400 status code
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
