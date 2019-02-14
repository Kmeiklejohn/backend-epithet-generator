import json
import os
from sprint_a import configure_app
from .helpers import EpithetGenerator, path_json
from flask import jsonify, views,flash


app = configure_app()
epithet = EpithetGenerator()
insult = epithet.epithet_data(path_json, 3)




@app.route('/')
def generate_epithet():
    """Is a route for the flask app for a random epithet"""
    
    return jsonify(epithets=insult)


@app.route('/vocabulary')
def vocab():
    
    return jsonify(vocabulary=insult)
