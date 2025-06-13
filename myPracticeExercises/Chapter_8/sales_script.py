'''
Sales class holds and records sales data. It 
then generates a descriptive sales report.
'''

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