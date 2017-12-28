'''
Created on Sep 20, 2017

@author: arturnowicki
'''
from os.path import os

# This is Project Root
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG_FILE = os.path.join(ROOT_DIR, '../config/meteoConfig.conf')
LOGS_FILE = os.path.join(ROOT_DIR, '../application_logs/meteo_logger.log')
