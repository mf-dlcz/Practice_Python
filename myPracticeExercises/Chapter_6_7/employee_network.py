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
        
        # initates an empty list to hold all posts
        self.posts = []

    def post_message(self, message):
        post = Post(self, message)
        self.posts.append(post)
        return post

class Post:

    #constructor
    def __init__(self, message, author):
        self.message = message
        self.author = author

        # initiates a list that holds comments on the post
        self.comments = []
    
    def edit_post(self, new_comment):
        self.message = new_comment


"""
Testing my classes
"""
# create a new employee
e1 = Employee("Mary Major", "mary.major@example.com", "07/12/2021")

# Use the post message method to create new Post objects
e1.post_message("hello")

# Capture the function return in a variable so you can reference the Post
second_post = e1.post_message("second message")

# Use the edit message method from the Post class to edit the message
second_post.edit_post("edited message")

# Check post to see that it includes the Employee as author
print (second_post.author.name)

# Use a list comprehension to print each message on the Employee's posts list. 
print ([post.message for post in e1.posts])