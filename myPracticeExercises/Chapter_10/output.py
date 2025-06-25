#import logging

# The only messages that were logged are WARNING,ERROR & CRITICAL
# Only the messages of warning level and higher are logged
'''
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
'''


#                   EXERCISE: Logging Practice
'''
import logging

# CRITICAL:root:This is a critical message
logging.basicConfig(level = logging.CRITICAL)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
'''

############################                    EXERCISE:

import logging

logging.basicConfig(level=logging.DEBUG)

def add_numbers(x, y):
    """Adds two numbers and returns the sum"""
    if type(x) != type(y):
        logging.warning("Args may not be compatible")
    
    if type(x)==str and type(y)==str:
        logging.error("Result is concatenated string")
    
    if (type(x)!=type(y)) and (type(x) in (bool,str) or type(y) in (bool, str)):
        logging.critical("Result '' cannot be processed")
        return ""
        
    logging.debug("x = {}, y = {}".format(x,y))
    logging.info("Function returns {}".format(x+y))
    return x+y
    
def main():
    add_numbers(2, 3)
    
if __name__ == "__main__":
    main()