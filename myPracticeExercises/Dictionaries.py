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
pet_store_inventory = {
    "dog_food" : 10,
    "cat_toy" : 5,
    "bird_seed" : 8
}

# Step 2: Print the dictionary to confirm its contents.
# print("\nPet store inventory:\t", pet_store_inventory,"\n")

# Step 3: Access and print the number of "cat_toy" items in stock.
# print(pet_store_inventory["cat_toy"])

# Step 4: Add a new item to the inventory: "hamster_wheel": 3.
pet_store_inventory["hamster_wheel"] = 3

# Step 5: Print the updated dictionary to confirm the new item was added.
print("\nUpdated pet store inventory:\t", pet_store_inventory, "\n")


#               Accessing Items:
