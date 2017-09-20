'''
Created on Sep 20, 2017

@author: arturnowicki
'''
from os.path import os


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # This is Project Root
CONFIG_FILE = os.path.join(ROOT_DIR, 'config/meteoConfig.conf')
LOGS_DIR = os.path.join(ROOT_DIR, 'application_logs')

MSG_NO_CONFIG_FILE = 'Config file does not exist!'