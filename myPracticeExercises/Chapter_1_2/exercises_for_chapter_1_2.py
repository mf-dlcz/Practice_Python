#                                           Task 1: Practicing Python Basics (AREA)
# pi = 3.14
# radius = 30
# radius = float(input("Enter a number to be the radius: \n"))

# #convert string to number
# radius = int(radius)

# areaOfCircle = (pi * radius * radius)
# print(f"The area of the circle with user input radius is {areaOfCircle}")


# #############################################
#                                             Task 1.2 Temperature
# Convert Farenheit into Celsius
# farenheit = input("Enter temperature in Farenheit: \n")

# Formula to convert:
# farenheit = float(farenheit)

# celsius = (farenheit - 32) * 5/9
# print(f"{farenheit} farenheit into Celsius is : {celsius}")


# ##############################################
#                                             Task 1.3 Swap
# x = input("Enter a number for x: \n")
# y = input("Enter a number for y: \n")

# temp = x
# x = y
# y = temp

# print(f"x = {x}             {y} = y")


# ############################################
#                                            Task 2: Practicing with Conditionals
# if 's' in "String":
#     print("Found!")
# if 's' not in "String":
#     print("sorry!")


statement = "The Cat in the Hat is a children's book"
# letter = input("Enter which letter you are searching for: ")

# if statement, using a membership operator “in”, and using two string methods in a single line
# if letter in statement.strip().lower():
#     print(f"Found the letter {letter}!")
# if letter not in statement.strip().lower():
#     print(f"Sorry! '{letter}' was not found! ")


# #################################################
#                                       Task 2.2 Even & Odd                       
"""
In a new file, ask the user to input any number. 
Use conditions to determine if the user-entered 
number is even or odd, and print if the number is 
even or if the number is odd.
"""

# number = int(input("Enter a number: \n"))

# if number % 2 == 0:
#     print(f"{number} is even.")
# else:
#     print(f"{number} is odd.")


# ##################################################
#                                        Task 3.3 Auditorium Seating
"""
In a new file, write a program to allocate an auditorium 
seating row for the user based on their favorite number by 
doing the following. Get a user-inputted value between 1 and 
50 and save it in the variable fav_number. Based on this value, 
using the following seating map, print the row that the user 
will sit in the auditorium. If the user enters anything that is 
above 100 or below 0, the program should tell them that it is an invalid input.

Fav_number ---- Row

1 - 10 ----- E

11 - 20 ----- D

21 – 30 ----- C

31 – 40 ------ B

41 - 50 ------ A
"""

fav_num = int(input("Enter your favorite number between 1 and 50: \n"))

if 1 <= fav_num and fav_num <= 10:
    print("\nYou're in row E")
elif 11 <= fav_num and fav_num <= 20:
    print("\nYou're in row D")
elif 21 <= fav_num and fav_num <= 30:
    print("\nYou're in row C")
elif 31 <= fav_num and fav_num <= 40:
    print("\nYou're in row B")
elif 41 <= fav_num and fav_num <= 50:
    print("\nYou're in row A")
elif fav_num >= 51 or fav_num <= 0:
    print("\n------- INVALID INPUT -------\n")