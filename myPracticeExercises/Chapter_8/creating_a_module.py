#               CREATING A MODULE FILE:

'''
Modules:    Contain data, classes and functions that are used in Python scripts.
'''

#       DOCUMENTING YOUR MODULE:
# Add a docstring to the beginning of the module explaining in a few lines its purpose.

#       EXAMPLE:
'''
This module contains classes for tracking 
product and sales data.
'''

##################################################################          CREATING AN ITERATOR:
'''
Iterator:   Object that you can use to traverse through all the values
            in an iterable.
            
Methods:
            __iter__()
            __next__()
'''

##################################################################          __iter__() METHOD:
'''
        EXAMPLE:

def __iter__(self):
    self.index = 0
    return self
'''

#################################################################           __next__() METHOD:
'''
__next__():     Will move you through each item on the list.
'''