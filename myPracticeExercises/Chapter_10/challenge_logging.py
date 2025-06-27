# Using the logging Module

import logging

'''
Use the logging module to write log messages to a file named ex_ample.log. 
Each log message should include the time it was logged, the level name, 
and a message. All logs at level INFO and higher should be logged.
'''

logging.basicConfig(filename = "/Users/mariadelacruz/Documents/AWS Coding Exercises/src/myPracticeExercises/Chapter_10/ex_ample.log",
                        format = "%(asctime)s %(levelname)s %(message)s",
                        level = logging.DEBUG)

def process_data():
    user_input = []
    user_input = input("Enter a list of numbers separated by commas: \n")
    return user_input

print(process_data())