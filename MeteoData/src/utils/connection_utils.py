'''
Created on Sep 19, 2017
@
@author: arturnowicki
'''
from ftplib import FTP
from socket import gaierror


class FtpConnector(object):
    '''
    remote connections utility
    '''
    def __init__(self):
        pass
    
    def get_ftp_connection(self, host, user, password):
        try:
            ftp = FTP(host)
            ftp.login(user, password)
        except gaierror as e:
            raise gaierror
        return ftp
