'''
Created on Sep 20, 2017

@author: arturnowicki
'''
import logging
import os.path
from definitions import LOGS_DIR
from datetime import datetime
from singleton import Singleton


class LoggingUtils(object, metaclass=Singleton):
    
    def __init__(self):
        now = datetime.now()
        error_file = str(now).replace(' ', '_')+'_errors.log'
        info_file = str(now).replace(' ', '_')+'_info.log'
        self.logger = logging.getLogger('error_logger')
        self.logger.setLevel(logging.DEBUG)
        error_fh = logging.FileHandler(os.path.join(LOGS_DIR, error_file))
        error_fh.setLevel(logging.ERROR)
        self.logger.addHandler(error_fh)
        info_fh = logging.FileHandler(os.path.join(LOGS_DIR, info_file))
        info_fh.setLevel(logging.INFO)
        self.logger.addHandler(info_fh)
    
    def get_logger(self):    
        return self.logger


    def compose_message(self, source_file, message):
        return str(datetime.now()) + source_file + message
