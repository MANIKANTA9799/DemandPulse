import logging 
from datetime import datetime 
import os 
LOG_DIR = "logs"
os.makedirs(LOG_DIR,exist_ok = True )
application_log_file = os.path.join(LOG_DIR,"application.log")
error_log_file = os.path.join(LOG_DIR,"error.log")



def get_logger(name:str)->logging.Logger:
    """
    custom function to log to a file 
    """
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    # if already there return it 
    if logger.handlers:
        return logger 
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s:%(lineno)d] - %(message)s"
    )
    file_handler = logging.FileHandler(application_log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

logger = get_logger("DemandPulse")