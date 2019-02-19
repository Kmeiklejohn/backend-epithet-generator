import json
import os
from sprint_a import configure_app
from .helpers import EpithetGenerator, path_json
from flask import jsonify, views,flash


app = configure_app()
epithet = EpithetGenerator()
data_dump = epithet.vocab_data(path_json)
random_int = epithet.random_num()


@app.route('/')
def generate_epithet():
    """Is a route for the flask app for a random epithet"""
    
    insult = epithet.epithet_gen(path_json, 1)
    return jsonify({"epithet": insult} )


@app.route('/vocabulary')
def vocab():  
    """returns json data of the vocab words used"""
    return jsonify({"vocabulary": data_dump})

@app.route('/epithet')
def random_epithets():
    """returns a random amount of epithets"""
    random_epit = epithet.epithet_gen(path_json, random_int)
    return jsonify({"epithets": random_epit})

@app.route('/epithets/<int:num>/')
def number_of_epithets(num):
    
    random_amount = epithet.epithet_gen(path_json, num)
    return jsonify({"epithets": random_amount} )
    