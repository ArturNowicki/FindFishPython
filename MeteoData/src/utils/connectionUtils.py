'''
Created on Sep 19, 2017

@author: arturnowicki
'''
from ftplib import FTP

class FtpConnector(object):
    '''
    remote connections utility
    raises ftplib - all_errors; socket - gaierror
    '''
    def __init__(self):
        pass
        
    def getFtpConnection(self, host, user, passwd):
        ftp = FTP(host)
        ftp.login(user, passwd)
        return ftp
