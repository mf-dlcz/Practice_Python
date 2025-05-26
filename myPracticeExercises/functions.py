"""
FUNCTIONS ->

- Functions are blocks of code that perform a specific task.
- Functions break your code into reusable, smaller pieces and they make
your code easier to read & maintain. 
- If you need to perform a task multiple times, you can use
functions to avoid repeating the same code.
"""

#       Example #1: 
def my_function3():
    print("I miss you")

# my_function3()


#       #################################               MATH FUNCTIONS: PREDEFINED
"""
-   Functions that are predefined don't need the def
    keyword.
-   Math functions are pre-build functions you can use to
    perform mathematical tasks on numbers.
-   Use the min() and max() functions to find the lowest and
    highest values in a list of numbers.
"""

#       min() & max()
# numbers = [60, 20, 11, 4, 12, 10]
# min_val = min(numbers)
# max_val = max(numbers)

# print('This is the minimum values: ',min_val)
# print('This is the maximum value: ', max_val)


#       pow(x, y)
# Returns the power of x raised to the power of y.
# print(pow(3, 3))        # 27
# print(pow(5, 2))        # 25


#       abs()
# Returns the absolute value of x(the distance of x from 0)
# print(abs(-60))         # 60


#       ###############################         EXERCISES:

#           Task 1: Working with min() and max()
numbers = [15, 8, 42, 23, 16]
smallest = min(numbers)
largest = max(numbers)
# print(f"Smallest number: {smallest}")
# print(f"Largest number: {largest}")

#           Task 2: Working with pow()
base = 4
exponent = 3
result = pow(base, exponent)
# print(f"{base} raised to the power of {exponent} is: {result}")

#           Task 3: Working with abs()
negative_num = -42
positive_result = abs(negative_num)
# print(f"The absolute value of {negative_num} is: {positive_result}")

#           Task 4: Combining functions
numbers_2 = [-5, 10, -15, 20, -25]
absolute_numbers = []  # Create an empty list to store absolute values

# Convert each number in numbers_2 to its absolute value and store it in absolute_numbers
for numb in numbers_2:
    absolute_numbers.append(abs(numb))

largest_absolute = max(absolute_numbers)
# print(f"The largest absolute value is: {largest_absolute}")


#       ##################################                              UNDERSTANDING VARIABLE SCOPE:
"""
Local Scope ->  A variable declared within a function
has local scope.
- You can ONLY access that variable within that function and not
outside of it.
"""

#       local scope:
def my_function():
    """
    Assign a value of 5 to a local 
    variable 'x' and print its value.
    """
    x = 5
    print('Local', x)

# my_function() # output: Local 5

# try to access variable outside of function
# print(x) # output: error


#       global scope:
"""
- A variable that's declared outside of a function
  or class has global scope.
- You can access that variable anywhere in your program.
- You can modify global variables from within functions
  or classes.
"""

# Assign value of 5 to global variable 'x'
x = 5

def my_function1():
  """
  Define a local variable 'x' with a value of 5, 
  then print it.
  """
  x = 5

#   print('Local', x)

my_function1() # output: Local 5

# try to access variable outside of function
# print('Global', x) #output: Global 5


#       ###########################################                             GLOBAL KEYWORD:
"""
-   If you need to create a global variable, but are stuck in the local
    scope, you can use the global keyword.
"""

#       EXAMPLE:
def my_function2():
  global x              # AVOID
  x = 10

my_function2()

# print(x)


#       #############################################                               EXERCISE:

#       Task 1: Fix the scope error
def calculate_total():
    subtotal = 50
    tax = 0.1
    total = (subtotal * tax) + subtotal
    print("The total is:", total)  # This line should print the total

# calculate_total()


#   -------------------------------------------------------

#       Task 2: Create and modify a global variable
score = 0  # This is your global variable

def update_score():
    # Add 10 points to the score
    global score
    score += 10
    print(score)

def double_score():
    # Double the current score
    global score
    score *= 2
    print(score)

# print('initial score', score)
# update_score()
# print('after update', score)
# double_score()
# print('after double', score)

#   ------------------------------------------------------

#       Task 3: Understanding variable shadowing
name = "Alex"

def change_name():
    name = "Sam"  # This creates a local variable
    print("Inside function:", name)

# change_name()
# print("Outside function:", name)


#   ------------------------------------------------------

#       Task 4: Using the global keyword
counter = 0

def increment_counter():
    # Use the global keyword to modify the counter
    # Add 1 to counter
    global counter
    counter += 1

def display_counter():
    # Print the current value of the counter
    print('Counter: ',counter)

# increment_counter()
# display_counter()

# increment_counter()
# display_counter()

# increment_counter()
# display_counter()

# increment_counter()
# display_counter()


#       ######################################################                      NAMING VARIABLES:
"""
- Using the same variable names inside and outside a function,
will be interpreted as two separate variables.
"""


#       ######################################################                      WORKING WITH ARGUMENTS:
"""
- Arguments are the values that Python passes
to a function when you call it.
"""

#   EXAMPLE:
#           PARAMETER
def welcome(name):
    print('Hello, ' + name + '!')

#         ARGUMENT
# welcome('Maria')


#       ######################################################                      ARGUMENTS & PARAMETERS:
"""
*** The terms parameter & argument both refer to info
    being passed to a function.

Parameter - variable you list iniside the 
            parenthesis in a function definition.

Argument -  value that Python sends to the function
            for that parameter when you call the
            function.
"""


