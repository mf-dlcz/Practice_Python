import json

orders = []

with open(orders_filename, 'r') as order_data:
    for order_json in order_data:
        order = json.loads(line)
        orders.append(order)