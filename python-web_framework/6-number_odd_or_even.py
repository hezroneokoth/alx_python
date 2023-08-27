#!/usr/bin/python3
"""
This script starts a Flask web application.
The web app listens on 0.0.0.0 port 5000. """

from flask import Flask, render_template
from urllib.parse import unquote
""" imports statements"""

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    decoded_text = unquote(text.replace('_', ' '))
    return "C " + decoded_text


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    decoded_text = unquote(text.replace('_', ' '))
    return "Python " + decoded_text


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even_route(n):
    return render_template(
        '6-number_odd_or_even.html',
        number=n, odd_even='odd' if n % 2 else 'even')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
