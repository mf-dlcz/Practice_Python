"""
Dictionaries are an iterable.
"""

#       Example 1:
sales_wk1 = {
    "Monday": 10,
    "Tuesday": 10,
    "Wednesday": 5,
    "Thursday": 5,
    "Friday": 15,
    "Saturday": 20,
    "Sunday": 15
}

# Looping through sales_wk1
# for day in sales_wk1:

    # prints keys
    # print(day)

    # prints values
    # print(sales_wk1[day])


## print keys using built in keys() method
# for day in sales_wk1.keys():
#     print(day)


## print value using the built in values() method
# for value in sales_wk1.values():
#     print(value)


## Use the items() method to loop through keys & values

"""            SYNTAX
for key, value in dictionaryName.items():
"""
# for key, value in sales_wk1.items():
#     print(key, value)


#       Accessing Values By Key:
sales_wk2 = {
    "Monday": 20,
    "Tuesday": 30,
    "Wednesday": 65,
    "Thursday": 45,
    "Friday": 95,
    "Saturday": 10,
    "Sunday": 85
}

# total_sales = 0

# for k in sales_wk2:
#     total_sales += sales_wk2[k]
# print (total_sales)


#       Exercise: Weekly Sales Data

# Step 1: Create a dictionary to store weekly sales data for a pet store.
# Data: "Monday": 8, "Tuesday": 12, "Wednesday": 5, "Thursday": 7, "Friday": 15, "Saturday": 20, "Sunday": 10
wkly_petSales = {
    "Monday": 8,
    "Tuesday": 12,
    "Wednesday": 5,
    "Thursday": 7,
    "Friday": 15,
    "Satursday": 20,
    "Sunday": 10
}

# Step 2: Loop through the dictionary and print only the keys (days of the week).
# Example output: "Monday"
#               First Way: using a regular for loop
# for day in wkly_petSales:
#     print(day)
#               Second Way: Using the key() method
# for day in wkly_petSales.keys():
#     print(day)


# Step 3: Loop through the dictionary and print only the values (number of sales).
# Example output: "8"
#               First Way: Using a regular for loop
# for day in wkly_petSales:
#     print(wkly_petSales[day])
#               Second Way: Using values() method
# for day in wkly_petSales.values():
#     print(day)


# Step 4: Loop through the dictionary to print both keys and values.
# Example output: "Monday: 8"
# for k, v in wkly_petSales.items():
#   print(f"{k}: \t{v}")

# Step 5: Calculate the total sales for the week by accessing values directly.
# Print the total sales.

wk2_totalSales = 0

for v in wkly_petSales:
    wk2_totalSales += wkly_petSales[v]
print(wk2_totalSales)