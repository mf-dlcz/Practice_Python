menu = [    
    {"item": "Pizza", "price": 12.99, "ingredients": ["tomato", "cheese", "basil"]},
    {"item": "Salad", "price": 8.99, "ingredients": ["lettuce", "tomato", "cucumber"]},
    {"item": "Pasta", "price": 14.99, "ingredients": ["pasta", "tomato sauce", "garlic"]}
]

# for element in menu:
#     print(element['ingredients'])
    
first = menu[0]
# print(first)
for each_element in first:
    print(f"Key is {each_element}, value is {first[each_element]}")
    
print("Second approach: ")
print("----------------------------------------")
for key, value in first.items():
    print(f"Key is {key} and the value is {value}")
    
# print(menu[0]['item'])

# print(menu[0]['ingredients'][2])