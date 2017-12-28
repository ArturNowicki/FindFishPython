'''
Created on Sep 19, 2017
@
@author: arturnowicki
'''
from ftplib import FTP

class FtpConnector(object):
    '''
    remote connections utility
    '''
    @staticmethod
    def get_ftp_connection(host, user, password):
        ftp = FTP(host)
        ftp.login(user, password)
        return ftp

    