#!/usr/bin/python3
"""
This a script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
import uuid

app = Flask(__name__)


@app.route('/1-hbnb/')
def hbnb():
    """city objects"""
    cities = storage.all(City)
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template('0-hbnb.html',
                           cities=cities,
                           states=states,
                           amenities=amenities,
                           places=places,
                           cache_id = uuid.uuid4())


@app.teardown_appcontext
def storage_teardown(exception):
    """calls the close function on states"""
    from models import storage
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
