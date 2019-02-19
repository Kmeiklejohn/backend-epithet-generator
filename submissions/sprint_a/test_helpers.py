#!/usr/bin/python3
import pytest 
import os
import urllib
# from .app import app as myapp
from .helpers import Vocabulary, FileManager, EpithetGenerator
from flask import Flask
from flask_testing import LiveServerTestCase 
from unittest.mock import patch



dir_path = os.path.abspath("../../resources")
path_json = os.path.join(dir_path, "data.json")
path_csv = os.path.join(dir_path, "data.csv")
ext_path = os.path.join(dir_path, 'data')

class Test_file_manager:
    """test the file manager"""


    file = FileManager()
    
    def test_get_ext(self):
        assert self.file.get_extension(ext_path) == 'json' or 'csv'
    
    def test_read_json(self):
        assert self.file.read_json(path_json)


class Test_vocab:
    """test the vocab dict"""

    data = Vocabulary()

    def test_from_file(self):
        assert self.data.from_file(path_json)
    
    def test_from_json(self):
        assert self.data.from_json(path_json)

class TestEpithet:
    """test the epithet generator"""

    test_epithet = EpithetGenerator()

    def test_vocab_data(self):
        assert self.test_epithet.vocab_data(path_json)
        

class TestFlask:
    """test flask connections and json data"""
    
    def test_json_data_index(self, client):
        res = client.get('/')
        assert res == 200
        assert res.json is not None
        assert res.json['epithet'] is not None
        assert len(res.json['epithet']) == 1

    def test_vocab_json(self, client):
        res = client.get('/vocabulary')
        assert res == 200
        assert res.json is not None
        assert res.json['vocabulary'] is not None

    @patch("random.randint", return_value=3)
    def random_epithet_test(self, client, a):
        res = client.get('/epithet')
        assert res == 200 
        assert res.json['epithets'] is not None
        assert len(res.json['epithets']) == 3

    def num_epithets_test(self, client):
        res = client.get('/epithet/10')
        assert res == 200
        assert res.json['epithets'] is not None
        assert len(res.json['epithets']) == 10