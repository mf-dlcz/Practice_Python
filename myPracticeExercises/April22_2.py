# Use range() to loop & access the elements of an iterable using an index

'''             Example:
for <counter_variable> in range(len(iterable)):
    print(f"index is {counter_variable}")
    print(f"element at index {counter_variable} is {iterable[counter_variable]}")
'''


        #  Exercise 1:
# name = "María"
                # 5 letters     
# for i in range(len(name)):
                        # index     access the character at index
#    print(f"element at index {i} is {name[i]}")
'''             Output:
element at index 0 is M
element at index 1 is a
element at index 2 is r
'''

        # 1.2
# listOfNums = [4 , 16, 33, 39]
# for num in listOfNums:
#    print(num)


        # Exercise 2:
'''         Definition:
    while loops -> is a control flow  statement that enables you to
    runs code repeatedly WHILE a specified condition is True.
    This loop is best suited for iterating when the number of iterations
    is known.
'''

# Counts from 1 to 5
# count = 1
# while count <= 5:
#    print(count)
#    count = count + 1          #Increments count to begin the loop again

        # 2.2:
# play_again = 'y'
# while (play_again == 'y'):
#    play_again = input("Would you like to play again (y/n)? ")
# print("Thanks for playing! Goodbye.")


'''
    Break Statement -> is a control flow statement you use to IMMEDIATELY
    STOP running a for or while loop statement.
'''
#         # Exercise 3:
# favColor = "black"
# for i in favColor:
#     if i == 'l':
#         print("The letter " + i + " was found!")
#         break


'''     input() ->  allows you to pause your program and prompt
a user to enter text. Python then assigns it to a variable.
''' 

# user_name = input("What is your user name? \n")
# print(f"\nYou entered {user_name} as your user name")
# answer = input("Is that correct? (Y/N) ")

# for i in answer:
#     if answer == "y":
#         print("\nGreat! Thank you\n")
#         break
#     elif answer == "Yes":
#         print("\nGreat! Thanks\n")
#         break
#     elif answer == "YES":
#         print("\nGreat! Thanks\n")
#         break
#     elif answer == "Y":
#         print("\nGreat! Thanks\n")
#         break
#     else:
#         print("\nWRONG USERNAME (；一_一)\n")


