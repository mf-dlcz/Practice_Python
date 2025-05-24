import json

"""
Nested Data Structures
"""

employees = [
    {"name": "John","age": 35,"position": "Manager", "department": "Sales"},
    {"name": "Ana","age": 28,"position": "Engineer", "department": "IT"},
    {"name": "Carlos", "age": 42, "position": "Director",
        "department": "Operations"}
]

# for emp in employees:
#     print (f'{emp["name"]} is in the {emp["department"]} department.')

#       EXAMPLE: using a for loop to iterate
# for emp in employees:
#     print(f"{emp['name']} is {emp['age']} years old.")


#   #########################################                   LISTS OF DICTIONARIES WITH LISTS:
"""
- Dictionaries can hold any type of data.
To access a list one can use indexing or a loop.
"""

students = [
    {'name': 'Alice', 'age': 20, 'grades': [90, 85, 95]},
    {'name': 'Bob', 'age': 21, 'grades': [80, 75, 70]},
    {'name': 'Charlie', 'age': 19, 'grades': [95, 90, 92]},
]

# for student in students:
#     # grades holds the grades list for the loop's current iteration
#     grades = student['grades']

#     # This line calculates the average value of the numbers in grades using Python’s built-in sum and len functions.
#     avg_grade = sum(grades) / len(grades)

#     # creates a new key-value for each student
#     student['avg_grade'] = round(avg_grade,2)

# print (students)

#       .sum()
"""
-> Built-in mathematical function that
returns the sum of all the NUMBERS in an iterable
"""

#       .round()
"""
-> Built-in mathematical function that returns
a number rounded to the nearest decimal place
specified.
"""

#   #######################################         NESTED ITEMS IN EMPLOYEE RECORDS

# Step 1: Create a list of dictionaries to store employee details.
# Each dictionary should have keys: "name", "age", "position", "department"

employees1 = {
        "001": {
        "name": "Michael",
        "age": 32,
        "position": "Data Analyst",
        "department": "Data"
    },
        "002": {
        "name": "Elise",
        "age": 34,
        "position": "Software Engineer",
        "department": "IT"
    },
        "003": {
        "name": "Sophie",
        "age": 30,
        "position": "DevOps",
        "department": "IT"
    },
        "004": {   
        "name": "William",
        "age": 33,
        "position": "Machine Learning Engineer",
        "department": "Data Science"
    }
}

# Step 2: Use a loop to print each employee's name and department.
# Example output: "John is in the Sales department."

# for employee in employees:
    # print(f'{employee["name"]} is in the {employee["department"]} department.')


# Step 3: Modify the loop to also print each employee's position.
# Example output: "John is in the Sales department and works as a Manager."

    # print(f'{employee["name"]} is in the {employee["department"]} department and works as a {employee["position"]}.')
    


#   ###############################################             Using Nested Dictionaries:

"""
- Nested Dictionary:  Dictionary that is contained by another dictionary.
- By organizing information in nested dictionaries, you can model your data 
as a hierarchical structure that can include layers of groups and subgroups.

- Use dictionary name and key in bracket notation
"""

# Accessing William's data:
# employee_profile = employees["004"]

#Accessing employee name and age
# print(f'{employee_profile["name"]}, is a {employee_profile["position"]}.')

# Accessing Williams deparment
# print(f'{employee_profile["name"]} is in the {employee_profile["department"]} department.')

"""
- Accessing employee 004's age can be done without storing the value in a variable
- Accessing directly from the main dictionary.
- It's not practical for the goal of accessing a single nested value.


- Start with the name of the outer dictionary. Then, 
use the key associated with the dictionary that you 
want to access, followed by the key associated 
with the nested value.
"""

# print(employees["004"]["age"])


#       EXERCISE: NESTED DICTIONARY OF EMPLOYEES

employees = {
    "001": {
        "name": "John",
        "age": 35,
        "position": "Manager",
        "department": "Sales",
        "location": {
            "street_address": "123 Main Street",
            "city": "Anytown",
            "country": "USA",
        },
    },
    "002": {
        "name": "Ana",
        "age": 28,
        "position": "Engineer",
        "department": "IT",
        "location": {
            "street_address": "456 Any Ave",
            "city": "Anyville",
            "country": "USA",
        },
    },
}

#           TASK #1: Access employee details

# Access & print the name of the employee with ID "001".
id001 = employees["001"]["name"]
# print(id001)

# Access and print the city of the employee with ID "002".
id002 = employees["002"]["location"]["city"]
# print(f'{employees["002"]["name"]} lives in {id002}.')


#           TASK #2: Add a new employee
"""
- Add a new employee with ID "003" to the employees dictionary. The employee's details are:
    Name: "Carlos"
    Age: 42
    Position: "Director"
    Department: "Operations"
    Location:
        Street Address: "789 New St"
        City: "Newtown"
        Country: "USA"
- Print the updated employees dictionary.
"""

employees["003"] = {"name": "Carlos", "Age": "42", "position": "director", "department": "operations", "location": {"street ddress": "789  New St", "city": "Newtown", "country": "USA",}}

# print(json.dumps(employees, indent = 4))


#           TASK #3: Update employee details

# Update the position of the employee with ID "001" to "Regional Manager"

employees["001"]["position"] = "Regional Manager"
# print(json.dumps(employees["001"], indent = 4))


#           Task #4: Access nested values
employee_address = employees["002"]["location"]["street_address"]
# print(employee_address)


#           TASK #5: Delete an employee
# removed_employee = employees.pop("003")
# print(json.dumps(employees, indent = 4))

# using del keyword will delete a key
# keyword dictionary_name["key"]

del employees['001']
print(json.dumps(employees, indent = 4))