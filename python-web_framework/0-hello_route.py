#!/usr/bin/python3
"""
This script starts a Flask web application.
The web app listens on 0.0.0.0 port 5000. """

from flask import Flask
""" imports Flask"""

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
