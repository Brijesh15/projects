import logging,os,logging.handlers
#import uuid

#d= {'uuid' : str(uuid.uuid4()).upper() }

FORMAT = "%(asctime)-15s -%(uuid)s - %(message)s- %(filename)s- %(lineno)d - %(levelname)s "
logger = logging.getLogger("tcpserver")
logging.basicConfig(format=FORMAT)
#logger= logging.handlers.RotatingFileHandler( maxBytes=512*1024 , backupCount=5 )
#logger=logging.LoggerAdapter(logger , extra=d)
#logger.warning("Protocol problem: " )
#os.system('python logger1.py')









