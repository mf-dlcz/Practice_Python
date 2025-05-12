# Exercise 1:
# Be a temperature filter! Find those warm days above 18°C
temperatures = [15, 20, 12, 24, 18, 21, 16, 19]
# for temp in temperatures:
#     if temp > 18:
#         # print(temp)


# Exercise 2:
# You have two lists of colors:
primary_colors = ['red', 'blue', 'yellow']
secondary_colors = ['purple', 'green', 'orange']
# a) Combine these into one master color list using the + operator
combinationOfColors = primary_colors + secondary_colors
#print(combinationOfColors)

# b) Swap the first two colors in the list. Hint: Use a new variable to store one of the colors.
# temp = combinationOfColors[0]
# combinationOfColors[0] = combinationOfColors[1]
# combinationOfColors[1] = temp
# print(combinationOfColors)

        # 2b)
# temp = combinationOfColors[2]
# combinationOfColors[2] = combinationOfColors[3]
# combinationOfColors[3] = temp
# print(combinationOfColors)

#c) Check if 'purple' is in your final color list
if "white" in combinationOfColors:
    print(f"Yes, purple is in {combinationOfColors}")
else:
    print(f"No, purple is not in {combinationOfColors}")


# Exercise 3:
word_frequency = {
    "the": 42, "and": 29, "to": 20, "of": 19,
    "a": 16, "in": 36, "is": 15, "it": 8,
    "you": 29, "that": 13
}
# Find those popular words! Write a program to iterate through this dictionary and print only the words that have a frequency of 20 or more.
# for key, value in word_frequency.items():
#     if value >= 20:
#         print(key)


# Exercise 4:
fruits = ['apples', 'bananas', 'oranges']
quantity = [10, 8, 20]
'''
Create your fruit inventory system - Use a for 
loop to use elements from these two lists to 
create a dictionary with elements from Fruits 
as the keys and elements from Quantity as the values. 
Remember, we can add new elements to a dictionary 
using dictionary[key] = value syntax.
'''
# Creates empty dictionary
# fruitQuantities = {}
# index, apples
# for i,fruit in enumerate(fruits):
#     fruitQuantities[fruit] = quantity[i]
# print(fruitQuantities)


# Exercise 5:
'''
Write a program to create a dictionary, 
scores = {} with 3 names (keys) and associated 
scores (values). Iterate through the dictionary and 
print the key-value pairs. Get user input for a name 
and check to see if that name exists in the scores 
dictionary. If it does, print the score of that user name. 
If not, print a message that user has not been found.
'''
# Dictionary with 3 names & their respective scores
scores = {
    'Kyle': 20,
    'Cara': 26,
    'Leslie': 24
}
# Input from user stored in name
# name = input('\nPlease, enter a name ')
# Looking for the name entered in my dictionary
# if name in scores:
    
#     score = scores[name]
#     print(f"{name}'s score: \t{score}")
# else:
#     print('The user has not been found')