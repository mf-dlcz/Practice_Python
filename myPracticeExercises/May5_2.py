# Task 1: Practicing Python Basics
# pi = 3.14
# radius = input("Enter a number to be the radius: \n")

# #convert string to number
# radius = int(radius)

# areaOfCircle = (pi * radius * radius)
# print(f"The are of the circle is {areaOfCircle}")


# ################################################################

# Convert Farenheit into Celsius
# farenheit = input("Enter temperature in Farenheit: \n")

# Formula to convert:
# farenheit = int(farenheit)

# celsius = (farenheit - 32) * 5/9
# print(f"{farenheit} farenheit into Celsius is : {celsius}")


# ################################################################
# x = input("Enter a number for x: \n")
# y = input("Enter a number for y: \n")

# temp = x
# x = y
# y = temp

# print(f"x = {x}             {y} = y")


# Task 2: Practicing with Conditionals
# if 's' in "String":
#     print("Found!")
# if 's' not in "String":
#     print("sorry!")


statement = "The Cat in the Hat is a children's book"
letter = input("Enter which letter you are searching for: ")

# if statement, using a membership operator “in”, and using two string methods in a single line
if letter in statement.strip().lower():
    print(f"Found the letter {letter}!")