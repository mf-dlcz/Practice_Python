class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


    def get_info(self):
        '''
        Book UML - Make the get_info() method return a nice formatted string 
        like: "Python Programming by Dr. K has 200 pages
        '''
        return f'\n{self.title} by {self.author} has {self.pages} pages.\n'

my_book = Book('Python Programming', 'Dr.K', 200)

print(my_book.get_info())