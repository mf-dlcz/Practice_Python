"""
This module contains classes for tracking product and sales data.
"""
'''
create a Product class with a constructor method that takes name, 
price, and inventory as arguments.
'''
class Product:
    def __init__(self, name, price, inventory):
        self.name = name
        self.price = price
        self.inventory = inventory
        
    # Add a __str__ method() that returns the name of the object with the price in parentheses. 
    def __str__(self):
        return f'{self.name} ({self.price})'
    
'''
Creating a Sales class

Now let's create a class that can hold and record sales data and generate a 
descriptive sales report. 
Create a sales class with a constructor method that takes no 
additional arguments and instantiates an object with an empty list named "sales_data".
'''

class Sales:
    def __init__(self):
        self.sales_data = []
        
    # add a method named add_sale() that takes product and quantity as arguments. Each sale should be recorded as a dictionary where the keys are "product" and "quantity" and the values are the product name and quantity arguments provided when the method is called. Each new dictionary should be added to the object's sales_data list. 
    def add_sale(self, product, quantity=1):
        self.sales_data.append({'product': product, 'quantity_sold': quantity})
        
    def generate_report(self):
        products = {}
        report = ''
        # loop through sales data and add a dict key for each unique product to the products dict
        for sale in self.sales_data:
            product_name = sale['product'].name
            if product_name in products.keys():
                # update quantity but do not update price as its already set
                products[product_name]['quantity'] = products[product_name]['quantity'] + sale['quantity_sold']  # Increment quantity
            else:    
                # for first iteration set the quantity and price
                products[product_name] = {'quantity': sale['quantity_sold'], 'price': sale['product'].price}
                
        # loop through products
        total_sales = 0
        for product_name, product_data in products.items():
            # calculate total revenue for each product
            total_revenue = product_data['price'] * product_data['quantity']
            # add total revenue to each item in the products dict
            products[product_name]['total_revenue'] = total_revenue
            total_sales = total_sales + total_revenue
            # add a newline to report with the product name and quantity and total revenue
            report = report + f'{product_name} (${product_data["price"]}): {product_data["quantity"]} {round(total_revenue, 2)}\n'
        report = report + f"Total sales: {round(total_sales, 2)}\n"    
        return report
        
    # def __iter__(self):
    #     self.index = 0
    #     return self   
    
    # def __next__(self):
    #     if self.index >= len(self.sales_data):
    #         raise StopIteration
    #     name = self.sales_data[self.index]["product"].name
    #     quantity = self.sales_data[self.index]["quantity_sold"]
    #     sale = f"You sold {quantity} of {name}."
    #     self.index += 1
    #     return sale

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

   #
    
    print(sales.generate_report())  
    
#     sales_iter = iter(sales)
#     print (next(sales_iter))
#     print (next(sales_iter))
#     print (next(sales_iter))
#     print (next(sales_iter))
    
#     print("-----------------")
#     print("looping through iterable")
#     for i in sales_iter:
#         print(i)

if __name__ == "__main__":
    test_classes()    
  

