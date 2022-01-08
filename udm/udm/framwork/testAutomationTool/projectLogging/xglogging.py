import logging
import logging.handlers
import os
from jsonformatter import JsonFormatter
path = os.path.dirname(os.path.abspath(__file__))

def createLogging(name, filename= path +'/amantya.log'):

    if filename == '':
        return None
    tlogger = logging.getLogger(name)
    #tlogger.handlers = []
    tlogger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s -%(filename)s - %(lineno)d - %(levelname)s - %(message)s')
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    fh = logging.handlers.RotatingFileHandler(filename, maxBytes=512*1024, backupCount=5)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    tlogger.addHandler(console)
    tlogger.addHandler(fh)
    return tlogger

def addFileHandler(filename, tlogger):
    """
    Add file handler in the logger
    """
    file_h = logging.FileHandler(filename)
    formatter = logging.Formatter('%(asctime)s -%(filename)s - %(lineno)d - %(levelname)s - %(message)s')
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    fh = logging.handlers.RotatingFileHandler(filename, maxBytes=512 * 1024, backupCount=5)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    tlogger.addHandler(file_h)
    tlogger.addHandler(console)
    tlogger.addHandler(fh)
    return tlogger

def delFileHandler(tlogger):
    """
    Delete file handlers from logger
    """
    thandler = tlogger.handlers
    while thandler:
        for i in thandler:
            print(i)
            tlogger.removeHandler(i)
            i.flush()
            i.close()
        thandler = tlogger.handlers

def loggingFormattest(logger):
    logger.info("now testing format for func name")

def get_xglogger():
    return logging.getLogger('xg1Klogger')

def createJsonLogging(name, filename= path + '/amantya.log'):
    STRING_FORMAT = '''{
        "Asctime":         "asctime",
        "Filename":        "filename",
        "Lineno":          "lineno",
        "Levelname":       "levelname",
        "FuncName":        "funcName",
        "Message":         "message"
        }'''
    tlogger = logging.getLogger()
    tlogger.setLevel(logging.DEBUG)
    formatter = JsonFormatter(STRING_FORMAT)
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    fh = logging.handlers.RotatingFileHandler(filename, maxBytes=512*1024, backupCount=5)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    tlogger.addHandler(console)
    tlogger.addHandler(fh)
    return tlogger

if __name__ == '__main__':
    #l=createLogging('xg1Klogger')
    #l.warn("logging start")
    #loggingFormattest(l)
    #delFileHandler(logging.getLogger('xg1Klogger'))
    l=createJsonLogging('xg1Klogger')
    l.warn("logging start")
