#!/usr/bin/python3
"""HBNB"""


from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """merely getting states"""
    states = storage.all("State")
    return render_template("9-states.html", states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """displaying state with id and info and cities"""
    states = storage.all("State")
    for s in storage.all("State").values():
        if s.id == id:
            return render_template("9-states.html", state=s)
    return render_template("9-states.html", states=states)


@app.teardown_appcontext
def teardown_meth(e):
    """teardown method to close SQLALCHEMY sessions"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
