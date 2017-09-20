'''
Created on Sep 19, 2017

@author: arturnowicki
'''
import inspect
import os.path
from utils.config_utils import ConfigReader
from definitions import CONFIG_FILE

import pytest

config_reader = ConfigReader()

def test_get_config_when_0k():
    config = config_reader.get_config(CONFIG_FILE)
    assert config is not None

def test_get_config_when_wrong_config_file():
    with pytest.raises(FileNotFoundError):
        config = config_reader.get_config('wrong/config.cfg')
