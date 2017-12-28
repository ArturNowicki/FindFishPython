'''
Created on Sep 18, 2017

@author: arturnowicki
'''
from ftplib import FTP
from ftplib import all_errors as ftpErrors
from socket import gaierror

from utils.config_utils import ConfigReader
from utils.connection_utils import FtpConnector

def compareLists():
    
    meteo_host = ConfigReader.get_host()
    meteo_user = ConfigReader.get_user()
    meteo_pass = ConfigReader.get_pass()
    remote_dir = ConfigReader.get_remote_dir()

    try:
        ftp = FtpConnector.get_ftp_connection(meteo_host, \
                                              meteo_user, meteo_pass)
        meteoFilesList = getFilesList(ftp, remote_dir)
    except ftpErrors as e:
        logError(e)
        exit(-1)
    except gaierror as e:
        logError(e)
        exit(-1)
        
    oldMeteoListFile = ConfigReader.get_used_meteo_list()
    oldFilesList = readOldFilesList(oldMeteoListFile)
    
    filesDiff = set(meteoFilesList) - set(oldFilesList)
    print(type(set(filesDiff)))
    print(type(filesDiff))


def getFilesList(ftp, remoteDir):
    filesList = []
    ftp.cwd(remoteDir)
    ftp.retrlines('NLST', filesList.append)
    ftp.quit()
    return filesList

def readOldFilesList(oldMeteoListFile):
    try:
        with open(oldMeteoListFile) as f:
            oldFilesList = f.read().splitlines()
    except FileNotFoundError as e:
        logError(e)
        raise
    return oldFilesList

def logError(e):
    print(str(e) + " Error in: " + __name__)
    print(str(type(e)))


if __name__ == '__main__':
    compareLists()

