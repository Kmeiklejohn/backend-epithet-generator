import json
import os
from sprint_a import configure_app
from .helpers import EpithetGenerator, path_json
from flask import jsonify, views,flash


app = configure_app()
epithet = EpithetGenerator()
data_dump=epithet.vocab_data(path_json)



@app.route('/')
def generate_epithet():
    """Is a route for the flask app for a random epithet"""
    insult = epithet.epithet_gen(path_json, 1)
    
    return jsonify({"epithets": insult} )


@app.route('/vocabulary')
def vocab():
    
    return jsonify({"vocabulary": data_dump})
