import ice_cream_shop
import json
from datetime import datetime

'''
Implement additional functionality
to the program so that it appends a new line for every order to a file called 
orders_<date>.txt where <date> is replaced with the current date in the
format YYYYMMDD.

Use json.dump to append the item to the file with the correct formatting.
'''

today = datetime.now()
orders_filename = today.strftime('orders_%Y%m%d.txt')
# print(orders_filename)

print("-=-=-=-=-=-=-=-=-")
print("Receipt script")
print("-=-=-=-=-=-=-=-=-")

print(ice_cream_shop.items)

with open(orders_filename, 'a') as orders_file:
    json.dump(ice_cream_shop.items, orders_file)
    orders_file.write('\n')