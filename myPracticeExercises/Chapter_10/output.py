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