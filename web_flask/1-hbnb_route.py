#!/usr/bin/python3
""" write a script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbhb():
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
