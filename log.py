# Author: David Samuel
# Version 1.0

def createLogFile(text):

    f = open("log",'w')
    f.writelines(text)
    f.close()