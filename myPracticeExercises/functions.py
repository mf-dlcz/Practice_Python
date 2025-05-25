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
print(result)



#       ######################################################                      UNDERSTANDING NAMESPACES: