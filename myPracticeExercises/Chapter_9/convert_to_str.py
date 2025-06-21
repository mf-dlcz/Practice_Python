'''
Exercise: Converting a dict into a JSON string.
'''
import json

data = {
    "book_title": "The Hitchhiker's Guide to the Galaxy",
    "author": "Douglas Adams",
    "year_published": 1979,
    "genre": "Science Fiction Comedy",
    "characters": ["Arthur Dent", "Ford Prefect", "Zaphod Beeblebrox", "Marvin"],
    "is_available": True,
    "details": {
        "pages": 193,
        "publisher": "Pan Books",
        "isbn": "0-345-39180-2"
    }
}

# Converting a dictionary into a python string
json_str = json.dumps(data, indent = 4)

print(json_str)

# with open() data