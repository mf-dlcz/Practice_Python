"""
FUNCTIONS ->

- Functions are blocks of code that perform a specific task.
- Functions break your code into reusable, smaller pieces and they make
your code easier to read & maintain. 
- If you need to perform a task multiple times, you can use
functions to avoid repeating the same code.
"""

#       Example #1: 
def my_function():
    print("I miss you")

# my_function()


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


#       ##################################          UNDERSTANDING VARIABLE SCOPE:
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

"""