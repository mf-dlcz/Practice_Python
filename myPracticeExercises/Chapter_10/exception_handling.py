#               Exception Handling:

#                   EXAMPLE:

'''
def add_numbers(x, y):
    """Adds two numbers and returns the sum"""
    try: 
        return x + y
    except: 
        return (f"Cannot add {type(x)} and {type(y)}")

print(add_numbers(2, 3))
'''

#########################################################

#               EXAMPLE:

# The code below doesn't include an explanation of why things failed
# If your divisor is 0 there will be an error.
# If you entered anything other than a number you'll receive an error.

'''
def divide_numbers():
    
    try:
        dividend = int(input("Enter the integer to divide: "))
        divisor = int(input("Enter the integer to divide by: "))
        return (dividend/divisor)
    
    except Exception as e:
        print (type(e))
        print (e)
        
print(divide_numbers())
'''

######################################################

#               Example:

# The code below includes exception handling for 
# dividing by zero
# not entering an integer

def divide_numbers():
    while True:
        try:
            dividend = int(input("Enter the integer to divide: "))
            divisor = int(input("Enter the integer to divide by: "))
            return (dividend/divisor)
        except ValueError: 
            print ("Enter an integer.")
        except ZeroDivisionError:
            print ("Cannot divide by zero.")
        except Exception as e:
            print (type(e))
            print (e)

print(divide_numbers())

#               SAME CODE AS ABOVE WITH THE ELSE BLOCK:

#* an else block can also be included after the last exception handler
#* 

'''
def divide_numbers():
    try:
        dividend = int(input("Enter the integer to divide: "))
        divisor = int(input("Enter the integer to divide by: "))
        result = dividend/divisor
    except ValueError: 
        print ("Enter an integer.")
    except ZeroDivisionError:
        print ("Cannot divide by zero.")
    else: 
        return (result)

divide_numbers()
'''

##################################################

#               EXAMPLE:
'''
                THE FINALLY BLOCK:
It can be specified to run the last code block whether
or not an exception has been raised.
'''

'''
try:
    file = open("myfile.txt", "r")
    # Perform some operations on the file
except FileNotFoundError:
    print("The file could not be found.")
except IOError:
    print("An error occurred while reading the file.")
else:
    print("File contents:", file.read())
finally:
    if 'file' in locals():
        file.close()
        print("File closed.")
'''

################################################

#               EXAMPLE:

# It's possible to raise exceptions if certain conditions
# occur. The keyword raise is used to raise an exception.

'''
#?    The following code raises an excpetion if the user 
#?    enters a number less than 13


def create_profile(username, age):
    """Creates dictionary with user details
    and calls function to create homepage """
    try: 
        if age < 13:
            raise Exception("Account holders must be 13 or older.")
        user_dict = {"name": username, "age": age}
        print (user_dict)
        create_homepage(user_dict)
    except Exception as e:
        print (e)



?  The example below is similar to the example above. The difference is that ValueError 
?  specifies that an inappropriate value was entered.

def create_profile(username, age):
    """Creates dictionary with user details
    and calls function to create homepage """
    try: 
        if age < 13:
            raise ValueError("Account holders must be 13 or older.")
        user_dict = {"name": username, "age": age}
        print (user_dict)
        create_homepage(user_dict)
    except Exception as e:
        print(type(e))
        print (e)
'''