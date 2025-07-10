'''
#? Concepts Covered: Classes (Creating Unique Objects, Custom Methods), Object Notation, Arguments, Basic Data Structures (Lists or Dictionaries)

#*              The Challenge:

#* Define an Item Class:

Create a class called Item.

Each Item should have attributes like name (string) and price (float or integer).

When you create a new Item object, you should be able to provide its name and price.

Add a method to the Item class called display_info() that prints the item's name and price in a readable format (e.g., "Laptop: $1200.00").

#* Create an Inventory:

Maintain a list or dictionary of Item objects representing your inventory.

Create a few sample Item objects (e.g., a "Laptop", "Mouse", "Keyboard") and add them to your inventory.

#* Display Inventory: 

Write a function that iterates through your inventory and calls the display_info() method for each item.

#* Hints for your approach:

Remember the __init__ method for initializing object attributes.

How do you define a method within a class that can access the object's own attributes?

How would you create an instance (an object) of your Item class?
'''

class Item:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        return f"Item: {self.name} Price: ${self.price}"


'''         TESTING             '''
item1 = Item('laptop', 3200)
item2 = Item('mouse', 60.89)
item3 = Item('keyboard', 350.03)

