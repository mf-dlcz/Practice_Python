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
# print(all_items)


#   ###################################################              CREATING & EDITING DICTIONARIES:
fruit_inventory = {
    "kiwi": 11,
    "apricot": 9,
    "pomegranate": 15,
    "orange": 4,
}

#       .keys()
# copies all the keys to the inventory_keys variable
inventory_keys = fruit_inventory.keys()
# print("\nFruit Inventory Keys: \t",inventory_keys)


#       .fromkeys()
"""
- Creates a new dictionary based on the keys in an existing dictionary 
and sets an initial value for all the keys.
EX.     {'kiwi': 10, 'apricot': 10, 'pomegranate': 10}

    - Every key value pair has an initial value of 10
"""
new_store_inventory = fruit_inventory.fromkeys(inventory_keys, 10)
# print("The new_store_inv holds these key-value pairs:", new_store_inventory)


#       .copy()
# creates a new dictionary from an existing one.
copy_fruit_inventory = fruit_inventory.copy()

# added a new key, value pair to copy_fruit_inventory
copy_fruit_inventory["grapes"] = 20

# print("Copy: \t",copy_fruit_inventory)
# print("\nOriginal: ", fruit_inventory)


#   ############################################                   EDITING DICTIONARIES:
"""
- To add a new item to the fruit_inventory dictionary
we can use the .update() method.
- If a key already exists we can use the .update() to
update the value.
"""
# creating a new key value pair
fruit_inventory.update({"blueberries": 2})
# print(fruit_inventory)

# Update an existing value
fruit_inventory.update({"apricot": 19})
# print(fruit_inventory)


# Remove items:
#       .pop()
# variable = dictionary_name.pop("key")        -> Returns an integer
new_inventory = fruit_inventory.pop("kiwi")
# print(fruit_inventory)

#       .popitem()
# removes the last item from the dictionary and stores it in a variable
last_fruit = fruit_inventory.popitem()
second_to_last_fruit = fruit_inventory.popitem()

# print("Fruit Inventory: ", fruit_inventory)
# print("Removed Fruits: ", last_fruit, second_to_last_fruit)


#       .clear()
# removed all items from the dictionary
fruit_inventory.clear()
# print(fruit_inventory)


#   #######################################                     ADDITIONAL PRACTICE:

# Create the inventory dictionary
vehicle_inventory = {
    "sedan": 15,
    "truck": 42,
    "mini-van": 26,
    "crossover": 30,
    "convertible": 31,
    "Limousine": 3
}

#           TASK #1: ACCESS KEYS & VALUES

# use .key() to get all the keys in the inventory dictionary
vehicle_keys = vehicle_inventory.keys()
# print(vehicle_keys)

# use .values() to get all the values in the inventory dictionary.
vehicle_values = vehicle_inventory.values()
# print(vehicle_values)


#           TASK #2: USE .get() & ADD A NEW ITEM

# used the .get() to get the value of..
# print(vehicle_inventory.get("crossover"))
# print(vehicle_inventory.get("wagon"))

# two ways to add a key, value pair to vehicle_inventory
vehicle_inventory["Hatchback"] = 19
# print(vehicle_inventory)

# using .update() to add a key, value pair to vehicle_inventory
vehicle_inventory.update({"off-road": 21})
# print(vehicle_inventory)


#           TASK #3: COPY & CREATE A NEW DICTIONARY

# creates a copy of vehicle_inventory
copy_of_vehicle_inventory = vehicle_inventory.copy()

# creates a new dictionary from existing and gives all the values an initial value
new_vehicle_inventory = vehicle_inventory.fromkeys(vehicle_inventory, 1)

# print("Copy of vehicle inventory: ", copy_of_vehicle_inventory)
# print("\nNew vehicle inventory", new_vehicle_inventory)


#           TASK #4: REMOVE ITEMS

# using .pop() to remove the key, value selected
# removing mini-vans because everyone purchased one... except me 😂
# returns the value of the key selected
removed_miniVans = vehicle_inventory.pop("mini-van")
# print(vehicle_inventory)

# use .popitem() to remove the last item added to vehicle_inventory
remove_lastVehicle = vehicle_inventory.popitem()
# print(vehicle_inventory)


#           TASK #5: CLEAR DICTIONARY

# use .clear() to clear vehicle_inventory
vehicle_inventory.clear()
print(vehicle_inventory)