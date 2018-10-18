# Author: David Samuel
# Version 1.0

from os import listdir
from conf import getImagePath
from random import choice
import ctypes

def chooseWallpaper():

    listFiles = [arq for arq in listdir(getImagePath() + "/")]
    return choice(listFiles)

def changeWallpaper():

    SystemParametersInfo = ctypes.WinDLL('user32').SystemParametersInfoW
    SystemParametersInfo(0x0014, 0, getImagePath() + "\\" + chooseWallpaper(), 0x0001 | 0x0002)