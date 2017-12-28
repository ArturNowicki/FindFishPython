'''
Created on Dec 28, 2017

@author: arturnowicki
'''
from batch_proxies import BatchRunnerProxy
import logging
from etl_module import extract_data

class ETLImpl:

    def __init__(self):
        logging.info(type(self).__name__ + ': Beginning ETL process.')
    
    def extract(self):
        extract_data()
    def transform(self):
        print('transfer icm data')
    def load(self):
        print('load icm data')

class BatchRunner(BatchRunnerProxy):
    def consistency_check(self):
#         return BatchRunnerProxy.consistency_check(self)
        logging.warning(type(self).__name__ + ': Consistency_check not implemented')

    def update_status(self):
        logging.warning(type(self).__name__ + ': Update_status not implemented')
#         return BatchRunnerProxy.update_status(self)
    