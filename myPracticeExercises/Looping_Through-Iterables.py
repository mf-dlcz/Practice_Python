# Accessing elements through iteration:
"""
Lists, sets, dictionaries & tuples are all iterables,
meaning that you can traverse over each element
they contain one at a time. Bulk actions can be done
through iteration. 
"""


#               Exercise 1:
# names = ["Alejandro", "Ana", "carlos", "john", "Jane", "Paulo"]

# name =  placeholder 
# for name in names:
#     name = name.title()
#     print (f"Hello, {name}!")


#              Exercise 2: Iterating Through Pet Owner Names

# Step 1: Create a list of pet owner names with one duplicate.
# Names: "alex", "beatriz", "carla", "derek", "alex"
owner_names = [ "alex", "beatriz", "carla", "derek", "alex" ]

# Step 2: Loop through the list to print a personalized thank-you message for each owner.
# Example output: "Thank you, Alex, for taking care of your pet!"
# for name in owner_names:
#     message = "Thank you, {}, for taking care of your pet!".format(name).title()
#     print(message)

# Step 3: Convert the list of owner names to a set to remove duplicates, and loop through it.
# removed_duplicates = set(owner_names)
# print(removed_duplicates)
# for uniqueName in removed_duplicates:
#     firstLetterCapital = uniqueName.title()
    # print(firstLetterCapital)

# Step 4: Print a note after looping through the set, mentioning that duplicates were removed.
# print("\nDuplicates have been removed\n")


#               Using Range & Index:
# names = ["Alejandro", "Ana", "carlos", "john", "Jane", "Paulo"]

# for i in range(len(names)):
    # print (f"\n{names[i]} is at position {i}\n")


#             Exercise 2: Numbering Pet Names

# Step 1: Create a list of pet names.
# Pet names: "Buddy", "Max", "Bella", "Charlie", "Luna"
pet_names = ["Buddy", "Max", "Bella", "Charlie", "Luna"]

# Step 2: Use a for loop with range() and len() to iterate through the list by index.
# Print a numbered list of pet names starting with 1.
# Example output: "1. Buddy"
# for pet in range(len(pet_names)):
    # print(f"{pet}.  {pet_names[pet]}")


#             enumerate()   -> Does the same thing as the code above

"""     Syntax for using enumerate()
  index                  (iterable DS)
for i, name in enumerate(names):
       item
"""
# for i, name in enumerate(pet_names):
    # print(f"{i}: {name.title()}")


#               Exercise 3: Enumerating Pet Names

# Step 1: Create a list of pet names.
# Pet names: "Buddy", "Max", "Bella", "Charlie", "Luna"
pet_names = ["Buddy", "Max", "Bella", "Charlie", "Luna"]

# Step 2: Use the enumerate() function to loop through the list.
# Print a numbered list of pet names starting with 0 for the index.
# Example output: "0: Buddy"
# for i, names in enumerate(pet_names):
#     print(f"{i}: {names}")

# Step 3: Adjust the numbering manually so it starts from 1 instead of 0.
# Example output: "1: Buddy"
for i, names in enumerate(pet_names):
    index = i + 1
    print(f"{index}: {names}")

