'''
Created on Sep 19, 2017

@author: arturnowicki
'''
import inspect
import os.path
from definitions import ROOT_DIR, CONFIG_PATH
METEO_CONFIG_PATH = 'config/meteoConfig.cfg'
this_file = os.path.abspath(inspect.getfile(inspect.currentframe()))
project_dir = os.path.dirname(os.path.dirname(this_file))
config_file = os.path.join(project_dir, METEO_CONFIG_PATH)

def main():
    print(ROOT_DIR)
    print(CONFIG_PATH)

if __name__ == '__main__':
    main()