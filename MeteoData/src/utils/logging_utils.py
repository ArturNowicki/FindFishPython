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
        now = datetime.now()
        log_date = str(datetime.today().date()).replace('-', '_')
        log_hour = now.hour
        log_minute = now.minute
        f_name = '%s_%s_%s_meteo.log' % (log_date, log_hour, log_minute)
        logging_level = ConfigReader.get_logging_level()
        logging.basicConfig(filename = os.path.join(LOGS_DIR, f_name),
                    format = '%(asctime)s %(levelname)s: %(message)s',
                    level = logging_level)
        return logging
