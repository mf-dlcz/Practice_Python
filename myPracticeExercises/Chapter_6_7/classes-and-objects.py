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



#               Attributes:
'''
-   Attributes describe an object's state.
-   This can be something descriptive like color or size.
-   Or, it could reflect of state of being, like 'on' or 'off'
-   INSTANCE ATTRIBUTES BELONG TO A SPECIFIC OBJECT INSTEAD OF THE
    WHOLE CLASS OF OBJECTS.
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


# my_list = {10, 11, 4, 20}

# for attribute_or_method in dir(my_list):
#     # returns a list of attributes or methods available to the object my_list
#     print(attribute_or_method)


#       #########################################################################               CREATING CLASSES & OBJECTS:
'''
#*                            Reasons to use classes and objects:

1.  Better Organization:
                        . Use classes to organize your code into logical and reusable blocks.
                        . You can establish relationships among objects and represent the behaviors
                        and properties of the specific objects that you want to model in your code.

2.  Code Reusability:
                        . After defining a class you can create objects from the class without having
                        to rewrite any of the universal characteristics or tools that define the class.

3.  Easier Code Maintenance:
                        . Classes provide a way to break down complex systems into smaller, more manageable
                        modular units.
                        . You can target your fixes to the affected classes without affecting the broader
                        system you've created.
'''

#                   ACCESSING OBJECT ATTRIBUTES:
'''
class Employee:
    status = 'active'


#* instantiating an object
new_employee = Employee()


#* inspecting object attributes:
for i in dir(new_employee):
    print(i)


#*  accessing object attributes
new_employee.status                 # active


#*  update object attribute
new_employee.status = 'retired'

'''


#           EXERCISE #1: Creating classes and objects
class Employee:
    status = "active"
    hire_date = "01/01/2020"


# Use the Employee class to create a new employee object.
employee_maria = Employee()
e1 = Employee()
# print (e1.hire_date)

# Change that employee's status to onboarding.
# Change the hire date to 09/01/2023.
employee_maria.status = 'onboarding'
employee_maria.hire_date = '09/01/2023'
# print(employee_maria.status)
# print(employee_maria.hire_date)



#           CLASS DOG: LABELED
'''
#? This line defines a new class named 'Dog'.
#? Classes are blueprints for creating objects (instances).
class Dog:
    #? This is the constructor method, special for initializing new objects.
    #? It's called automatically when a new 'Dog' object is created.
    #? 'self' refers to the instance of the class being created.
    #? 'name' and 'breed' are parameters that will be passed when creating a Dog.
    def __init__(self, name, breed):
        #? These lines are attributes of the 'Dog' object.
        #? 'self.name' assigns the 'name' parameter to the 'name' attribute of the object.
        #? 'self.breed' assigns the 'breed' parameter to the 'breed' attribute of the object.
        self.name = name
        self.breed = breed
        #? This is another attribute, initialized with a default value.
        self.tricks = []

    #? This is a method (a function defined inside a class) that belongs to 'Dog' objects.
    #? 'self' is always the first parameter and refers to the object calling the method.
    #? This method allows a dog to learn a new trick.
    def learn_trick(self, trick):
        #? This line adds the 'trick' to the 'tricks' list of the specific dog object.
        self.tricks.append(trick)
        #? This line prints a message confirming the trick was learned.
        print(f"{self.name} just learned {trick}!")

    #? Another method to make the dog bark.
    def bark(self):
        #? This line prints a barking sound, using the dog's name.
        print(f"{self.name} says Woof!")

# --- Creating Objects (Instances) from the Class ---

#? This line creates an object (an instance) of the 'Dog' class.
#? 'Dog("Buddy", "Golden Retriever")' calls the __init__ method.
#? "Buddy" is passed as 'name', and "Golden Retriever" as 'breed'.
#? The new Dog object is assigned to the variable 'my_dog'.
my_dog = Dog("Buddy", "Golden Retriever")

#? This line creates another 'Dog' object, named 'your_dog'.
your_dog = Dog("Lucy", "Labrador")

#* --- Accessing Attributes and Calling Methods ---

#? This line accesses the 'name' attribute of the 'my_dog' object and prints it.
print(f"My dog's name is {my_dog.name}.")

#? This line accesses the 'breed' attribute of the 'your_dog' object and prints it.
print(f"Your dog's breed is {your_dog.breed}.")

#? This line calls the 'bark' method on the 'my_dog' object.
my_dog.bark()

#? This line calls the 'learn_trick' method on the 'my_dog' object, passing "fetch" as the trick.
my_dog.learn_trick("fetch")

#? This line calls the 'learn_trick' method on the 'my_dog' object again.
my_dog.learn_trick("roll over")

#? This line prints the list of tricks for 'my_dog'.
print(f"{my_dog.name}'s tricks: {my_dog.tricks}")

#? This line calls the 'bark' method on the 'your_dog' object.
your_dog.bark()

#? This line tries to print tricks for 'your_dog' (which hasn't learned any yet).
print(f"{your_dog.name}'s tricks: {your_dog.tricks}")
'''


#           ###################################################################                                         * NOTES:

#             DEFINING INSTANCE ATTRIBUTES:
'''
-   The constructor is created with one of the special dunder methods (__init__).
-   The __init__ function builds your object.
-   It's called automatically when an object of a class is created and it assigns
    the starting attributes and methods that make up your object.
-   The __init__ function takes an argument, named self, that refers to the
    instance of the object being created.
-   The self argument can be used to assign attribute values to an object on
    creation.
-   When a class is instantiated, the __init__ function runs and assigns the values
    passed in as arguments to the attributes named in the class definition.
-   Your class can include a mix of class and instance attributes.
'''



#           Challenge: Defining a new class
class BankAccount:
    number_of_accounts = 0

    def __init__(self, balance):
        account_number = BankAccount.number_of_accounts + 1
        self.account_number = str(account_number)
        BankAccount.number_of_accounts += 1
        self.balance = balance
    
    def deposit(self, deposit_amount):
        self.balance += deposit_amount

    def withdraw(self, withdraw_amount):
        if self.balance < withdraw_amount:
            print('Insufficient funds.')
        else:
            self.balance -= withdraw_amount
        
    def account_balance(self):
        return f'Your current balance is ${self.balance}'


# Testing my code

# create an instance of an object
marias_bank_account = BankAccount(0)

marias_bank_account.deposit(500)
print(f'I deposited ${marias_bank_account.balance}')

marias_bank_account.withdraw(200)
withdrawal_amount = 200
print(f'I withdrew ${withdrawal_amount} from my account. My current balance is ${marias_bank_account.balance}')


#       ###########################################################             