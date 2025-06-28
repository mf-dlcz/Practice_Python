# Using the logging Module

import logging

'''
Use the logging module to write log messages to a file named ex_ample.log. 
Each log message should include the time it was logged, the level name, 
and a message. All logs at level INFO and higher should be logged.
'''

logging.basicConfig(filename = "/Users/mariadelacruz/Documents/AWS Coding Exercises/src/myPracticeExercises/Chapter_10/ex_ample.log",
                        format = "%(asctime)s %(levelname)s %(message)s",
                        level = logging.INFO)

def process_data():
    logging.info("Inside my fuction")
    user_input = input("\nEnter a series of numbers, each separated by comma: \n")

    if " " not in user_input:
        logging.error("User did not enter values separated by a comma")
        logging.info("Function will return, please try again.")
        return 'Please try again!'
    
    str_list = user_input.split(",")
    logging.info("User input is %i items long", len(str_list))
    numb_list = [int(x) for x in str_list]
    logging.info("Function returns %s", numb_list)
    return (numb_list)

print(process_data())