#           PARAMETER
def bye(name):
    print('bye for good, ' + name + '!')

#         ARGUMENT
# bye('Sean')


#       ###################################################                         DEFAULT PARAMETER VALUE:
"""
-   If you provide no argument, Python uses the default
    value, and if you provide an argument, it will
    overwrite the default value.
"""

#       EXERCISE:

def my_function4(food = "burgers"):
  print("My favorite food is " + food)

"""
Print a message about the programmer's favorite food.
"""
# call function4 with 'pizza' as an argument.
# my_function4("pizza")

# call function4 with 'tacos' as an argument.
# my_function4("tacos")

# call function4 with no argument.
# my_function4()


#       #####################################################                       USING THE RETURN STATEMENT:
"""
-   The return statement returns a value from a function.
"""
# Takes x, y as parameters and returns x+y
def add_numbers(x, y):
    return x + y

# because you have a result it must be stored in a variable
result = add_numbers(3,5)
# print(result)



#       ######################################################                      UNDERSTANDING NAMESPACES:
"""
-   A namespace maps names to objects they represent in a program.
-   A namespace is sort of like a dictionary where the variable names
    are the keys and the assigned object is the value.    
"""


"""             Built-in:
-   Includes the names of all of Python's built in objects like
    the data types and functions
"""



"""             Global:
-   Includes any name defined within the main program.
"""



"""             Local & Enclosing:
-   The local namespace is for variables that you defined inside
    functions.

-   The enclosing namespace is created when a function is defined
    inside another function.

-   Modules, classes and functions all create a local namespace.
"""


#       ###########################################################                         POSITIONAL ARGUMENTS:
"""
-   Positional arguments -  are arguments passed to a function in a
    specific order, where the position of the argument determines its
    meaning.
-   The order of arguments matter when using positional argument.
"""

def my_friend(friend_name, friend_city):
    """
    Take in two parameters, `friend_name` and `friend_city`,
    and print a message stating your friend with name `friend_name`
    lives in `friend_city`.
    """
    print(f"My friend {friend_name} lives in {friend_city} city.")

# my_friend('Maria','New York')



def my_sister(sisters_name, sisters_job):
    print(f'My sister, {sisters_name} is a/an {sisters_job}.')

# my_sister('Nail Tech', 'Fer')



#       ##########################################################                          Keyword Arguments:
"""
Keyword Arguments - Are a way to pass arguments to a function by
                    explicitly specifiying the parameter names
                    along with their values.
                -   Are not dependent on the order in which you pass
                    them.
"""

def my_friend2(friend2_name, friend2_city):
    print(f"My friend {friend2_name} lives in {friend2_city}.")

#       KEYWORD ARGUMENT:
# my_friend2(friend2_name = 'Becky', friend2_city = 'Brookly')


#       ###########################################################                         PASSING AN ARBITRARY # OF ARGUMENTS:
"""
-   In some cases, you might NOT know ahead of time how many arguments
    a function will need to accept.
-   It's permitted to pass an arbitrart number of arguments.

        *args(arbitrary arguments)
-   Use the *args variable to pass a variable number of arguments to a
    function.
-   Use *args to send a non-keyworded variable length argument list to a
    function.
"""


#       EXAMPLE:
def my_colors(*args):
    for color in args:
        print(color)

# my_colors('red', 'orange', 'blue', 'grey')


#       ##############################################################                      **kwargs (ARBITRARY KEYWORD ARGUMENTS):
"""
**kwargs -  is a special syntax in Python that gives you the option
            to pass an arbitrary number of arguments in a function.
        -   lets you pass keyword arguments to a function.
        -   when you use **kwargs in your function definition it allows the
            function to accept an arbitrary number of keyword arguments.
    *   -   Python passes these keyword arguments as a dictionary, where
    *       the keys are the arguments names and the values are the argument
    *       values.
"""

#           EXAMPLE:
def user_info(**kwargs): 

    """
    Take in keyword arguments as inputs and print 
    out the key-value pairs.
    """
    for key, value in kwargs.items(): 
	    print(f"{key}: {value}") 

# user_info(Name="Jane", Age=33, City="Paris", Language="French")


#       ################################################################                    PRACTICE EXERCISES:

#       Task 1: Working with required parameters
def create_profile(name, age, city):
    # Add parameters: name, age, city
    # Return them in a formatted string
    return f'Name: {name}, \nAge: {age}, \nCity: {city}'

# alice_profile = create_profile('Alice', 25, 'New York')
# print(alice_profile)

#   *****************************************************************

#       Task 2: Using default parameter values
def calculate_interest(principal, rate = 0.05, years = 1):
    # Add parameters: principal, rate=0.05, years=1
    # Calculate and return simple interest (principal * rate * years)
    return principal * rate * years

interest = calculate_interest(1000)
interest_2 = calculate_interest(1000, 0.07)
interest_3 = calculate_interest(1000, 0.07, 2)
# print(interest)
# print(interest_2)
# print(interest_3)

#   ******************************************************************

#       Task 3: Mixing positional and keyword arguments
def make_pizza():
    # Add parameters: size, crust_type, *toppings
    # Return a string listing the pizza details and all toppings
    pass



#       Task 4: Create a function that accepts any number of key-value pairs
def print_user_info():
    # Use **kwargs to accept any number of user details
    # Print each detail on a new line in "key: value" format
    pass