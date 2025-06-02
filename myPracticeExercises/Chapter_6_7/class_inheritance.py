'''
Inheritance:
- A parent class is also called a base class, or superclass
- A child class is also called a derived class or subclass
'''

#       EXAMPLE:
'''
            (inheritance from Employee class)
class Engineer(Employee):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.posts = []
'''


#       REFERENCING THE PARENT CLASS:
'''
- One way to reference the parent class by name within the child's __init__ function.


class Engineer(Employee):
    def __init__ (self, name, email, hire_date):
        #* Referencing the parent class by name
        Employee.__init__(self, name, email, hire_date)
'''


#       The super() function:

'''
- The super() function allows a child class to access methods and attributes,
including the __init__ function, from the parent class without referencing the
parent class by name.
- This helps keep your code more flexible and maintainable than if you used a
direct reference.
# * You don't pass a self reference into the super() function.
'''


#       EXAMPLE:
'''
class Engineer(Employee):
    def __init__(self, name, email, hire_date):
    #* Referencing the parent class using super()
        super().__init__(name, email, hire_date)
'''