#!/usr/bin/python3
"""
Define a Flask application.
"""
from os import getenv
from flask import Flask
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close(self):
    """ Close the current session """
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    return ({"error": "Not found"}, 404)


if (__name__ == "__main__"):
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", 5000)
    app.run(host=host, port=port, threaded=True)
