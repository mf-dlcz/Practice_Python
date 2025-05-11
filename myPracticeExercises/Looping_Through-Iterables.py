# Accessing elements through iteration:
"""
Lists, sets, dictionaries & tuples are all iterables,
meaning that you can traverse over each element
they contain one at a time. Bulk actions can be done
through iteration. 
"""


#               Exercise 1:
# names = ["Alejandro", "Ana", "carlos", "john", "Jane", "Paulo"]

#  placeholder
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
removed_duplicates = set(owner_names)
# print(removed_duplicates)
for uniqueName in removed_duplicates:
    firstLetterCapital = uniqueName.title()
    # print(firstLetterCapital)

# Step 4: Print a note after looping through the set, mentioning that duplicates were removed.
# print("\nDuplicates have been removed\n")


#               Using Range & Index:
names = ["Alejandro", "Ana", "carlos", "john", "Jane", "Paulo"]

for i in range(len(names)):
    print (f"{names[i]} is at position {i}")
