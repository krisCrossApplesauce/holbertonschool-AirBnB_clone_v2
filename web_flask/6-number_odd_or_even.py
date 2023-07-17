#!/usr/bin/python3
""" add /number_odd_or_even/<n> """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    even_odd = ""
    if n % 2:
        even_odd = "odd"
    else:
        even_odd = "even"
    return render_template('6-number_odd_or_even.html', n=n, even_odd=even_odd)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
