'''
Created on Sep 19, 2017

@author: arturnowicki
'''

from batch_implementations import BatchRunner, ETLImpl
from utils.logging_utils import LoggingUtils


# myConfig = ConfigReader.get_config()
def main():
    logging = LoggingUtils.setup_logger()
    logging.info(__name__ + ': Starting application.')
    batch_runner = BatchRunner(ETLImpl())
    batch_runner.consistency_check()
    batch_runner.processBatch()
    batch_runner.update_status()
    logging.info(__name__ + ': Done.')

if __name__ == '__main__':
    main()