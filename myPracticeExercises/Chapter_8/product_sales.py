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

class Sales:
    def __init__(self):
        self.sales_data = []

    def add_sale(self, product, quantity):
        sale = {'product': product, 'quantity': quantity}
        self.sales_data.append(sale)

    def generate_report(self):
        total_value = 0
        for sale in self.sales_data:
            total_value += sale['product'].price * sale['quantity']

        report = ''
        # Get unique products from sales_data
        unique_products = {sale['product'] for sale in self.sales_data}

        for product in unique_products:
            quantity_sold = sum(
                sale['quantity'] for sale in self.sales_data if sale['product'] == product
            )
            revenue = round(product.price * quantity_sold, 2)
            report += f'{product}: {quantity_sold} sold for a total revenue of ${revenue}\n'

        report += f'Total Sales: ${total_value}\n'
        return report

#           TEST
def test_classes():
    prod1 = Product("WidgetA", 10.99, 100)
    prod2 = Product("WidgetB", 19.99, 50)
    prod3 = Product("WidgetC", 7.99, 150)
    prod4 = Product("WidgetD", 3.99, 500)
    
    sales = Sales()
    sales.add_sale(prod1, 15)
    sales.add_sale(prod2, 30)
    sales.add_sale(prod3, 45)
    sales.add_sale(prod1, 30)
    sales.add_sale(prod4, 100)
    
    print (sales.generate_report())

test_classes()