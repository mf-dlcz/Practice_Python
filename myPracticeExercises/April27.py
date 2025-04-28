# Notes
# print("Examples for conversions between collections:")
# print("----------------")

# Starting Examples:
list_example = [1, 2, 2, 3]
tuple_example = (1, 2, 3, 4, 3, 2, 1)
set_example = {1, 2, 3}
alphanums = {"a": 1, "b": 2}

print("---------- Converting TO LIST -----------")
print(list(tuple_example))  # From tuple: [1, 2, 2, 3]
print(list(set_example))    # From set: [1, 2, 3]
print(list(alphanums))   # From alphanums: ['a', 'b'] (keys only)

print("---------- Converting TO TUPLE ----------")
print(tuple(list_example))  # From list: (1, 2, 2, 3)
print(tuple(set_example))   # From set: (1, 2, 3)
print(tuple(alphanums))  # From alphanums: ('a', 'b') (keys only)

print("---------- Converting TO SET ----------")
print(set(list_example))    # From list: {1, 2, 3}
print(set(tuple_example))   # From tuple: {1, 2, 3}
print(set(alphanums))    # From alphanums: {'a', 'b'} (keys only)

print("---------- Converting TO DICTIONARY ----------")
# From list of tuples/lists (must be key-value pairs)
print(dict([['a', 1], ['b', 2]]))  # {'a': 1, 'b': 2}
print(dict([('a', 1), ('b', 2)]))  # {'a': 1, 'b': 2}

# # Creating a books dictionary with title:author pairs
# books = {
#     "1984": "George Orwell",
#     "The Hobbit": "J.R.R. Tolkien",
#     "Pride and Prejudice": "Jane Austen",
#     "Dune": "Frank Herbert",
#     "The Great Gatsby": "F. Scott Fitzgerald"
# }