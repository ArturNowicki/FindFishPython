'''
Created on Sep 19, 2017

@author: arturnowicki
'''

import configparser

class ConfigReader(object):
    '''
    configuration reader
    '''
    def __init__(self):
        pass
    
    def getConfig(self, configFile):
        config = configparser.ConfigParser()
        dataset = config.read(configFile)
        if len(dataset) != 1:
            raise FileNotFoundError("Config file does not exist!")
        return config
        