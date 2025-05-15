"""         List Methods
Lists have built in tools called methods.
Methods are generally identified and used
with DOT notation. Which is the syntactical
way of attaching a method to the object or
item it's working with using a dot. 
"""



"""         Adding List El:
append and insert are two methods used to
add list els.
append -> adds items to the end of the list
insert -> adds el at the specific position


To add a list of items to an existing list,
you can use the extend method or the addition
operator(+)
"""

#       Ex: 1 -> .append() & .insert()
listOfPets = ["bird", "hamster", "dog", "cat"]

# Adding spider to the end of listOfPets
# listOfPets.append("spider")

# Adding spider on 1st position
# listOfPets.insert(1,"spider")
# print(listOfPets)


#       EX: 1.2  -> .append() & .insert()
# Adding fish to the end of listOfPets
listOfPets.append("fish")

# Adding pig to the 2nd position
listOfPets.insert(2, "pig")
# print(listOfPets)


#       EX: 1.3  -> .extend()
secListOfPets = ["lizard", "mice", "ferret", "snake"]

# extend listOfPets
listOfPets.extend(secListOfPets)
print(listOfPets)



"""         Popping list Els:

"""