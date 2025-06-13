'''
This module contains classes for tracking
product and sales data.
'''

class Product:
    def __init__(self, name, price, inventory):
        self.name = name
        self.price = price
        self.inventory = inventory
    
    def __str__(self):
        return f'{self.name} (${self.price})'


