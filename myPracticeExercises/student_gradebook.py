'''
#? Concepts Covered: Nested Data Structures, Scope, Arguments, Sets, Tuples, Working 
#? with Sets/Tuples, Looping Through Iterables, Basic Statistics

#*              The Challenge:

#* Student Data Structure:

Design a way to store information for multiple students. For each student, you'll need their name, a 
student ID (perhaps a unique number), and a list of grades (numbers).

Consider using a dictionary where keys are student IDs, and values are another dictionary containing the 
student's name and a list of their grades.

#* Add Student:

Create a function that takes student_id and name as arguments and adds a new student to your gradebook 
data structure.

Ensure student_id is unique. If a student with that ID already exists, inform the user. (This is a good 
place to think about how sets could help, or just a simple check against existing keys in your dictionary).

#* Add Grade:

Create a function that takes student_id and grade as arguments.

Add the grade to the specified student's list of grades.

If the student ID doesn't exist, handle this gracefully.

#* Calculate Average Grade:

Create a function that takes student_id as an argument.

It should return the average grade for that student.

What if a student has no grades? Handle this to prevent errors (e.g., division by zero).

#* Display Student Info:

Create a function that takes student_id as an argument and prints the student's name, ID, 
and all their grades.

If the student is not found, print an appropriate message.

All Student Averages (Optional - but good for looping):

Write a function to display the name and average grade for all students in your gradebook.

Scope and Arguments: Pay attention to how variables are passed as arguments to your functions and 
what variables are accessible within different parts of your code (scope).

#* Hints for your approach:

How will you represent the list of grades for each student? A list is a natural fit.

To ensure uniqueness for student IDs, you might find a set useful for keeping track of all used IDs, 
or you can simply check if the ID is already a key in your main dictionary.

Think about how to iterate through your nested data structure to access individual student information 
and their grades.
'''

def add_grade(student_id, grade):
    pass

def calc_average_grade(student_id):
    pass

def display_student_info(student_id):
    return f"Student: \nStudent ID: {student_id}\nGrades: "
