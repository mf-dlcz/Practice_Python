#               WRITING LOG FILES:

'''
Using filename keyword in the basicConfig function to write a log file.

logging.basicConfig(filename = 'example.log', level = logging.DEBUG)
'''

'''
import logging

logging.basicConfig(filename="example.log", level=logging.DEBUG)

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

#*                                              NOTES:

-   The default mode for writing to a log file is append.
-   You can change this in the basicConfig function by specifying the filemode.


'''