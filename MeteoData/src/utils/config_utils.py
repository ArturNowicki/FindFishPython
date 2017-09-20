'''
Created on Sep 19, 2017

@author: arturnowicki
'''

import configparser
from definitions import CONFIG_FILE, MSG_NO_CONFIG_FILE
from datetime import datetime
from utils.logging_utils import LoggingUtils

class ConfigReader(object):
    '''
    configuration file reader
    '''
    
    def __init__(self):
        self._tools = LoggingUtils()


    def get_config(self, CONFIG_FILE):
        logger = self._tools.get_logger()
        config = configparser.ConfigParser()
        dataset = config.read(CONFIG_FILE)
        if len(dataset) != 1:
            message = self._tools.compose_message(__file__, MSG_NO_CONFIG_FILE)
            logger.error(message)
            raise FileNotFoundError(MSG_NO_CONFIG_FILE)
        return config
        