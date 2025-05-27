"""
Order Association:
"""

class Customer:
    
    def __init__(self, name, address, email):
        self.id = 'ID1234'
        self.name = name
        self.address = address
        self.email = email
        self.orders = []
        
class Product:
    def __init__(self, name, price, shipping_weight, barcode):
        self.id = 'PROD1234'
        self.name = name
        self.price = price
        self.weight = shipping_weight
        self.barcode = barcode
    def __str__(self):
        return str(vars(self))
        
class Order:
    def __init__(self, user):
        self.id = 'O-1234'
        self.user = user
        self.order_items = []
        
        
customer1 = Customer('Jason', {'street':'123 elm drive', 'city': 'College Station', 'state': 'tx'}, 'jason@notreal.com')
# print(vars(customer1))

laptop = Product(
    name="MacBook Pro 13-inch",
    price=1299.99,
    shipping_weight=3.0,
    barcode="8590123456789"
)

headphones = Product(
    name="Sony WH-1000XM4",
    price=349.99,
    shipping_weight=0.5,
    barcode="7891234567890"
)

coffee_maker = Product(
    name="Breville Espresso Machine",
    price=699.99,
    shipping_weight=15.7,
    barcode="6789012345678"
)

order = Order(customer1)
# print(vars(order))

order.order_items.append(laptop)
order.order_items.append(headphones)
order.order_items.append(coffee_maker)


# for item in order.order_items:
#     print(item)
    
customer1.orders.append(order)

print(customer1.orders[0].order_items)
for item in customer1.orders[0].order_items:
    print(item)