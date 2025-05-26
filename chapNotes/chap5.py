#                       Functions:

"""
Functions are blocks of code that perform a specific task. Functions give you the 
option to break your code into reusable, smaller pieces. A function takes in an 
input, processes it, and returns an output.
"""


#                       Scope:

"""
In Python, scope refers to the region in your code where you can access or reference 
a variable or function. Python has two types of scope—local and global. 

        Local:  A variable you declare within a function has local scope. You can only 
                access that variable within that function and not outside of it. 

        Global: A variable that you declare outside of a function or class has global scope. 
                You can access that variable from anywhere in your program. 
"""


#                       Arguments:

"""
Arguments are the values that Python passes to a function when you call them.

        Positional arguments:   are arguments passed to a function in a specific order, where 
                                the position of the argument determines its meaning. It's important 
                                to note that the order of the arguments matter when using positional arguments.

        Keyword arguments:      are a way to pass arguments to a function by explicitly specifying the parameter 
                                names along with their values. Unlike positional arguments, keyword arguments are 
                                not dependent on the order in which you pass them.
"""


#                       Passing a variable number of arguments:

"""
•   Use the *args function definition to pass a variable number of arguments to a function. 
    You use *args to send a non-keyworded variable length argument list to a function.

•   When you use **kwargs in a function definition, it permits the function to accept an 
    arbitrary number of keyword arguments. Python passes these keyword arguments as a 
    dictionary, where the keys are the argument names and the values are the argument values.
"""