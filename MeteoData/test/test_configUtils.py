'''
Created on Sep 19, 2017

@author: arturnowicki
'''
import inspect
import os.path
from utils.configUtils import ConfigReader

import pytest

meteoConfigPath = 'config/meteoConfig.cfg'
this_file = os.path.abspath(inspect.getfile(inspect.currentframe()))
project_dir = os.path.dirname(os.path.dirname(this_file))
configReader = ConfigReader()

def test_GetConfigAllOk():
    configFile = os.path.join(project_dir, meteoConfigPath)
    config = configReader.getConfig(configFile)
    assert config != None

def test_GetConfigWrongFile():
    configFile = 'wrong/path/meteoConfig.cfg'
    with pytest.raises(FileNotFoundError):
        configReader.getConfig(configFile)
