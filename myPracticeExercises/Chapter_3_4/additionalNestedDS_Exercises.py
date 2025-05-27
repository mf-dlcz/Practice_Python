"""
ADDITIONAL EXERCISES TO PRACTICE NESTED
DATA STRUCTURES:
"""

#       EXERCISE #1:    ANALYZING BOOKSTORE INVENTORY

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




#   ##############################################       EXERCISE #2:   User Activity Analysis

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
    total = 0
    
    # accessing the playlist key within users & storing it in user_playlist
    user_playlist = user['playlists']

    for playlist in user_playlist:
        song = playlist['songs']
        total += len(song)

    #creating a new key, value pair to store the total songs of each list of dictionaries
    user['total_songs_listened'] = total
# print(json.dumps(users, indent = 4))


#   ##########################################       EXERCISE #3:   Calculating Total Oder Value

customer_orders = [
    {
        'order_id': 'O1001',
        'customer_name': 'Alice Smith',
        'items': [
            {'product_name': 'Laptop', 'price': 1200.00, 'quantity': 1},
            {'product_name': 'Mouse', 'price': 25.50, 'quantity': 2}
        ]
    },
    {
        'order_id': 'O1002',
        'customer_name': 'Bob Johnson',
        'items': [
            {'product_name': 'Keyboard', 'price': 75.00, 'quantity': 1},
            {'product_name': 'Monitor', 'price': 300.00, 'quantity': 1},
            {'product_name': 'Webcam', 'price': 49.99, 'quantity': 1}
        ]
    },
    {
        'order_id': 'O1003',
        'customer_name': 'Charlie Brown',
        'items': [
            {'product_name': 'Headphones', 'price': 99.99, 'quantity': 2}
        ]
    }
] 

"""             Goal:
For each order in the customer_orders list, you need to:
- Calculate the total value of that order. This means summing 
up (price * quantity) for every item in that order.
- Add a new key-value pair to each order's dictionary: 'total_order_value' 
with the calculated total (rounded to two decimal places, as it's currency).
"""