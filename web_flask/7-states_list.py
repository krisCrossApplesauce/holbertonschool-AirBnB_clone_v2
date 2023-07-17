#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    return render_template('7-states_list.html', storage=storage.all())

@app.teardown_appcontext
def teardown():
    storage.close()