import logging , os
os.system('rm first_logfile.log second_logfile.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s  %(uuid)s')


def setup_logger(name, log_file, level=logging.INFO):
    """Function setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# first file logger
logger = setup_logger('first_logger', 'first_logfile.log')
logger.info('This is just info message')

# second file logger
logger = setup_logger('second_logger', 'second_logfile.log')
logger.error('This is an error message')

