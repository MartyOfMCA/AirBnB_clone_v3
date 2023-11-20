#!/usr/bin/python3
"""
Define a route to check API status
"""
from api.v1.views import app_views
from json import loads
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route("/status")
def status():
    return loads('{"status": "OK"}')


@app_views.route("/stats")
def num_of_objects():
    objects = {"amenities": 0,
               "cities": 0,
               "places": 0,
               "reviews": 0,
               "states": 0,
               "users": 0}
    for key in objects.keys():
        # Create a duplicate of the current key
        cls = key
        # Obtain the class from the key
        cls = cls.replace(cls[0], cls[0].upper())
        cls = cls.replace("ies", "y") if cls.endswith("ies") else cls[0:-1]
        cls = eval(cls)

        objects[key] = storage.count(cls)

    return (objects)
