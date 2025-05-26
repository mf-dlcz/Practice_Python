"""
    CHECKING NUMBERS:
"""

"""                     TASKS:
-   Create two number-checker functions, isEven and isOdd. 
The isEven function should return True if the argument passed 
into it is an even number, and False if the argument is an odd 
number. The isOdd function should return True if the argument 
passed into it is odd, and False if the argument is even. Test 
each function by using a loop to evaluate numbers zero through nine.
"""

def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False


def isOdd(number):
    if number % 2 != 0:
        return True
    else:
        return False


print('EVEN: ' ,isEven(23))
print('ODD: ', isOdd(23))