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
