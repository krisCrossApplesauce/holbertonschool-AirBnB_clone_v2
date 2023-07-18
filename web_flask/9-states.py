#!/usr/bin/python3
""" states stuff :P """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    states = storage.all("States")
    return render_template('9-states.html', states=states.values())


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    state = storage.get(State, id)
    if state:
        return render_template('9-states.html', state=state.values())
    else:
        pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
