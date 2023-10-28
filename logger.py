import time
import logging

def getLogger(logger_name,file_name):
    logger = logging.getLogger(logger_name)

    # Create formatter
    formatter = logging.Formatter(
            '%(levelname)-9s %(asctime)s %(name)-12s  %(message)s')

    # Create streaming handler
    handler = logging.StreamHandler() 
    handler.setFormatter(formatter)

    # Create file handler
    file_handler = logging.FileHandler(filename=file_name)
    file_handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
    return logger