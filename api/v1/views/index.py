#!/usr/bin/python3
"""
Define a route to check API status
"""
from api.v1.views import app_views
from json import loads


@app_views.route("/status")
def status():
    return loads('{"status": "OK"}')
