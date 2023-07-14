#!/usr/bin/python3
""" add route /c/<text> """
from flask import Flask

app = Flask(__name__)


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return "C {}".format(text.replace("_", " "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
