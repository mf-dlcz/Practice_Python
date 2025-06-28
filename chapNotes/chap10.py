'''
                Logging & Error Handling:

The logging module from Python's standard library offers a flexible system for recording events that occur as your code runs. 
Logged errors and exceptions can help you troubleshoot and debug your code. Analyzing event timing can help you monitor code 
performance and target areas for improvement. Logging can also be used to identify and fix security vulnerabilities and 
ensure compliance with policies.


                Logging Levels:

There are five standard logging levels: DEBUG, INFO, WARNING, ERROR, and CRITICAL. The levels are meant to differentiate among 
the severity of the issue that appears in a log. You can change which levels of events are reported in a log file by changing 
the configuration.


                Formatting Logs:

You can apply custom formatting to include as much information as you want to a logged event. You can add the date and time an 
event occurred. You can include the level of event and custom messages that might or might not include variable values.


                Errors & Exceptions:

Errors are an inevitable part of programming. Errors detected during runtime are called exceptions. Instead of runtime errors 
causing your program to crash, you can build logic into your programs that anticipates potential errors and provides a workaround. 


                Exception Handling:

The most basic form of exception handling uses try-except blocks. With these blocks, you can use a try statement to attempt to run 
some code, and then provide a different set of instructions to follow if that code fails.

You can stack as many except blocks under a try block as you wish. When you understand the errors that are likely to be raised, you 
can write code in your except blocks that respond to particular errors.

You can also use else and finally blocks with the try-except pattern. The instructions provided in an else block run after a try block
has been successful. The finally block runs after all of the others, regardless of which blocks ran before it.


                Logging Exceptions:

Just because you can predict and handle exceptions doesn't mean that you want them occurring in your running software. 
Logging exceptions provides developers with important information and context around these events. This can help debug 
and troubleshoot problems, and provide information for improving code.

'''