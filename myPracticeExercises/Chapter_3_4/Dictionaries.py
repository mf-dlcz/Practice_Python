"""
Dictionaries are one of the most versatile and widely
used DS.
It's an ordered collection of key-value pairs.
Values can be of any type of DS, even including
other dic.
Keys hold immutable, values, such as strings, numbers
or tuples.
"""


#                   Exercise 1: Dictionaries

inventory = {
    "apples": 5,
    "bananas": 4,
    "coconuts": 2
}
# print (inventory)

inv_with_dups = {
    "apples": 5,
    "bananas": 4,
    "coconuts": 2,
    "apples": 1
}
# print (inv_with_dups)


#                  Exercise 2:

# Managing Pet Store Inventory

# Step 1: Create a dictionary to store the inventory of the pet store.
# Items: "dog_food": 10, "cat_toy": 5, "bird_seed": 8
# pet_store_inventory = {
#     "dog_food" : 10,
#     "cat_toy" : 5,
#     "bird_seed" : 8
# }

# Step 2: Print the dictionary to confirm its contents.
# print("\nPet store inventory:\t", pet_store_inventory,"\n")

# Step 3: Access and print the number of "cat_toy" items in stock.
# print(pet_store_inventory["cat_toy"])

# Step 4: Add a new item to the inventory: "hamster_wheel": 3.
# pet_store_inventory["hamster_wheel"] = 3

# Step 5: Print the updated dictionary to confirm the new item was added.
# print("\nUpdated pet store inventory:\t", pet_store_inventory, "\n")


#               Accessing Items:
"""
TASK 1:
"""
# inventory = {
#     "apples": 5,
#     "bananas": 4,
#     "coconuts": 2,
#     "dates": 10
# }

# The value of the key dates is stored in the variable num_dates 
# num_dates = inventory["dates"]
# The value of the key apples is stored in the variable num_apples
# num_apples = inventory["apples"]

# print (f"There are {num_dates} dates and {num_apples} apples in the inventory.")

"""
TASKT 2: Create a new variable for each of the remaining items 
in the dictionary and store their respective values.
"""
num_bananas = inventory["bananas"]
num_coconuts = inventory["coconuts"]
# print(f"\nThere are {num_bananas} bananas and {num_coconuts} coconuts in the inventory.")


#               Adding & updating items by key:
"""
To update values use the dic name and key.

"""
# Adds blueberries to the inventory dic
inventory["Blueberry"] = 20
inventory["Pomegranate"] = 40
inventory["Peaches"] = 15

# Update the value of an existing key
inventory["apples"] = 10
inventory["coconuts"] = 8

# Using assignment operators to update the value of a key
inventory["Peaches"] += 3           # Peaches is now 18
inventory["apples"] -= 2            # apples is now 8


#                  Exercise 2: Adding and Updating Pet Store Inventory

# Step 1: Create a dictionary to store the inventory of the pet store.
# Items: "dog_food": 10, "cat_toy": 5, "bird_seed": 8
pet_store_inventory = {
    "dog_food": 10,
    "cat_toy": 5,
    "bird_seed": 8
}

# Step 2: Add a new item to the inventory: "hamster_wheel": 3.
pet_store_inventory["hamster_wheel"] = 3

# Step 3: Update the stock of "cat_toy" to 10.
pet_store_inventory["cat_toy"] += 5

# Step 4: Increment the stock of "dog_food" by 5 and decrement "bird_seed" by 2.
pet_store_inventory["dog_food"] += 5
pet_store_inventory["bird_seed"] -= 2

# Step 5: Print the updated inventory to confirm changes.
# print("Updated pet store inventory:", pet_store_inventory)