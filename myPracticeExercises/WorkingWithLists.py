"""         List Methods
Lists have built in tools called methods.
Methods are generally identified and used
with DOT notation. Which is the syntactical
way of attaching a method to the object or
item it's working with using a dot. 
"""


#   #####################################               Adding List El:
"""
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
# print(listOfPets)


#       ###############################             Popping list Els:
"""
The pop method removes els from the list.

*** Optionally, you can specify the index of the
item to remove as a parameter. If no index is specified,
the last item on the list will be removed.
"""

# Remove a lost pet from listOfPets - No Index (last item)
lostPet = listOfPets.pop()
# print(lostPet)          # Removed Snake since it's the last item

# Remove fish
removedFish = listOfPets.pop(5)
# print(removedFish)

# Remove pig
# print(listOfPets)
removePig = listOfPets.pop(2)
# print(removePig)


#   ###################################             Removing List Els:
"""
Methods to remove el from a list are
.remove() & .clear()

.remove ()      ->  Reference that item using its matching
string value or using the list name and position.

.clear()        ->  clears all value from the list.
"""

#       Example: .remove()
groceryList = ["oatmeal", "avocados", "apples", "bananas", "frozen fruit", "eggs", "milk", "sausages"]
# print(f"List of groceries: {groceryList}")

# Remove frozen fruit
groceryList.remove("frozen fruit")
# print(groceryList)

# Remove apples using its position
groceryList.remove(groceryList[2])
# print(groceryList)

#   clear the groceryList
groceryList.clear()
# print("Grocery List After .clear(): ", groceryList)


# #####  Example 2: .remove()
pets = ["dog", "cat", "hamster", "iguana", "goldfish"]

# removed goldfish
pets.remove("goldfish")
# print ("pets after remove('goldfish') is", pets)

# removes dog
pets.remove(pets[0])
# print ("pets after remove(pets[0]) is", pets)

# clear
pets.clear()
# print("pets after clear() is", pets)


#   ###############################                 Copying Lists:
"""
It can be useful to create a copy of a list to
avoid modifing the original list.

Method to create copy is .copy()
"""


#       Exercise: Using .copy()
todo_List = ["eat", "exercise", "study", "drive to work", "go for a walk", "eat lunch"]

# Creating copy
# copyOfTodoList = todo_List.copy()

# Creating copy using slicing
copyOfTodoList1 = todo_List[:]
# print("To Do List:", todo_List)
# print("\nCopy:", copyOfTodoList1)


#       Converting a tuple to a list
# tupleToList = list((1, 2, 3))           # <class 'list'>
# print(type(tupleToList))

#       Creates an empty list
emptyL = list()                            # <class 'list'>
# print(type(emptyL))

#       Creates a copy of the existing list
originalList = [1, 2, 3]
copyList = list(originalList)
# print("Original List: ", originalList)
# print("Copy of Original: ", copyList)


#       ################################            Modifying List Order:

"""         .sort() & .reverse()

.sort()     -> sorts a list into ascending values by default.
                If list els are strings, it sorts alphabetically.
                ** Optionally, the list can be sorted in descending, or
                reverse alphabetical, order.

.reverse()  ->  reverses the order of a list.
"""

#           Example:    .sort()
cities = ["New York", "San Francisco", "Los Angeles", "Orlando", "Phyladelphia", "Saint George", "Albany", "Brooklyn"]
# cities.sort()
# print(cities)


#           Example 2:
# sort alphanumeric string
my_list = ["car", "boat", "truck", "1", "0", "20", "Car"]
shoeList = ["sneakers", "Boots", "sandals", "clogs", "Heels", "flats"]
my_list.sort()
# print("\nMixed case alphanumeric sort:", my_list)

# sort with optional reverse argument
my_list.sort(reverse=True)
shoeList.sort(reverse = True)
# print("Shoe List Reversed: ", shoeList)
# print("Sort with optional reverse argument:", my_list)

# sort using reverse method
groceries = ["apples", "berries", "cabbage"]
groceries.reverse()
# print("groceries after reverse()", groceries)


#   ###########################################         Counting Els:
"""         
.count()    -> finds the number of times an item
appears in a list.
"""

#           Example 1:
# numbers = [8, 6, 9, 8, 8, 9, 6, 10, 15, 20, 30, 31, 10]
# print(numbers.count(8))         # Returns 3 because the number 8 appears three times in the numbers list: at indices 0, 3, and 4.



#   ##########################################          Indexing:
"""
The method .index() find the first position of the 
first list el with a specified value.
"""

#           Example 1:
numberz = [0, 1, 3, 5, 7, 20, 10, 11, 20, 16, 18, 5, 9, 4]
# if 4 in numberz:
#     print(numberz.index(4))
# else:
#     print("Value 4 is not in the list.")


#       #####################################           Determine Membership:
"""
in and not in       -> tests whether a value is a member
of a sequence or collection. Each statement that uses
a membership operator returns True or False.
Frequently, the membership operator is used in a conditional
or loop to control the flow of your program.
"""
#       Example 1: Using the numberz list from line 210
# print(20 in numberz)            # True
# print(4 in numberz)             # True
# print(2 in numberz)             # False 2 is not in the list
# print(20 not in numberz)        # False because 20 is in the list
# print(2 not in numberz)         # True because 2 is not in the list


#   ######################################                  Exercises: List Methods
# Practicing Python List Methods

# Step 1: Create a list of numbers and a list of fruits.
numbers = [10, 20, 30, 40, 50]
fruits = ["cherry", "banana", "apple"]

#      ###       TASK #1: ADD ELS           ###
# Adding 60 to numbers using .append()
numbers.append(60)
# print(numbers)

# Adding "mango" to fruits using insert
fruits.insert(0, "mango")
# print(fruits)

#     ###        TASK #2: REMOVE ELS        ###
# remove banana using .remove()
fruits.remove("banana")

# remove last el using .pop()
fruits.pop()
# print(fruits)


#    ###         TASK #3: EXTEND & SORT     ###
#  combine new list ["peach", "pear"] with fruits using .extend()
fruits.extend(["peach", "pear"])
fruits.sort()
# print(fruits)

#   ###         TASK #4: Combine Methods    ###
# Create a copy of numbers
numsCopy = numbers.copy()

# Add 100 to numsCopy
numsCopy.append(100)

# reverse numsCopy
numsCopy.reverse()
# print("\nOriginal List:", numbers)
# print("\nCopy with modifications:", numsCopy)


#   ###          TASK #5: Complex Manipulation      ###
grocery_List = ["milk", "bread", "eggs", "butter", "cheese"]

# Add yogurt using .append()
grocery_List.append("yogurt")

# Remove butter using .remove()
grocery_List.remove("butter")

# Find position of "eggs" using .index() and insert juice before "eggs"
index = grocery_List.index("eggs")
# print(index)
grocery_List.insert(index, "juice")
grocery_List.sort()

print(grocery_List)


"""   #########         .sort()   &   .reverse()            #########
Returns None because they are modifying the original list not 
creating and returning a new list
"""
print(grocery_List.sort())