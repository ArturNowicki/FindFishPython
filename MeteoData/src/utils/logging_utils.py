'''
Created on Sep 20, 2017

@author: arturnowicki
'''
from utils.config_utils import ConfigReader
import logging
from definitions.path_definitions import LOGS_DIR
import os
from datetime import datetime

class LoggingUtils:

    @classmethod
    def setup_logger(cls):
        f_name = str(datetime.today().date()).replace('-', '_') + '_meteo.log'

        logging_level = ConfigReader.get_logging_level()
        logging.basicConfig(filename = os.path.join(LOGS_DIR, f_name),
                    format = '%(asctime)s %(levelname)s: %(message)s',
                    level = logging_level)
        return logging
