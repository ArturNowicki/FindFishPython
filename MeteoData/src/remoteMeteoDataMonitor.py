'''
Created on Sep 18, 2017

@author: arturnowicki
'''
from ftplib import FTP
import inspect
import os.path

from utils.configUtils import ConfigReader
from utils.connectionUtils import FtpConnector
from ftplib import all_errors as ftpErrors
from socket import gaierror

thisFile = os.path.abspath(inspect.getfile(inspect.currentframe()))

def compareLists():

    meteoConfigPath = 'config/meteoConfig.cfg'
    meteoConfigSection = 'MeteoConfig'
    pathConfigSection = 'Paths'
    projectDir = os.path.dirname(os.path.dirname(thisFile))
    configFile = os.path.join(projectDir, meteoConfigPath)

    configReader = ConfigReader()
    try:
        config = configReader.getConfig(configFile)
    except FileNotFoundError as e:
        logError(e)
        exit(-1)

    meteoHost = config.get(meteoConfigSection, 'host')
    meteoUser = config.get(meteoConfigSection, 'user')
    meteoPass = config.get(meteoConfigSection, 'pass')
    remoteDir = config.get(meteoConfigSection, 'remoteDir')

    ftpConnector = FtpConnector()
    try:
        ftp = ftpConnector.getFtpConnection(meteoHost, meteoUser, meteoPass)
        meteoFilesList = getFilesList(ftp, remoteDir)
    except ftpErrors as e:
        logError(e)
        exit(-1)
    except gaierror as e:
        logError(e)
        exit(-1)
        
    oldMeteoListFile = config.get(pathConfigSection, 'oldMeteoFiles')
    oldMeteoListFile = os.path.join(projectDir, oldMeteoListFile)
    
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
    print(str(e) + " Error in: " + thisFile)
    print(str(type(e)))


if __name__ == '__main__':
    compareLists()

