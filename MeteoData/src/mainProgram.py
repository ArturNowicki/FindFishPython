'''
Created on Sep 19, 2017

@author: arturnowicki
'''
import inspect
import os.path

meteoConfigPath = 'config/meteoConfig.cfg'
thisFile = os.path.abspath(inspect.getfile(inspect.currentframe()))
projectDir = os.path.dirname(os.path.dirname(thisFile))
configFile = os.path.join(projectDir, meteoConfigPath)

def main():
    pass

if __name__ == '__main__':
    main()