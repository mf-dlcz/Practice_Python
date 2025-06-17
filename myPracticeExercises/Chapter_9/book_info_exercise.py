import json

# 1. Define a Python dictionary: Create a dictionary named 'book_info'
#    with at least three key-value pairs representing a book's information.
#    (e.g., title, author, publication_year).
book_info = {
    "Author": "William Shakespeare",
    "Title": "Hamlet",
    "Pages": 432,
    "Genre": "Revenge Tragedy"
}

# 2. Convert to JSON: Use the 'json' module to convert your 'book_info'
#    dictionary into a JSON string. Store this string in a variable called 'json_book'.
json_book = "" # This will hold your JSON string
json_book = json.dumps(book_info)

# 3. Print the result: Display the 'json_book' string.
# print(json_book) # Uncomment this line when you're ready to print

print(type(json_book))