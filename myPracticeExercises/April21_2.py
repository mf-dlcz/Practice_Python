#If you mix a number with a float. The result will be always be a float.
# Exercise 1:
#print(30 + 4.8)   #Output: 34.8


# Exercise 2:
# Define two variables: one integer and one float
#a = 4  # Replace with any integer value
#b = 10.11  # Replace with any float value
# Perform the operations and print the results
# Add your predictions in the comments before running the code
# Example:
# Addition
# Predict: float
#print(a + b) #Output: 14.11
# Now complete subtraction, multiplication, and division below!
# Multiplication
#print(a * b) #Output: 40.44
# Subtraction
#print(a - b) #Output: -6.109
# division
#print(a / b) #Output: 0.39


# Exercise 3:
#m = 33
#d = 11.5
#print( type(m) ) #Output: int
#print( type(d) ) #Output: float


# Exercise 4:
#m = "Maria"
#b = False
#print( type(m) ) #Output: str
#print( type(b) ) #Output: boolean / bool


# Exercise 5:
#Casting
#x = float(3)
#y = str(2)
#z = int(2.8)
#print(x) #Output 3.0
#print(y) #Output "2"
#print(z) #Output 2


# Exercise 6:
#Indexing
#name = "María"
#favoriteCity = "New York"
#print(name[2]) #Output: "r"
#print(name[0]) #Output: "M"
#print(name[3]) #Output: "í"
  #Slicing
#print(favoriteCity[0:3]) #Output: "New"
#print(favoriteCity[4:8]) #Output: "York"
# Leave the begining empty to slice from begining to index 3
#print(favoriteCity[:3]) #Output: "New"
# Leave the end empty to slice from desired index to the end
#print(favoriteCity[4:]) #Output: "York"


# Exercise 7:
# Modify this code to complete the tasks below
#my_string = "Python is awesome!"
# Example of slicing: Extract "Python" from the string
#example_slice = my_string[:6]
#print(example_slice)
# Task #1 -> Extract the word "awesome" using slicing
#awesome_slice = my_string[10:17]
#print(awesome_slice)
# Task #2 -> Extract the phrase "Python is"
#pythonIs_slice = my_string[0:9]
#print(pythonIs_slice)
# Task #3 -> Extract everything from the word "is" to the end of the string
#isEverything_slice = my_string[7:]
#print(isEverything_slice)
# Task #4 -> Reverse the entire string using slicing
#reverseString_slice = my_string[::-1]
#print(reverseString_slice)


# Exercise 8:
# .upper() Capitalizes
#listOfHobbies = "Hiking, Djing, dancing, painting, photographing, exercising, sleeping, reading, studying"
#print(listOfHobbies.upper())
# .strip() Removes white space from the BEGINNING & END
#removeWhiteSpace = "            Why?        "
#print(removeWhiteSpace.strip())
# .replace() Replaces a string with another string & returns a new string
#bookName = "How to Make Friends & Influence People"
#print(bookName.replace("&", "and"))


# Exercise 9:
#user_name = " Jjonathan Smith"
#removedWhiteSpace = user_name.strip()
#correct_userName = removedWhiteSpace.replace("Jjonathan", "Jonathan")
#   Result
#print(correct_userName)

      # 9.2
#messageInA_Bottle = "          Hiii, I miss you so much!!          "
#removedExtraI = messageInA_Bottle.strip()
#intendedMessage = removedExtraI.replace("Hiii", "Hey babe")
#   Result
#print(intendedMessage)


# Exercise 10:
#Concatenating Strings: Combines two or more strings into a single string
#age = 59
#profile = "Hi, my name is Megan, and I am {} years old."
#print(profile.format(age))

#first_name = "Clara"
#last_name = "Smith"
#fav_Artist = "Helmut Ebritsch"
#message = "My name is {} {}. I'm {} years old, and currently my favorite artist is {}"
#print(message.format(first_name, last_name, age, fav_Artist))


