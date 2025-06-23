import ice_cream_lab
import json
from datetime import datetime

# stores the current date and time in today
today = datetime.now()

# creates an orders_filename and format the name of the file
orders_filename = today.strftime('orders_%Y%m%d.txt')

# prints the name of the file with requested file name
print(orders_filename)

print('\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('Receipt script')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(ice_cream_lab.items)

with open("orders_filename", "a") as orders_file:
    json.dump(ice_cream_lab.items, orders_file )
    orders_file.write("\n")