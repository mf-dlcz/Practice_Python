#       EMPLOYEE SOCIAL NETWORKING APPLICATION

                                        # Employee class
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
        
        self.total_score = 0             # initializes a total_score variable to track points
        self.posts = []                  # initializes an empty list to hold all posts
        self.comments = []               # initializes an empty list to hold all comments

    # Creates a new post
    def post_message(self, message):
        post = Post(self, message)
        self.total_score += 5
        self.posts.append(post)
        return post

    # creates a new comment in a post
    def comment_on_post(self, message, post):
        comment = Comment(self, message, post)
        post.comments.append(comment)               # comment is added to the comments list
        self.comments.append(comment)               # appends comment to the employee object

                                        # Subclasses:
class Engineer(Employee):
    def __init__(self, name, email, hire_date):
        super().__init__(name, email, hire_date)
        self.department = 'engineering'


class Marketer(Employee):
    def __init__(self, name, email, hire_date):
        super().__init__(name, email, hire_date)
        self.department = 'marketing'

                                        # Post Class
class Post:

    #constructor
    def __init__(self, message, author):
        self.message = message
        self.author = author

        # initiates a list that holds comments on the post
        self.comments = []
    
    def edit_post(self, new_comment):
        self.message = new_comment

                                        # Comment class
class Comment:

    # Constructor
    def __init__(self, author, message, post):
        self.author = author
        self.message = message
        self.post = post

    def edit_message(self, new_message):
        self.message = new_message



"""
                                                            Testing:
"""
# create a new employee
e1 = Employee("Mary Major", "mary.major@example.com", "07/12/2021")
e2 = Employee("Pat Candella", "pat.candella@example.com", "12/1/2022")
engineer1 = Engineer('Michael Mike', 'michael.mike@example.com', '06/1/2023')
marketer1 = Marketer('Arisa Blank', 'arisa.blank@example.com', '08/15/22')

print(f'Name: {engineer1.name} Email: {engineer1.email} Hire Date: {engineer1.hire_date}')
print(f'Name: {marketer1.name} Email: {marketer1.email} Hire Date: {marketer1.hire_date}')

# print(f'EMPLOYEE COUNT: {Employee.employee_count}')

# Use the post message method to create new Post objects
intro_message = e2.post_message("Hi all! So excited to be joining the company!")
engineer1_message = engineer1.post_message(f"Hi, My name is {engineer1.name} I'm super excited to be here!")
marketer1_message = marketer1.post_message(f"Hi, I'm {marketer1.name} It's a pleasure to meet you all!")

print(engineer1.total_score)
print(marketer1.total_score)


# Use the returned post to comment on the message
e1.comment_on_post("Welcome to the team!", intro_message)
e2.comment_on_post("Thanks!", intro_message)


# Another example of a new post with comment exchange
workshop_post = e1.post_message("I just attended a workshop.")

e2.comment_on_post("Cool! What was the workshop about?", workshop_post)
e1.comment_on_post("Python classes and objects", workshop_post)

print ("Mary's posts are",[post.message for post in e1.posts])
print ("Pat's posts are", [post.message for post in e2.posts])

print ("-" * 50)

print ("Mary's comments are",[comment.message for comment in e1.comments])
print ("Pat's comments are",[comment.message for comment in e2.comments])

print ("-" * 50)

print ("Intro message comments are",[comment.message for comment in intro_message.comments])
print ("Workshop post comments are", [comment.message for comment in workshop_post.comments])