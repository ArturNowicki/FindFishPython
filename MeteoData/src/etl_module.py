'''
Created on Dec 28, 2017

@author: arturnowicki
'''
import logging
from utils.config_utils import ConfigReader
from utils.connection_utils import FtpConnector
from ftplib import all_errors as ftpErrors
from socket import gaierror

host = ConfigReader.get_host()
user = ConfigReader.get_user()
passwd = ConfigReader.get_pass()
remote_dir = ConfigReader.get_remote_dir()

def extract_data():
    new_dataset = get_new_dataset()
    new_dataset.
#     if new_dataset
    download_data()
    unpack_data()


def get_new_dataset():
    logging.info(__name__ + ': Retrieving new ICM files list')
    try:
        ftp = FtpConnector.get_ftp_connection(host, user, passwd)
    except ftpErrors as e:
        logging.error(__name__ + ': ' + str(e))
        raise e
    except gaierror as e:
        logging.error(__name__ + ': ' + str(e))
        raise e
    new_files_list = getFilesList(ftp, remote_dir)
    old_files_list = readOldFilesList(ConfigReader.get_used_meteo_list())
    new_files = set(set(new_files_list) - set(old_files_list))
    new_files.
    return new_files

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
        logging.error(__name__ + ': ' + str(e))
        raise e
    return oldFilesList

def download_data():
    pass

def unpack_data():
    pass