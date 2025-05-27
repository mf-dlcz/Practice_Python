import json

'''                     CLASSES & OBJECTS:

-   An attributes describe something about a class or object.
-   Methods define what a class or object can do.
-   Object method and attributes are specific to a particular instance of a class.
-   Class methods and attributes are shared by all instances of a class.

'''



#               CLASSES:
'''
-   A class is like a blueprint for creating new objects.
-   You can define, at the class level, what data the
    new object should carry and the functions it can perform.
'''



#               OBJECTS:
'''
-   An object is an instance of a class.
-   It is a collection of data that describes the object (attributes)
    and define what it can do(methods).
'''



#               Attribues:
'''
-   Attributes describe an object's state.
-   This can be something descriptive like color or size.
-   Or, it could reflect of state of being, like 'on' or 'off'
'''



#               METHODS:
'''
-   Methods describe what an object can do.
-   These are the functions you can build into an object.
'''



#       ############################################################################                EXPLORING OBJECTS & NOTATION:
'''
    .   What are objects?
                Almost everything is an object in Python. An object is a collection of data
                (attributes) and the functions(methods) that operate on that data. 
'''

'''
#*  To access the attributes and methods for a given object use dot notation.
#*  EXAMPLE:
#*          object_name.method_or_attribute_name
'''


#       inspecting objects:
'''
-   use the dir() function to view the available attributes and methods for an object
'''


my_list = {10, 11, 4, 20}

for attribute_or_method in dir(my_list):
    # returns a list of attributes or methods available to the object my_list
    print(attribute_or_method)


#       #########################################################################               CREATING CLASSES & OBJECTS:
'''
#*                            Reasons to use classes and objects:

1.  Better Organization:
                        . Use classes to organize your code into logical and reusable blocks.
                        . You can establish relationships among objects and represent the behaviors
                        and properties of the specific objects that you want to model in your code.
2.  Code Reusability:
                        . 
'''