''' This file is a library file for the weather. 
    It is meant to be imported into the mainMenu and called when needed.'''
import os as sh 
from sources import * 
sleep0 = 'sleep 1' 
def getWeather():
    print(f'Getting the weather for {zip_code}...')
    sh.system(sleep0)
    sh.system(f'curl wttr.in/{zip_code}')
# this code ensures the module doesn't run at import time.
if __name__ == '__main__':
    getWeather()