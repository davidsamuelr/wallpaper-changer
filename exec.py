# Author: David Samuel
# Version 1.0

from reg import modifyReg
from wallpaper import changeWallpaper
from log import createLogFile
import time

if __name__ == '__main__':

    text = str(time.ctime())

    try:
        modifyReg()
        changeWallpaper()

    except FileNotFoundError:
        text = "Directory not found " + text

    except IndexError:
        text = "Directory can not be empty " + text

    except PermissionError:
        text = "Access denied " + text

    finally:
        createLogFile(text)