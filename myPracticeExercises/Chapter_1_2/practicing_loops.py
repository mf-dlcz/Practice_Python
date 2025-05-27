#                                   Task 3 - Practice with Loops
"""
Identify which loop would work best for this situation: 
You are learning how to play basketball and practicing 
free-throw shots. You make three unsuccessful attempts, 
and on the fourth attempt you make the shot. Once you 
have identified the loop, write a program that will 
print a statement every time your free throw attempt 
fails and when the attempt was successful.
"""
# Keeps my loop going from 1 - 4
# for free_throw in range(1, 5):
    # checks if my shot is less than 4... if it is returns missed shot
    # if free_throw < 4:
    #     print("You missed free throw!")
    # otherwise it's equal to 4 which is a successful free throw 
    # elif free_throw == 4:
    #     print("Yay! you successful had a free throw!")


#                                   Task 3.2 - Prints numbers
# for num in range(1, 11):
#     print(num)

# num = 11
# while (num > 0):
#     num = num - 1
#     print(num)


#                                   Task 3.3 - Cryptic Name
"""
You are creating a cryptic name generator, 
and the first step in this process is to 
interleave the user’s first name with a 
number after every character. Here are 
the steps to create this:
"""

# Ask user for their first name
user_name = input("Enter your name: \n")

# Create a cryptic_name variable with an empty string
cryptic_name = ""

"""
- Use a for loop to iterate through the user’s name
- In each iteration of the loop, ask the user to 
input a number. This number should be appended 
after the character of the user’s first name 
and appended into the new cryptic_variable name.
"""
#  ####################### One way to solve #########
# for letters in user_name:
#     number = input("Enter a number: \n")
#     cryptic_name = cryptic_name + letters + number

# print(cryptic_name)


#                       Second way to solve
for letter in range(len(user_name)):
    num = input("Enter a number: \n")
    cryptic_name = cryptic_name + user_name[letter] + num

print(cryptic_name)