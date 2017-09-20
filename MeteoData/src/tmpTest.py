'''
Created on Sep 20, 2017

@author: arturnowicki
'''
from utils.logging_utils import LoggingUtils
from time import sleep

utils1 = LoggingUtils()
logger1 = utils1.get_logger()

utils2 = LoggingUtils()
logger2 = utils2.get_logger()

logger1.error("a;sldkfjsalfkj")
sleep(2000)

logger2.error("a;sldkfjsalfkj")
