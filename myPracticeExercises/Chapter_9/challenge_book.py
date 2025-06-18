import json

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def json_string(self):
        books = {}
        json_str = ''
        json_str = json.dumps()
        return json_str


my_book = Book('Romeo and Juliet', "Shakespeare")

