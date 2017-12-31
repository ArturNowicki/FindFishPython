'''
Created on Dec 28, 2017

@author: arturnowicki
'''
import logging

# Fronting/Proxy of main apps flow surrogates
# 

class ETLProxy:
    def __init__(self, implementation):
        self.__implementation = implementation
    # Pass method calls to the implementation:
    def extract(self): self.__implementation.extract()
    def transform(self): self.__implementation.transform()
    def load(self): self.__implementation.load()


class BatchRunnerProxy:
    def __init__(self, etl_impl):
        self.__etl_impl = etl_impl

    def consistency_check(self):
        raise NotImplementedError
    def update_status(self):
        raise NotImplementedError
    
    def processBatch(self):
        etl_proxy = ETLProxy(self.__etl_impl)
        etl_proxy.extract()
        etl_proxy.transform()
        etl_proxy.load()

