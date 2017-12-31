'''
Created on Dec 31, 2017

@author: arturnowicki
'''

class FTPLoginException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
