'''
Created on Dec 28, 2017

@author: arturnowicki
'''
from utils.logging_utils import LoggerUtils

def test_logging():
    my_logger = LoggerUtils.setup_logger()
    my_logger.debug("debug")
    my_logger.info("info")
    my_logger.warning('warning')
    my_logger.error('error')
    my_logger.critical('critical')
