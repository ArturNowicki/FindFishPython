'''
Created on Sep 20, 2017

@author: arturnowicki
'''
from utils.config_utils import ConfigReader
import logging
from definitions.path_definitions import LOGS_FILE

class LoggingUtils:

    @classmethod
    def setup_logger(cls):        
        logging_level = ConfigReader.get_logging_level()
        logging.basicConfig(filename = LOGS_FILE,
                    format = '%(asctime)s %(levelname)s: %(message)s',
                    level = logging_level)
        return logging
