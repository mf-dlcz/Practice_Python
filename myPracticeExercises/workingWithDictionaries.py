"""
Working with Dictionaries:
"""

inventory = {
    "apples": 5,
    "bananas": 4,
    "coconuts": 2,
    "dates": 10
}

#   ACCESSING KEYS & VALUES:
#       .get()
# retrieves the value associated with the provided key. 
# DOESN'T raise an error if they doesn't exist instead returns None

#   dictionary_name.get("key")
# print(inventory.get("coconuts"))        # 2
# print(inventory.get("kiwi"))            # None
# print(inventory.get("dates"))           # 10


#       .keys()
# lists all keys in a dictionary.
# returns a special data type, dict_keys, that remains tied to the dictionary in memory

# stores all the keys in the inventory_keys variable
inventory_keys = inventory.keys()
# print(inventory_keys)

# creates a new key,value pair
inventory["apricot"] = 7
# print(inventory)


#       .values()
"""
- Displays a list of all the values in a dictionary.
- Returns a special data type, dict_values. 
- You can treat it as a list in many ways, but it is a
view of the dictionary values.
- If values in the dictionary change, so will this data.
"""

# stores all the inventory values as a list in the inventory_values variable
inventory_values = inventory.values()
# print(inventory_values)


#       .items()
"""
- Retrieves all the key-value pairs from a dictionary.
- Returns another special data type, dict_items
- Returned values look and function like a list of tuples,
but if the underlying dictionary data changes, so will this data.
"""

# created a new key, value pair
inventory["raspberry"] = 3

# stored list of tuples in the all_items variable
all_items = inventory.items()
print(all_items)