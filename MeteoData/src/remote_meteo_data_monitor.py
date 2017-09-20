'''
Created on Sep 18, 2017

@author: arturnowicki
'''
from ftplib import FTP
import inspect
import os.path

from utils.config_utils import ConfigReader
from utils.connection_utils import FtpConnector
from ftplib import all_errors as ftpErrors
from socket import gaierror

this_file = os.path.abspath(inspect.getfile(inspect.currentframe()))

def compareLists():
    
    METEO_CONFIG_PATH = 'config/meteoConfig.cfg'
    pathConfigSection = 'Paths'
    
    project_dir = os.path.dirname(os.path.dirname(this_file))
    config_file = os.path.join(project_dir, METEO_CONFIG_PATH)

    config_reader = ConfigReader()
    try:
        config = config_reader.get_config(config_file)
    except FileNotFoundError as e:
        logError(e)
        exit(-1)

    meteoHost = config.get(meteo_config_section, 'host')
    meteoUser = config.get(meteo_config_section, 'user')
    meteoPass = config.get(meteo_config_section, 'pass')
    remote_dir = config.get(meteo_config_section, 'remote_dir')

    ftp_connector = FtpConnector()
    try:
        ftp = ftp_connector.get_ftp_connection(meteoHost, meteoUser, meteoPass)
        meteoFilesList = getFilesList(ftp, remote_dir)
    except ftpErrors as e:
        logError(e)
        exit(-1)
    except gaierror as e:
        logError(e)
        exit(-1)
        
    oldMeteoListFile = config.get(pathConfigSection, 'oldMeteoFiles')
    oldMeteoListFile = os.path.join(project_dir, oldMeteoListFile)
    
    try:
        oldFilesList = readOldFilesList('oldMeteoListFile')
    except FileNotFoundError as e:
        exit(-1)
    
    filesDiff = set(meteoFilesList) - set(oldFilesList)
    
    print(filesDiff)







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

