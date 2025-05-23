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

employees = [
    {
        "name": "Michael",
        "age": 32,
        "position": "Data Analyst",
        "department": "Data"
    },
    {
        "name": "Elise",
        "age": 34,
        "position": "Software Engineer",
        "department": "IT"
    },
    {
        "name": "Sophie",
        "age": 30,
        "position": "DevOps",
        "department": "IT"
    },
    {   
        "name": "William",
        "age": 33,
        "position": "Machine Learning Engineer",
        "department": "Data Science"
    }
]

# Step 2: Use a loop to print each employee's name and department.
# Example output: "John is in the Sales department."

for employee in employees:
    # print(f'{employee["name"]} is in the {employee["department"]} department.')


# Step 3: Modify the loop to also print each employee's position.
# Example output: "John is in the Sales department and works as a Manager."

    print(f'{employee["name"]} is in the {employee["department"]} department and works as a {employee["position"]}.')