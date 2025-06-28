from datetime import datetime
import json

today = datetime.now()
orders_filename = today.strftime('orders_%Y%m%d.txt')

'''
Convert the JSON objects to Python objects so that you can loop
through the data and tally sales.

Print each order's total and a total for the whole day.
'''

orders = []

with open(orders_filename, 'r') as order_data:
    for order_json in order_data:
        order = json.loads(order_json)
        orders.append(order)

daily_total = 0
prices = {
    'cup': 1.00,
    'cone': 1.50,
    'scoop': 1.50
}

for order in orders:
    order_total = 0
    for item in order:
        item_price = 0
        container_type = item['container']
        item_price += prices[container_type]

        num_scoops = len(item['scoops'])
        item_price += nums_scoops * prices['scoop']
        print(f'    Item price ${item_price:.2f}')
        order_total += item_price
    print('Order total:', f'${order_total:.2f}' )
    daily_total += order_total

print(f'Total Daily Sales: ${daily_total:.2f}')