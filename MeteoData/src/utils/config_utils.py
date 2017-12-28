'''
Created on Sep 19, 2017

@author: arturnowicki
'''

import configparser

from definitions.msg_definitions import MSG_NO_CONFIG_FILE
from definitions.path_definitions import CONFIG_FILE

class ConfigReader(object):
    '''
    configuration file reader
    provides getters for configuration parameters
    '''
    umRemoteHostConfig = 'umRemoteHostConfig'
    pathsConfig = 'pathsConfig'
    interpConfig = 'interpConfig'
    logConfig = 'logConfig'
    
    @classmethod
    def get_host(cls):
        return cls.get_cfg().get(cls.umRemoteHostConfig, 'host')

    @classmethod
    def get_user(cls):
        return cls.get_cfg().get(cls.umRemoteHostConfig, 'user')

    @classmethod
    def get_pass(cls):
        return cls.get_cfg().get(cls.umRemoteHostConfig, 'pass')

    @classmethod
    def get_remote_dir(cls):
        return cls.get_cfg().get(cls.umRemoteHostConfig, 'remote_dir')

    @classmethod
    def get_used_meteo_list(cls):
        return cls.get_cfg().get(cls.pathsConfig, 'old_meteo_files')

    @classmethod
    def get_interp_method(cls):
        return cls.get_cfg().get(cls.interpConfig, 'interp_method')

    @classmethod
    def get_logging_level(cls):
        return cls.get_cfg().get(cls.logConfig, 'logging_level')

    @staticmethod
    def get_cfg():
        config_parser = configparser.ConfigParser()
        dataset = config_parser.read(CONFIG_FILE)
        if len(dataset) == 0:
            raise FileNotFoundError(MSG_NO_CONFIG_FILE)
        return config_parser
