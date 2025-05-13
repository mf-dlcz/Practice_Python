#           Additional Exercises: Looping through iterables

scienceStudents = ["kenneth", "john", "Zyra", "zoe", "Tesa", "maribel", "celest", "sol", "john", "Tesa"]

#       Exercise 1:

# Remove duplicates by turning the list into a set
# Duplicate names were John & Tesa
# uniqueList = set(scienceStudents)
# print(uniqueList)

# Loop through each name and display a message
# for name in uniqueList:
#     name = name.title()
#     print(f"{name}, been added to the list!")


# Check how many items are in the list
# for name in range(len(scienceStudents)):
#     name = name + 1
#     print(f"{name}: {scienceStudents[name]}")


#       Exercise 2: Using enumerate
# for i, student in enumerate(scienceStudents):
#     print(f"{student}")

for student in scienceStudents:
    newList = student.replace("kenneth", "Lisa").title()
    print(newList)