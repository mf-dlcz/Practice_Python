'''
Exercise: Converting a dict into a JSON string.
'''
import json

data = {
    "book_title": "The Hitchhiker's Guide to the Galaxy",
    "author": "Douglas Adams",
    "year_published": 1979,
    "genre": "Science Fiction Comedy",
    "characters": ["Arthur Dent", "Ford Prefect", "Zaphod Beeblebrox", "Marvin"],
    "is_available": True,
    "details": {
        "pages": 193,
        "publisher": "Pan Books",
        "isbn": "0-345-39180-2"
    }
}
'''

# Converting a dictionary into a python string
json_str = json.dumps(data)

# print(json_str)

# adds the json string[[data]] to the data.json file
with open('data.json', 'w') as json_file:
    json_file.write(json_str)


# Reading data from the file
# import json 
with open('data.json', 'r') as input:
    # Converts the json string
    details = json.load(input)

print(type(details))

'''

###########################################################################

#                       EXERCISE:

product_data = {
    "product_name": "Wireless Bluetooth Earbuds",
    "product_id": "ELEC001",
    "price": 49.99,
    "in_stock": True,
    "specifications": {
        "color": "Black",
        "battery_life": "8 hours",
        "water_resistant": False
    },
    "reviews": [
        {
            "user": "TechLover22",
            "rating": 5,
            "comment": "Amazing sound quality!"
        },
        {
            "user": "MusicFanatic",
            "rating": 4,
            "comment": "Good value for the price, battery could be better."
        }
    ]
}

'''
# Convert python dictionary into a json string
product_data_str = json.dumps(product_data)

# <class str>
# print(type(product_data_str))

# opens and writes the converted JSON string into the product_data.json file
with open("product_data.json", "w") as json_file:
    json_file.write(product_data_str)

# read the string in the terminal
with open("product_data.json", "r") as input:
    product_info = json.load(input)

print(product_info)
'''

##############################################################
#                   EXERCISE:

'''
food = ['apricots', 'peach', 'mango', 'kiwi', 'blueberries']

# Convert list into a json str
str_food = json.dumps(food)

# <class str>
# print(type(str_food))

# Read str in terminal without creating a separate file
json_to_a_list = json.loads(str_food)
print(json_to_a_list)

'''

############################################################

#                   EXERCISE:

