# Tuples:

"""
Store a collection of data in a single variable. 
They're immutable (CANNOT BE CHANGED AFTER CREATED). 
They're used for storing info that will NOT,or 
should NOT change. They're ordered, mutable collections
that can store data of any type and duplicate values.
"""

#           Initializing Tuples:
#   Both are tuples:
tuple = (2, 3, 5, 6, 1, 10, 0)
tuple_2 = "apples", "bananas", "oranges"
# print(type(tuple), type(tuple_2))                   # <class 'tuple'>  --> output


#           Tuple with one value:
# IF COMMA IS REMOVED ITS DT CHANGES TO INT
tuple1 = (10,)
tuple1_1 = 20,
# print(type(tuple1), type(tuple1_1))

"""         NEED HELP WITH THIS:
#           Creats an empty tuple
tuple_constr = tuple()
# print(type(tuple_constr))


#           List converts to tuple
list = tuple(["M", "M", "D", "J"])
print(list, type(list))

"""


#                   Accessing items: using positive index & negative index
new_tuple = ("zero", "one", "two", "three", "four")

# print(new_tuple[0])
# print(new_tuple[-1])


#                   Exercise 1: Initializing & accessing items

# Step 1: Create a tuple to store details of a pet adoption.
# Example details: "Golden Retriever", "John Doe", 1, "01-01-2025", 300.00
# adoption_details = ("Golden Retriever", "John Doe", 1, "01-01-2025", 300.000)

# Step 2: Print the entire tuple to confirm its contents.
# print("Adoption details:", adoption_details)

# Step 3: Access and print the pet's breed and the adoption fee using positive indexing.
# print(f"Dog's Beed: \t{adoption_details[0]} \nAdoption Fee: \t{adoption_details[4]}")

# Step 4: Access and print the adopter's name using negative indexing.
# print(f"Adoptor's Name: \t{adoption_details[-4]}")

# Step 5: Create a tuple using the tuple constructor to store adoption status options.
# Example options: "Pending", "Approved", "Rejected"
adoption_status = tuple(["Pending", "Approved", "Rejected"])

# Step 6: Print the tuple of adoption status options.
print("Adoption status options:", adoption_status)