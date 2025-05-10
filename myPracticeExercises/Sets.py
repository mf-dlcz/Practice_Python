# Python Sets Review:
"""
Sets are unordered collections that contain ONLY unique
elements. Duplicates are automatically removed. They're
mutable which allows you to add or remove elements after creation.
Sets can ONLY contain immutable elements like numbers or strings.
This restricts the types of objects that can be stored in them.
SETS ARE PRIMARILY USED WHEN YOU NEED TO STORE ONLY UNIQUE 
ITEMS IN A DS. 
"""

#                   Exercise 1:

farm_animals = {"cow", "chicken", "sheep", "pig"}
# print(farm_animals)


# Converts List into a set
myListOfSupplies = set(["notebook", "pen", "paper", "binder", "binder", "notepad"])
# print(myListOfSupplies)           # type(myListOfSupplies)      -> Type Set


# Creates a new set
new_set = set ()

# Converts to set; Set will always print in order
convertSet = set([1, 5, 6, 4, 9, 9, 0, 1, 6, 4, 5, 9])
# print(convertSet)


#                   Exercise 2:
# Managing Unique Pet Breeds

# Step 1: Create a set of unique pet breeds available at the store.
# Breeds: "Golden Retriever", "Persian Cat", "Parrot", "Siamese Cat", "Golden Retriever"
pet_breeds = {"Golden Retriever", "Persian Cat", "Parrot", "Siamese Cat", "Golden Retriever"}


# Step 2: Print the set to verify that duplicate values are removed.
# print("Unique pet breeds:", pet_breeds)


# Step 3: Convert a list of new pet breeds into a set and print the result.
# New breeds: ["Cockatoo", "Maine Coon", "Golden Retriever"]
new_breeds = set(["Cockatoo", "Maine Coon", "Golden Retriever"])
print(f"Turned my list into a set:  \n{new_breeds}")


# Step 4: Create an empty set to store exotic breeds and print it.
exotic_breeds = set()
print(f"Empty set of exotic breeds: \n{exotic_breeds}")