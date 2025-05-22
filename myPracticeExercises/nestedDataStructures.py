import json

"""
Nested Data Structures
"""

employees = [
    {"name": "John","age": 35,"position": "Manager", "department": "Sales"},
    {"name": "Ana","age": 28,"position": "Engineer", "department": "IT"},
    {"name": "Carlos", "age": 42, "position": "Director",
        "department": "Operations"}
]

# for emp in employees:
#     print (f'{emp["name"]} is in the {emp["department"]} department.')

#       EXAMPLE: using a for loop to iterate
# for emp in employees:
#     print(f"{emp['name']} is {emp['age']} years old.")


#   #########################################                   LISTS OF DICTIONARIES WITH LISTS:
"""
- Dictionaries can hold any type of data.
To access a list one can use indexing or a loop.
"""

students = [
    {'name': 'Alice', 'age': 20, 'grades': [90, 85, 95]},
    {'name': 'Bob', 'age': 21, 'grades': [80, 75, 70]},
    {'name': 'Charlie', 'age': 19, 'grades': [95, 90, 92]},
]

# for student in students:
#     # grades holds the grades list for the loop's current iteration
#     grades = student['grades']

#     # This line calculates the average value of the numbers in grades using Python’s built-in sum and len functions.
#     avg_grade = sum(grades) / len(grades)

#     # creates a new key-value for each student
#     student['avg_grade'] = round(avg_grade,2)

# print (students)


#       EXERCISE #2:

books = [
    {
        'title': 'The Hitchhiker\'s Guide to the Galaxy',
        'author': 'Douglas Adams',
        'genres': ['Science Fiction', 'Comedy'],
        'reviews': [5, 4, 5, 4, 5]
    },
    {
        'title': 'Pride and Prejudice',
        'author': 'Jane Austen',
        'genres': ['Romance', 'Classic'],
        'reviews': [5, 5, 4, 5, 4]
    },
    {
        'title': '1984',
        'author': 'George Orwell',
        'genres': ['Dystopian', 'Science Fiction'],
        'reviews': [4, 5, 4, 4, 5]
    },
    {
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'genres': ['Classic', 'Fiction'],
        'reviews': [5, 5, 5, 5, 5]
    }
]

#       GOAL:
"""
- Calculate the average review score.
- Add a new key-value pair to each book's dictionary: 'average_review' 
with the calculated average review score (rounded to two decimal places).
"""

# access the key reviews using a for loop
# loops through each key in the books dictionary
# for book in books:
#     key = book["reviews"]

#     average_review = sum(key) / len(key)

#     book["average_review"] = round(average_review, 2)
# print(json.dumps(books, indent = 4))




#       EXERCISE #3:    

users = [
    {
        'username': 'music_lover_1',
        'email': 'user1@example.com',
        'playlists': [
            {'name': 'Chill Vibes', 'songs': ['Song A', 'Song B', 'Song C']},
            {'name': 'Workout Jams', 'songs': ['Song D', 'Song E']}
        ]
    },
    {
        'username': 'indie_fan',
        'email': 'user2@example.com',
        'playlists': [
            {'name': 'New Discoveries', 'songs': ['Song F', 'Song G', 'Song H', 'Song I']}
        ]
    },
    {
        'username': 'rock_n_roller',
        'email': 'user3@example.com',
        'playlists': [
            {'name': '80s Rock', 'songs': ['Song J', 'Song K']},
            {'name': 'Classic Anthems', 'songs': ['Song L', 'Song M', 'Song N']}
        ]
    }
]

"""         GOAL:
- Calculate the total number of songs across all their playlists.
- Add a new key-value pair to each user's dictionary: 'total_songs_listened' 
with the calculated count.
"""

for user in users:

    # accessing the playlist key within users & storing it in user_playlist
    user_playlist = user['playlists']

    for playlist in user_playlist:
        song = playlist['songs']
        total = len(song)
    print(total)