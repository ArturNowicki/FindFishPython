'''
Created on Sep 20, 2017

@author: arturnowicki
'''
from time import sleep

from utils.logging_utils import LoggingUtils


logger1 = LoggingUtils().get_logger()
logger2 = LoggingUtils().get_logger()

logger1.warning("a;sldkfjsalfkj")
sleep(200)
print("aaa")