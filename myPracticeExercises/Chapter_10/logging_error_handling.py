#   Logging:

'''
                            What is logging?
-   Logging refers to the practice of recording events and data about an application's behavior as the application code runs.
-   They are meant to record events and information in a way that can be reviewed later.
-   You can create multiple logging objects to report about different parts of your code.


                            Importance of logging:
Debugging and Troubleshooting:  Logging can help you flag and investigate bugs in your code. Logs provide historical context for 
                                events, so developers can study log files to locate and resolve bugs. They also use tools like 
                                log analyzers to automate the processing of log files.

Monitoring & Performance Analysis:  Logging provides monitoring and performance analysis by capturing data about an application's 
                                    behavior over time. Developers can include logs that measure efficiency of running code. They 
                                    can use those logs to detect weak performance and resolve inefficiencies.

Security & Compliance:  Logs can be used to identify and fix security vulnerabilities in application code, as well as ensure that 
                        security policies are being followed. Regular reviews of audit logs can help organizations identify and 
                        improve weaknesses in their systems.
'''


'''
                            Error Handling:

-   refers to the process of anticipating, detecting, responding to and recovering from errors that occur when an application runs.
-   When you anticipate where errors might occur, error handling provides a way to resolve or work around the problems without stopping 
    your program or losing data. Without proper error handling, software can fail in unpredictable ways, leading to data loss and 
    security vulnerabilities.
'''


'''
                            Logging Levels:

Level:          When It's Used:                                                                                     Least Severe:
Debug           Detailed information, typically of interest only when diagnosing problems.          

Info            Confirmation that things are working as expected.

Warning         An indication that something unexpected happened, or indicative of some 
                problem in the near future (for example, ‘disk space low’). The software 
                is still working as expected.

Error           Due to a more serious problem, the software has not been able to perform some function.

Critical        A serious error, indicating that the program itself may be unable to continue running.              Most Severe:

DOCUMENTATION:
https://docs.python.org/3/howto/logging.html#when-to-use-logging

'''

#* The default level is WARNING, which means that only events of this level and higher will be tracked, 
#* unless the logging package is configured to do otherwise.

