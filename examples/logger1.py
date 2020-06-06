import logging 
#import os
from cc import logger

#os.system('rm logfile1' )

#logging.basicConfig(filename = 'logfile1')#, level=logging.DEBUG )
#logger=logging.getLogger('logfile')
#logger.setLevel(logging.DEBUG)
#i=12
#logging.info("This is a info massege")
#logger.critical("This is a criticle massege")
#logger.debug("This is a debug massege")
#logger.warning("This is a warning massege")
#logger.error("This is a error massege")
#import logging,os,logging.handlers
import uuid
d= {'uuid' : str(uuid.uuid4()).upper() }
logger=logging.LoggerAdapter(logger, extra=d)
logger.error("massege from info ")

