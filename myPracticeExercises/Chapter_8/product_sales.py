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
        sale = {'product': product, 'quantity_sold': quantity}
        self.sales_data.append(sale)

    def generate_report(self):
        products = {}
        report = ''
        total_sales = 0
        # loop through sales data and add a dict key for each unique product to the products dictionary
        for each_sale in self.sales_data:
            product_name = each_sale['product'].name
            # If this product has been seen before
            if product_name in products.keys():
            # add the new quantity to what we already have
                products[product_name]['quantity'] = products[product_name]['quantity'] + each_sale['quantity_sold']
            # If this is the first time we are seeing this product
            else:
            # create a new entry with q, price
                products[product_name] = {'quantity': each_sale['quantity_sold'], 'price': each_sale['product'].price}
        
        for product_name, product_data in products.items():
            # revenue for each product
            total_revenue = product_data['price'] * product_data['quantity']
            # add total_revenue to each item in the products dictionary
            products[product_name]['total_revenue'] = total_revenue
            total_sales += total_revenue
            report = report + f"{product_name} (${product_data['price']}) : {product_data['quantity']} {total_revenue}\n"
        report = report + f'Total Sales: {round(total_sales, 2)}\n'
        return report

    # def __iter__(self):
    #     self.index = 0
    #     return self

    # def __next__(self):
    #     if self.index >= len(self.sales_data):
    #         raise StopIteration
    #     name = self.sales_data[self.index]['product'].name
    #     quantity = self.sales_data[self.index]['quantity']
    #     sale = f'You sold {quantity} of {name}.'
    #     self.index += 1
    #     return sale


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

    # sales_iter = iter(sales)
    # print (next(sales_iter))
    # print (next(sales_iter))
    # print (next(sales_iter))
    # print (next(sales_iter))
    # print (next(sales_iter), '\n')


if __name__ == '__main__':
    test_classes()