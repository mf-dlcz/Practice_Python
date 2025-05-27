'''
Library Management System
Create a simple library management system to manage books and their borrowing status.

Create two classes:
A library class to manage the collection of books
A book class to represent individual books

The book class should:
Have attributes for:
title
author
ISBN
borrowing status
borrower name
Be initialized with title, author, and ISBN

The library class should:
Maintain a list of books
Keep track of total books and borrowed books
Include the following methods:
add_book(book_object): Adds a new book to the library (prevent duplicates)
remove_book(title_book): Removes a book from the library
borrow_book(title, borrower_name): Marks a book as borrowed
return_book(title): Marks a book as returned
'''

class book:
    
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.borrower_name = None
        
class Library:
    
    def __init__(self):
        self.books = []
        self.total_books = 0
        self.borrowed_books = 0
        
    def add_book(self, book_object):
        if book_object in self.books:
            print("Book already exixts in the Library")
        else:
            self.books.append(book_object)
            self.total_books = self.total_books + 1

    def remove_book(self, title_book):
        if title_book in self.books:
            title_book.remove()

    def borrow_book(self, booktitle, borrower):
        #should check if the title of the book exists
        #if book title does not exist, return Book not found
        #if it exists, check if book is borrowed
            #if book is borrowed, return Book is already borrowed by someone else
            #if not, mark it borrowed, and update borrower name
            #return Book borrowed.
        for each_book in self.books:
            if each_book.title == booktitle:
                if each_book.is_borrowed:
                    return f"Book is already borrowed by {each_book.borrower_name}"
                else:
                    each_book.is_borrowed = True
                    each_book.borrower_name = borrower
                    self.borrowed_books = self.borrowed_books+1
                    return "Book is now borrowed"
        return "Book not found"            
        
    def return_book(self, booktitle):
        pass
            
#create book objects
book1 = book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
book2 = book("To Kill a Mockingbird", "Harper Lee", "9780446310789")

# print(book1.author)
# print(book2.is_borrowed)
#create a library object
library_object = Library()
library_object.add_book(book1)
library_object.add_book(book2)
# print(library_object.books)

# for each_book in library_object.books:
#     print(each_book.isbn)
#     print(each_book.is_borrowed)

print(library_object.borrow_book("To Kill a Mockingbird", "Dr.K"))
print(library_object.borrow_book("Atomic Habits", "Maria"))
print(library_object.remove_book("To Kill a Mockingbird"))
print(book2.is_borrowed, book2.borrower_name)
# print(library_object.borrow_book("To Kill a Mockingbird", "Dr.K"))

print(library_object.borrow_book("The Wizard of Oz", "Dr.K"))