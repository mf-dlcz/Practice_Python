import json

order_dictionary = {
  "orders": [
    {
      "orderId": "ABC123",
      "customerInfo": {
        "name": "John Doe",
        "email": "john.doe@example.com"
      },
      "orderDetails": [
        {
          "productId": "PROD001",
          "name": "Product A",
          "quantity": 2,
          "price": 19.99
        },
        {
          "productId": "PROD002",
          "name": "Product B",
          "quantity": 1,
          "price": 29.99
        }
      ],
      "totalAmount": 69.97,
      "paymentMethod": "Credit Card",
      "shippingAddress": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345"
      }
    }    
  ]
}

animals = ['monkeys', 'parrots', 'dolphins', 'kittens']

########## 
# write dictionary to python string

json_string = json.dumps(order_dictionary)
# print(json_string)

json_list_string = json.dumps(animals)
print(json_list_string)
# write dictionary to file using string

with open('order_info.json', 'w') as json_file:
  json_file.write(json_string)
  


# write dictionary directly to file using json library

with open('animals.json', 'w') as json_animals_file:
  json.dump(animals, json_animals_file)
  

##########  
# reading:

with open('order_info.json', 'r') as json_file:
  order = json.load(json_file)

# interact with dictionary

# print(type(order))
# print(order_dictionary)

# read list from jsonstring
list_from_json = json.loads(json_list_string)
print(type(list_from_json))