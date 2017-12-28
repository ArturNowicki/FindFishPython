'''
Created on Sep 19, 2017

@author: arturnowicki
'''
from ftplib import FTP
from ftplib import all_errors as ftpErrors
from socket import gaierror

import pytest

from utils.connection_utils import FtpConnector


host = 'ftpmeteo.icm.edu.pl'
user = 'iopan'
passwd = 'austrul'
remoteDir = 'um'

def test_get_connection_when_ok():
    ftp = FtpConnector.get_ftp_connection(host, user, passwd)
    assert ftp != None

def test_get_config_when_wrong_host():
    with pytest.raises(gaierror):
        FtpConnector.get_ftp_connection('wrongHost', user, passwd)

def test_get_config_when_wrong_user():
    with pytest.raises(ftpErrors):
        FtpConnector.get_ftp_connection(host, 'wrongUser', passwd)
    
def test_get_config_when_wrong_password():
    with pytest.raises(ftpErrors):
        FtpConnector.get_ftp_connection(host, user, 'wrongPasswd')

