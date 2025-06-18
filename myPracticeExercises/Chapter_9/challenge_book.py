import json

class Book:
    # 1. Define a Python class called Book with the attributes title and author.
    def __init__(self, title, author):
        self.title = title
        self.author = author

# 2. Create an instance of the class with the title and author of your favorite book.
my_book = Book('Romeo and Juliet', "Shakespeare")

'''
3.  Use json.dumps() to convert the attributes of the Book instance (object) to a JSON string. 
NOTE: You can either define a dictionary manually or using a special method. In addition, 
json.dumps() wont work if you pass it an object type. It only works on these data types: 
dict, list, tuple, string, int, float, True, False, None. You will need to convert the book 
object to a dict in this case.

4.  Format the string with four spaces of indentation and a colon followed by a space as the separator between keys and values.
'''
json_string = json.dumps({"title": my_book.title, "author": my_book.author}, indent = 4, separators = (", ", ": "))

print(json_string)


'''
                    SOLUTION 2:

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

#create a book instance
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")

# convert the book instance to a JSON string with indentation and custom parameters
book1_json = json.dumps(book1.__dict__, indent=4, separators=(",",": "))

# print the JSON string
print(book1_json)
'''