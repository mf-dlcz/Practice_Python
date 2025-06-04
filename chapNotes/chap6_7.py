'''
Classes, objects and notation:
'''

#           Class:
'''
A class is like a blueprint for creating new objects.
'''


#           Object:
'''
An object is an instance of a class. It is a collection of data that describes an 
object through its attributes and defines what it can do through its methods.
'''

#           Attribute:
'''
An attribute describes an objects state. This can be something descriptive like color 
or size, or it could reflect a state of being, like on or off.
'''


#           Method:
'''
Methods are functions assigned to an object; they describe what the object can do.
'''


#           dot notation:
'''
You can access the methods and attributes for a given object using dot notation where 
you provide the object name, a dot (.), and the name of the method or attribute.
'''


#           Creating classes & objects:
'''
Class definitions start with the keyword class and then the name of the class you are 
defining. Everything that belongs to the class definition should be indented four spaces 
under the first line. You can name class attributes, also called static attributes, that 
keep track of attributes that belong to an entire class not an individual instance. An 
object is an instance of a class.
'''


#           Creating unique objects:
'''
Because objects are often modeled to represent real-world entities, their classes typically 
include a constructor method that initiates an object with specific values on creation. 
The __init__() function runs automatically when an object is created and assigns attributes 
and methods to the instance. The __init__() function always takes a parameter, typically called 
self, that references the instance being created.
'''


#           associated objects:
'''
You should try to keep your code as modular as possible. One way to do that is keeping your 
objects focused on representing a single thing. To build full applications, your objects 
will likely interact with each other. You can create new objects from the methods that 
belong to other objects.
'''


#           class inheritance:
'''
You can create classes that inherit attributes and methods from other classes. In this 
situation, the original class is called a parent or base class. It can also be called a 
superclass. The class that inherits properties is called the child or derived class. 
It can also be called a subclass.

The super() function is a useful way to reference the parent class from within a child class.
'''


#           custom methods:
'''
You can override inherited methods to customize them for the child classes you create. You 
can also reference methods from a parent inside the definition of a child method.
'''