# Lists and Sets

#  *** Slicing -> similar to slicing a string
#   Doesn't change original sequence

fruits = ["apples", "bananas", "cherry", "date", "elderberry"]

# bannas, cherry, date
# print(fruits[1:4])

# apples, bananas, cherry
# print(fruits[0:3])

# date, elderberry
# print(fruits[3:])

# cherry, date, elderberry
# print(fruits[2:])


#               Section: 1.2
my_list = ["first", "second", "third", "fourth"]

# print single element using the positive index
print(my_list[1])

# print single element using the negative index
print(my_list[-1])

# print range of values using the slice operator
print(my_list[1:3])