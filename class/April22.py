                                                    # Data Structures
'''          List
Mutable, ordered, non-unique items (can have mixed data types)
'''

            # Exercise 1:       
# Empty List
# veggies = []

# List of fruits
# fruits = ["papaya", "pomegranate", "kiwi"]
# first element
# print(fruits[0])
# last value
# print(fruits[-1])

# replace papaya with orange
# fruits[0] = "orange"
# print(fruits)


            # Exercise 2:
'''         Set 
- unique items, unordered, { }, mutable
- reminds me of: a box of markers, since each color is unique in a box. 
'''
# colors = {"green", "orange", "purple"}
# print(colors)


            # Exercise 3:
'''         Tuple 
- Sequenced (order, index), immutable elements
- reminds me of: Curb side pick up. Once order is placed can't be modified.
'''

# zoo = ("Python", "Giraffe", "Koala")
# print(zoo)
# access individual elements using their index
# print(zoo[2]) # Koala


            # Exercise 4:
'''         Dictionary
- Mutable, unordered key-value pairs (NO INDEX)
'''

person = {"name": "Tina", "age": 97, "city": "Why does it matter"}
# must include key to access value
print(person["city"])


#################################################################

# Additional notes:
#List - [], ordered so has indices, mutable
#empty list
nums = []

#list of fruits []
fruits = ['apples', 'bananas', 'oranges']

print(fruits)

#access a single element with positive or negative indexing
print(fruits[-1])

#replace apples with pears - modify existing values
fruits[0] = 'pears'

#add an element by using index - will not work!
# fruits[3] = 'plums'
print(fruits)

############################################################################
#Set - unique items, unordered, {}, mutable
#set = box of markers
colors = {'red', 'green', 'blue', 'blue'}
print(colors)
#sets cannot use indexing to access elements

#list of kindergarten ages
my_ages = [5, 6, 5, 6, 5, 5, 5, 5, 6, 6, 7]
print(my_ages)

#To get number of unique elements in the list:
#convert list to a set using set()
ages_set = set(my_ages)
#unique elements in the list = length of the set
print(len(ages_set))

#membership testing 
print('yellow' in colors)

############################################################################
#tuple - (), indexing, cannot modify element values once created - IT
coords = (10, 20, 30)
print(coords)
#individual elements using indexing
print(coords[:2])

#cannot change the element value
#coords[1] = 50

coords = (10, 20, 30, 40, 50)
print(coords)

list_coords = list(coords)
print(list_coords)

#create empty tuple
tup = ()

#############################################################################
#created empty dictionary
emp_info = {}

print(type(emp_info))

#keys must be unique
person = {"name":"Terry", "age":56, "city":"Anytown"}
print(person)

#accessing individual values - name_of_dictionary["key"]
print(person["name"])

#modifying elements
person["name"] = "Krishna"
print(person)