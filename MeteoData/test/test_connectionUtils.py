'''
Created on Sep 19, 2017

@author: arturnowicki
'''
from ftplib import FTP
from ftplib import all_errors as ftpErrors
from utils.connectionUtils import FtpConnector

import pytest
from _pytest.outcomes import fail
from socket import gaierror

host = 'ftpmeteo.icm.edu.pl'
user = 'iopan'
passwd = 'austrul'
remoteDir = 'um'
ftpConnector = FtpConnector()

def test_GetConnectionAllOk():
    ftp = ftpConnector.getFtpConnection(host, user, passwd)
    assert ftp != None

def test_GetConfigWrongParameters():
    with pytest.raises(gaierror) as excInfo:
        ftpConnector.getFtpConnection('wrongHost', user, passwd)
    with pytest.raises(ftpErrors):
        ftpConnector.getFtpConnection(host, 'wrongUser', passwd)
    with pytest.raises(ftpErrors):
        ftpConnector.getFtpConnection(host, user, 'wrongPasswd')

