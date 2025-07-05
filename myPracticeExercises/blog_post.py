'''
#? Concepts Covered: Object Notation, Creating Unique Objects, Class Inheritance, Creating Custom Methods, 
#? Association, Working with Modules, Script, Writing Log Files, Logging Exceptions, Writing Unit Tests 
#? (for functions and classes)

#*              The Challenge:

This one is a bit more involved, but it ties together a lot of the object-oriented concepts!

#* Post Class:

Create a base class called Post.

❎ It should have attributes like title (string), content (string), and author (string).

❎ Include a method display_post() that prints the post's title, author, and content in a readable format.

❎ Add a method to generate a unique post_id (perhaps using a simple counter or a module like uuid for more robust IDs).

#* BlogPost Class (Inheritance):

❎ Create a class BlogPost that inherits from Post.

❎ BlogPost should have an additional attribute: tags (a list of strings).

❎ Override the display_post() method to also show the tags.

#* Comment Class (Association):

Create a Comment class with author (string) and text (string) attributes.

A BlogPost should be able to have multiple Comment objects associated with it. How will you store these comments 
within a BlogPost instance?

Add a method to BlogPost called add_comment() that takes a Comment object as an argument and adds it to the post's 
comments.

Modify display_post() to also display all associated comments.

#* Logging:

Whenever a new Post or Comment is created, or an error occurs (e.g., trying to add a comment to a non-existent 
post if you were to expand this), write a log entry to a file named blog_log.txt.

Include timestamps in your log entries.

Use the logging module for this, and ensure you also practice logging exceptions.

#* Unit Tests:

Once you've built your classes and methods, write a few unit tests for them.

For example, test that a Post object is created correctly, that BlogPost inherits properly, that add_comment works, 
and that average grade calculation is accurate if you were to combine this with the previous project.

You can use Python's built-in unittest module or simply assert statements to check expected behavior.

#* Hints for your approach:

For logging, import logging and configure it to write to a file.

Think about how to store multiple Comment objects within a BlogPost instance (a list of Comment objects is a 
good approach). This demonstrates association.

For unit tests, think about the "happy path" (things working as expected) and "edge cases" (e.g., empty lists, 
invalid input).
'''

import logging
import uuid

# Configure logging
logging.basicConfig(
    filename='blog_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.post_id = self.generate_post_id()
        logging.info(f"Post created: '{self.title}' by {self.author}")

    def display_post(self):
        return f'''
            Title: {self.title}
            Content: {self.content}
            Author: {self.author}
            Post ID: {self.post_id}
        '''

    def generate_post_id(self):
        return str(uuid.uuid4())

class BlogPost(Post):
    def __init__(self, tags):
        self.tags = []

    def display_post(self):
        return f'Tags: {self.tags}'

class Comment(Post):
    