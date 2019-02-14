#!/usr/bin/python3
import pytest 
import os
from pathlib import Path
from .helpers import Vocabulary
from .helpers import FileManager

dir_path = os.path.abspath("../../resources")
path_json = os.path.join(dir_path, "data.json")
path_csv = os.path.join(dir_path, "data.csv")
ext_path = os.path.join(dir_path, 'data')

class Test_file_manager(object):
    file = FileManager()
    
    def test_get_ext(self):
        assert self.file.get_extension(ext_path) == 'json' or 'csv'
    
    def test_read_json(self):
        assert self.file.read_json(path_json)


class Test_vocab(object):
    data = Vocabulary()

    def test_from_file(self):
        assert self.data.from_file == self.data.from_file
    
    def test_from_json(self):
        assert self.data.from_json(path_json)