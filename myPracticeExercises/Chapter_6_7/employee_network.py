#       EMPLOYEE SOCIAL NETWORKING APPLICATION


class Employee:
    # class attribute to track current number of employees
    employee_count = 0
    
    
    def __init__(self, name, email, hire_date):
        """
        Constructor method for Employee class
        Initializes an Employee object with name, email, and hire date. 
        Adjusts the employee_count class attribute when a new employee 
            is created. 
        """
        self.name = name
        self.email = email
        self.hire_date = hire_date
        Employee.employee_count += 1
        

class Post:

    #constructor
    def __init__(self, message, author):
        self.message = message
        self.author = author

        # initiates a list that holds comments on the post
        self.comments = []
    
    def edit_post(self, new_comment):
        self.message = new_comment