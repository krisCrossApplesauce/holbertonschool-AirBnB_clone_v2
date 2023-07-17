#!/usr/bin/python3
""" add /number_template/<n> """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('templates/5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
