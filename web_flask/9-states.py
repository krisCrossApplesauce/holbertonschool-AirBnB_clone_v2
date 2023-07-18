#!/usr/bin/python3
""" states stuff :P """
from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.route('/states', strict_slashes=False)
def states_list():
    states = storage.all("State")
    return render_template('9-states.html', states=states.values())


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    state = storage.get(State, id)
    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('9-states.html', not_found=False, state=state, cities=cities)
    else:
        return render_template('9-states.html', not_found=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
