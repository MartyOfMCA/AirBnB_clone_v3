#!/usr/bin/python3
"""
Define a view for State objects.
"""
from flask import abort, request, jsonify
from api.v1.views import app_views
from models.state import State
from models import storage
from json import loads


@app_views.route("/states", strict_slashes=False)
def get_states():
    """
    Retrieve a list of states available.

    Return
        A list of all the states available
        or an empty list if there are no
        states.
    """
    return (jsonify([state.to_dict() for state in
            storage.all("State").values()]))


@app_views.route("/states/<string:id>")
def get_state_by_id(id):
    """
    Retrieve the state that matches the given
    id.

    Parameters
    id : string
        The id for the state to retrieve

    Return
        The state that macthes the given id
        otherwise error 404 is thrown.
    """
    for state in storage.all("State").values():
        if (state.id == id):
            return (state.to_dict())

    abort(404)


@app_views.route("/states/<string:id>", methods=["DELETE"],
                 strict_slashes=False)
def delete_state_by_id(id):
    """
    Delete the state with the given id.

    Parameters
    id : string
        The id for the state to delete

    Return
        An empty dictionary with the status code
        of 200 otherwise error 404 is
        raised.
    """
    for state in storage.all("State").values():
        if (state.id == id):
            # state.delete()
            storage.delete(state)
            storage.save()
            return ({}, 200)

    abort(404)


@app_views.route("/states", methods=["POST"],
                 strict_slashes=False)
def add_state():
    """
    Store a new State object.

    Return
        The newly added State object with the
        response code 201 (created) otherwise
        an appropriate error message along with
        response code 400.
    """
    data = request.get_json()

    if (type(data) is dict):
        if ("name" in data):
            state = State()
            state.name = data.get("name")
            storage.new(state)
            storage.save()
            return (state.to_dict(), 201)
        else:
            abort(400, "Missing name")
    else:
        abort(400, "Not a JSON")


@app_views.route("/states/<string:id>", methods=["PUT"],
                 strict_slashes=False)
def update_state(id):
    """
    Update the State with the given id.

    Parameters
    id : string
            The id for the State to update
    """
    data = request.get_json()

    if (type(data) is dict):
        for state in storage.all("State").values():
            if (state.id == id):
                state.name = data["name"]
                storage.save()
                return (state.to_dict())

        abort(404)
    else:
        abort(400, "Not a JSON")
