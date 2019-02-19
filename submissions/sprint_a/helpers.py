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
    epithet_list = []

    def random_word(self, column):
        """randomn number generator"""
        random_item = random.choice(column)    
        return random_item 

    def epithet_gen(self, path_json, num):
        """Returns a random epithet from the three columns of vocab"""
        self.epithet_list = []

        for i in range(num):   
            data = self.files.read_json(path_json)
            column1 = data['Column 1']
            column2 = data['Column 2']
            column3 = data['Column 3']
            
            vocab1 = self.random_word(column1)
            vocab2 = self.random_word(column2)
            vocab3 = self.random_word(column3)
            epithet = f'Thou {vocab1} {vocab2} {vocab3}'
            self.epithet_list.append(epithet)
            
        return self.epithet_list

    def vocab_data(self, path_json):
        """Returns the vocab used for the epithet"""

        vocab_data = self.files.read_json(path_json)
        return vocab_data

    def random_num(self):
        return random.randint(1, 50)
    
    