# Exercise 1:
# Filter cold day temperatures below 60°F
# weeklyTemperature = [50, 60, 40, 70, 50, 80, 100]
# for temp in weeklyTemperature:
#     if temp <= 60:
#         print(temp)


# Exercise 2:
# You have two lists of vehicles
fourWheelVehicles = ["sedan", "truck", "SUV", "van", "coupes", "hatchback"]
twoWheelVehicles = ["motorcycle", "scooter", "moped", "bicycle"]
# a) Combine these into one master list using the + operator
allVehicles = fourWheelVehicles + twoWheelVehicles
# print(allVehicles)


# b) Swap the 6 and 7 vehicle in the list. Hint: Use a new variable to store one of the vehicles.
# tempPosition = allVehicles[5]
# allVehicles[5] = allVehicles[6]
# allVehicles[6] = tempPosition
# print(allVehicles)


#c) Check if 'moped' is in your final vehicle list
# user_input = input("What vehicle are you looking for? \n")

# if user_input == 'moped':
#     print("\nMoped is in the vehicle's list 🎉")
# else:
#     print(f"\n{user_input} is NOT in our list 🥺\n")


# Exercise 3:
word_frequency = {
    "the": 42, "and": 29, "to": 20, "of": 19,
    "a": 16, "in": 36, "is": 15, "it": 8,
    "you": 29, "that": 13
}
'''
Find the least popular words! Write a program to iterate 
through this dictionary and print only the words that 
have a frequency of less than 30.
'''
for key, value in word_frequency.items():
    if value < 30:
        print(key)


# Exercise 4:
colors = ["orange", "green", "pink"]
quantity = [16, 10, 27]
'''
Create your fruit inventory system - Use a for 
loop to use elements from these two lists to 
create a dictionary with elements from Fruits 
as the keys and elements from Quantity as the values. 
Remember, we can add new elements to a dictionary 
using dictionary[key] = value syntax.
'''








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