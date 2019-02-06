import json
import os
from sprint_a import configure_app
from flask import jsonify

app = configure_app()


@app.route('/')
def generate_epithet():
    """Is a route for the flask app for a random epithet"""

    return jsonify({"epithets": []}, {"vocabulary": {}})


@app.route('/vocabulary')
def vocab():

    return jsonify({"vocabulary": {}})
