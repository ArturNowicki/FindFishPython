'''
Created on Sep 19, 2017

@author: arturnowicki
'''
from ftplib import FTP
from ftplib import all_errors as ftpErrors
from utils.connection_utils import FtpConnector

import pytest
from _pytest.outcomes import fail
from socket import gaierror

host = 'ftpmeteo.icm.edu.pl'
user = 'iopan'
passwd = 'austrul'
remoteDir = 'um'
ftp_connector = FtpConnector()

def test_get_connection_when_ok():
    ftp = ftp_connector.get_ftp_connection(host, user, passwd)
    assert ftp != None

def test_get_config_when_wrong_parameters():
    with pytest.raises(gaierror):
        ftp_connector.get_ftp_connection('wrongHost', user, passwd)
    with pytest.raises(ftpErrors):
        ftp_connector.get_ftp_connection(host, 'wrongUser', passwd)
    with pytest.raises(ftpErrors):
        ftp_connector.get_ftp_connection(host, user, 'wrongPasswd')

