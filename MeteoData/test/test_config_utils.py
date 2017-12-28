'''
Created on Sep 19, 2017

@author: arturnowicki
'''
from utils.config_utils import ConfigReader

def test_get_config_when_ok():
    config = ConfigReader.get_cfg()
    assert config is not None

def test_get_host():
    host = ConfigReader.get_host()
    assert host == 'ftpmeteo.icm.edu.pl'

def test_get_user():
    user = ConfigReader().get_user()
    assert user == 'iopan'

def test_get_interp_method():
    interp_method = ConfigReader().get_interp_method()
    assert interp_method in ['spline', 'linear', 'cubic']
    
def test_get_logging_level():
    logging_level = ConfigReader().get_logging_level()
    assert logging_level in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']