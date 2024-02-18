#!/usr/bin/python3
""" this module contains a script that starts a Flask web application
    the web application must be listening on 0.0.0.0, port 5000
    Routes: - /hbnb_filters """
from models import *
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from flask import Flask, render_template
app = Flask(__name__)


classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


@app.route('/hbnb', strict_slashes=False)
def hbnb_filters():
    """ hbnb_filters method: display HTML page state & city from DBStorage """
    states = storage.all(State).values()
    ameninities = storage.all(Amenity).values()
    reviews = storage.all(Review).values()
    cities = storage.all(City).values()
    places = storage.all(Place).values()
    users = storage.all(User).values()
    states = sorted(list(states), key=lambda x: x.name)
    ameninities = sorted(list(ameninities), key=lambda x: x.name)
    reviews = sorted(list(reviews), key=lambda x: x.name)
    cities = sorted(list(cities), key=lambda x: x.name)
    places = sorted(list(places), key=lambda x: x.name)
    users = sorted(list(users), key=lambda x: x.name)
    return (render_template('100-hbnb.html', states=states,
                            amenities=ameninities, reviews=reviews,
                            cities=cities, places=places,
                            users=users))


@app.teardown_appcontext
def remove_SQLalc_session(exception):
    """ close storage when tear down is called """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
