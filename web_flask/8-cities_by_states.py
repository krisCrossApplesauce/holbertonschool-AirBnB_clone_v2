#!/usr/bin/python3
"""
add /cities_by_states
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontent
def teardown_appcontent(exception):
    """ tears down session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ returns html file, listing states and their cities from storage """
    states = storage.all("State")
    return render_template('8-cities_by_states.html', states=states.values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
