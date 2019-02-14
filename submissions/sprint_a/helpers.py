#!/usr/bin/python3

import os
import json
import random
import json
from flask import jsonify


dir_path = os.path.abspath("../../resources")
path_json = os.path.join(dir_path, "data.json")


class FileManager:
    """Handle local file system IO."""
    
    @staticmethod
    def get_extension(path):
        """Get file extension from file path."""
        return os.path.splitext(path)[-1][1:]

    @staticmethod
    def read_json(path, mode='r', *args, **kwargs):
        with open(path, mode=mode, *args, **kwargs) as handle:
            return json.load(handle)

class Vocabulary:
    """Standardize vocabulary representation from multiple sources."""

    files = FileManager()

    @classmethod
    def from_file(cls, path, *args, **kwargs):
        extension = cls.files.get_extension(path)
        representation = cls.strategies(extension)(path, *args, **kwargs)
        return representation

    @classmethod
    def from_json(cls, path, fields=True, *args, **kwargs):
        data = cls.files.read_json(path, *args, **kwargs)
        if fields:
            representation = (data, data.keys())
        else:
            representation = data
        return representation

    @classmethod
    def strategies(cls, file_extension, intent='read'):
        input_strategies = {'json': cls.from_json}
        if intent is 'read':
            return input_strategies[file_extension]


class EpithetGenerator(object):
    vocab = Vocabulary()
    files = FileManager()
    
    def random_word(self, column):
        random_item = random.choice(column)    
        return random_item 

    def epithet_data(self, path_json, num):
        epithet_list = []
        for i in range(num):   
            data = self.files.read_json(path_json)
            column1 = data['Column 1']
            column2 = data['Column 2']
            column3 = data['Column 3']
            
            vocab1 = self.random_word(column1)
            vocab2 = self.random_word(column2)
            vocab3 = self.random_word(column3)
            epithet = [vocab1, vocab2, vocab3]
            epithet_list.append(epithet)

        return epithet_list

epithet = EpithetGenerator()

epithet.epithet_data(path_json, 10)