# Exercise 11:
# Escape character \
#myFav_affirmation = "Briana Wiest \"You're not looking for anyone else to give you the answers, you're looking for what you already know to be reflected back to you. You already know what's true\""
#print(myFav_affirmation)
# New line
#fav_music = "\nElectronic, \nPost-Punk, \nLofi, \nInstrumental Metal, \nTechno, \nDub"
#print(fav_music)
# Tab
#paragraph = "\tThis has been an incredible, ride. I've meet amazing people along the way that have taught me things about me. \nEveryday, I am grateful for the experiences that shape my reality. I'm grateful I met you!"
#print(paragraph)
#Example:
#print("Name:\tTerry\nAge:\t28\nJob:\tCloud application developer")


# Exercise 12:
# Task 1: Use string concatenation to introduce yourself
#name = "Maria"
#introduction = "Hi, this is " + name + ". It's a pleasure to be here."
#print(introduction)  # Expected output: Hello, my name is [Your Name].
# Task 2: Use the .format() method to add more details
# Replace placeholders with your hobby, age, and city
#details = "I enjoy {}. I am {} years old and I live in {}.".format("working out", "99", "Venus") # Complete this line
#print(details)  # Expected output: I enjoy [Your Hobby]. I am [Your Age] years old and I live in [Your City].
# Task 3: Use escape characters to display a formatted block
# Use \n for new lines and \t for tabs
#formatted_info = "\nName:\tMaria\nHobby:\tWorking Out\nAge:\t99"
#print(formatted_info)  # Expected output:
# Name:     [Your Name]
# Hobby:    [Your Hobby]
# Age:      [Your Age]


# Exercise 13:
# Conditions & Loops
# Using conditionals with proper indentation

'''    Syntax: 
if <condition>:         Evaluates to either True or False
    <perform an action>
print(Outside the if statement)
'''

#m = 29
#if m < 17:  
#    print("m is less than 17")
#elif m == 20:
#    print("m is equal to 20")
#else:
#    print("m is less than 30")
#Outside the if statement
#print("Condition check complete!")

        # 13.2
#t = 16
#k = 4
#a = 8
#if k < t and k < a:
#    print(f"{t} is greater than {k}. \n{k} is less than {a}.")
#print("\tThis code is outside the if statement.")

#if k != a or t > a:
#    print(f"\n{k} is NOT equal to {a}. \n{t} is greater than {a}.")


# Exercise 14:
# if elif

#f = 96
#m = 39
#if f > m:
#    print(f"{f} is greater than, {m}")
#elif m > f:
#    print(f"{m} is greater than {f}")
#print("The condition is over")

      # 14.2
#g = 57
#j = 86
#p = 86

#if p < g:
#    print(f"{p} is less than {g}")
#elif j == p:
#    print(f"{j} is equal to {p}")
#else:
#    print(f"{p} is greater than {j}, and {g}")


# Exercise 15:
# Step 1: Define the age variable
#age = 12  # Assign a numeric value to represent someone's age
# Step 2: Use if-elif-else to determine the life stage
# Add your conditions below
#if age < 13:
#    print("You're a child")
#elif age >= 13 and age <= 19:
#    print("You're a teenager")
#elif age == 20 or age > 20 and age <= 100:
#    print("You're an adult")
#else:
#    print("You're an alien")


# Exercise 16:
# for loop with range()
# for loop prints #'s from 10 - 20
#for number in range(10, 20):
#    print(number)
#    print("This line runs inside the loop") #because of the indentation:
#print("This line does NOT run inside the loop")

      # 16.2     
# loops through each character
#motivational_message = "opportunities DON'T happen, you create them."
#for character in motivational_message:
#    print(character)

'''     for loop syntax:
for <variable> in <iterable>:
    <body>
'''


# Example 17:
vocabulary_word = "Volatile"
print(f"The word {vocabulary_word} is spelled: ")
for character in vocabulary_word:
    print(character)
