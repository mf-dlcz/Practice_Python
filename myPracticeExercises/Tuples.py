# Tuples:

"""
Store a collection of data in a single variable. 
They're immutable (CANNOT BE CHANGED AFTER CREATED). 
They're used for storing info that will NOT,or 
should NOT change. They're ordered, mutable collections
that can store data of any type and duplicate values.
"""

#           Initializing Tuples:
#   Both are tuples:
tuple = (2, 3, 5, 6, 1, 10, 0)
tuple_2 = "apples", "bananas", "oranges"
# print(type(tuple), type(tuple_2))                   # <class 'tuple'>  --> output


#           Tuple with one value:
# IF COMMA IS REMOVED ITS DT CHANGES TO INT
tuple1 = (10,)
tuple1_1 = 20,
# print(type(tuple1), type(tuple1_1))

#           Creats an empty tuple
tuple_constr = tuple()
# print(type(tuple_constr))


#           List converts to tuple
list = tuple(["M", "M", "D", "J"])
print(list, type(list))