#   #################       Working with Sets:

"""
Sets have unique values. 
Use a set constructor to convert
a list to a set which will remove the
duplicate values.

******   set() constructor converts an iterable into
a set of unordered unique els.      ***********
"""

list = [1, 1, 2, 2, 3, 4, 2, 1, 5, 6, 7, 4, 3, 4, 5, 6]

# convert to set to remove duplicate values
my_set = set(list)

# print(my_set)


#      ###################        SET Methods: Determining membership
#  |   in   |     -> used to check if an el belongs to a set.

nums = {1, 3, 2, 4, 5, 6}
# print(2 in nums)            # True since 2 is in the set
# print(5 in nums)            # True
# print(0 in nums)            # False


#   |   not in  |   -> used to check if an el doesn't belong to a set.
# print(100 not in nums)      # True 100 is not in the set
# print(20 not in nums)       # True 20 is not in the set
# print(1 not in nums)        # False 1 is in the set


#   ######################          BOOLEAN SET METHODS: 
"""
To understand relationships among all els of two sets, you
can use a collection of methods named after relationships
defined in set theory.

                            SET THEORY:
Set theory deals with the properties and relationships between
collections.
- Membership -> whether an object belongs to a particular set
- Subsets -> One set is entirely contained within another
- Union, Intersection, complement
- Cardinality -> size of a set (finite or infinite)
"""

#                       .isdisjoint()   
# returns True if the two sets have no common els
wild_animals = {"pig", "lion", "koala", "kangaroo"}
farm_animals = {"cow", "chicken", "sheep", "pig"}
australian_animals = {"koala", "kangaroo"}

# print(farm_animals.isdisjoint(wild_animals))            # False; they have "pig" in common
# print(wild_animals.isdisjoint(australian_animals))      # False; they have "koala" & "kangaroo" in common
# print(farm_animals.isdisjoint(australian_animals))      # True; No els in common


#                       .issubset()     
# returns True if the first set contains ALL els of the second set
school_supplies = {"paper", "pen", "sticky notes", "backpack", "computer"}
camping_supplies = {"tent", "pen", "book", "blanket", "air mattress", "cooler", "sunglasses", "hat"}
work_supplies = {"sticky notes", "paper", "computer"}

# print(school_supplies.issubset(camping_supplies))               # False; only one item in common
# print(work_supplies.issubset(school_supplies))                  # True; ALL els are the same


#                       .issuperset()
# returns True if the second set contains ALL the els of the first set      |   converse of .issubset()   |
# print(work_supplies.issuperset(school_supplies))                   # False; ALL els in school_supplies are NOT in work_supplies 
# print(school_supplies.issuperset(work_supplies))                   # True; ALL els in work_supplies are IN school_supplies



#   ##########################################                      JOINS, UPDATES, & GENERATING NEW SETS:
"""
set relationships can be used to join sets together,
create new sets, and modify the membership of existing
sets.
"""

#           .difference()
# creates a new set that contains the differences between a set & one or more other sets

setA = {"Python", "JavaScript", "PHP"}
setB = {"Python", "JavaScript", "Java", "C++"}

diff_of_sets = setB.difference(setA)                # {"C++", "Java"}
diff_of_sets = setA.difference(setB)                # {"PHP"}
# print(diff_of_sets)


#           .difference_update()
# finds the difference but makes changes to the original set instead of creating a new set
# setB.difference_update(setA)                        # removed all the els in common and returned only the difference.
# print(setB)                                         # setB was modified and only contains {"C++", "Java"}

# setA.difference_update(setB)                          # removed all els and kept {"PHP"}
# print(setA)


#   ###########################################                     FINDING THE INTERSECTION:

#           .intersection()
# finds where sets overlap. It creates a new set that contains common els between two sets.

combination_of_AB = setA.intersection(setB)
# print(combination_of_AB)

# finds intersection between a set & a list
setC = {"JavaScript", "TypeScript", "Node.js"}
listC = ["Python", "JavaScript", "Java"]

intersection_of_cLists = setC.intersection(listC)
print(intersection_of_cLists)