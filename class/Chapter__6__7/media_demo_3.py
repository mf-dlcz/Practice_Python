
household_collection = {
    "son_collection": {
        "movies": [
            {
                "title": "Alien",
                "director": "Ridley Scott",
                "year": 1979,
                "genre": "Sci-Fi Horror",
                "runtime": 117,  # in minutes
                "watched": True,
                "rating": 5
            },
            {
                "title": "Godzilla",
                "director": "Ishirō Honda",
                "year": 1954,
                "genre": "Monster",
                "runtime": 96,
                "watched": True,
                "rating": 4
            },
            {
                "title": "Ghostbusters",
                "director": "Ivan Reitman",
                "year": 1984,
                "genre": "Comedy",
                "runtime": 105,
                "watched": True,
                "rating": 5
            }
        ],
        "books": [
            {
                "title": "Goosebumps",
                "author": "R.L. Stine",
                "year": 1992,
                "genre": "Horror Fiction",
                "read": True,
                "rating": 4
            }
        ],
        "games": [
            {
                "title": "Fast & Furious: Highway Heist",
                "publisher": "Prospero Hall",
                "designer": "Aaron Donogh",
                "type": "Campaign Game",
                "min_players": 2,
                "max_players": 4,
                "playtime": 60,  # in minutes
                "rating": 7
            },
            {
                "title": "Jaws",
                "publisher": "Prospero Hall",
                "designer": "Brian Kirk",
                "type": "Board Game",
                "min_players": 2,
                "max_players": 4,
                "playtime": 60,
                "rating": 7
            },
            {
                "title": "Uno",
                "designer": "Merle Robbins",
                "type": "Card Game",
                "min_players": 2,
                "max_players": 10,
                "playtime": 30,
                "rating": 6
            }
        ]
    },
    "spouse_collection": {
        "movies": [
            {
                "title": "The Matrix",
                "director": "The Wachowskis",
                "year": 1999,
                "genre": "Sci-Fi",
                "runtime": 136,
                "watched": True,
                "rating": 5
            },
            {
                "title": "Demolition Man",
                "director": "Marco Brambilla",
                "year": 1993,
                "genre": "Action",
                "runtime": 115,
                "watched": True,
                "rating": 4
            },
            {
                "title": "My Cousin Vinny",
                "director": "Jonathan Lynn",
                "year": 1992,
                "genre": "Comedy",
                "runtime": 119,
                "watched": True,
                "rating": 5
            }
        ],
        "books": [
            {
                "title": "Dune",
                "author": "Frank Herbert",
                "year": 1965,
                "genre": "Science Fiction",
                "read": True,
                "rating": 5
            },
            {
                "title": "I, Robot",
                "author": "Isaac Asimov",
                "year": 1950,
                "genre": "Science Fiction",
                "read": True,
                "rating": 4
            },
            {
                "title": "Foundation",
                "author": "Isaac Asimov",
                "year": 1951,
                "genre": "Science Fiction",
                "read": False,
                "rating": None
            }
        ],
        "games": [
            {
                "title": "Pax Pamir 2nd edition",
                "designer": "Cole Wehrle",
                "publisher": "Wehrlegig Games",
                "type": "Strategy Board Game",
                "min_players": 1,
                "max_players": 5,
                "playtime": 120,
                "rating": 9
            },
            {
                "title": "Terraforming Mars",
                "designer": "Jacob Fryxelius",
                "publisher": "Stronghold Games",
                "type": "Strategy Board Game",
                "min_players": 1,
                "max_players": 5,
                "playtime": 120,
                "rating": 10
            },
            {
                "title": "Castles of Burgundy",
                "designer": "Stefan Feld",
                "publisher": "Alea Games",
                "type": "Strategy Board Game",
                "min_players": 2,
                "max_players": 4,
                "playtime": 90,
                "rating": 8
            }
        ]
    },
    "my_collection": {
        "movies": [
            {
                "title": "The Fifth Element",
                "director": "Luc Besson",
                "year": 1997,
                "genre": "Sci-Fi",
                "runtime": 126,
                "watched": True,
                "rating": 5
            },
            {
                "title": "My Fair Lady",
                "director": "George Cukor",
                "year": 1964,
                "genre": "Musical",
                "runtime": 170,
                "watched": True,
                "rating": 4
            },
            {
                "title": "Starship Troopers",
                "director": "Paul Verhoeven",
                "year": 1997,
                "genre": "Sci-Fi",
                "runtime": 129,
                "watched": True,
                "rating": 4
            }
        ],
        "books": [
            {
                "title": "Ringworld",
                "author": "Larry Niven",
                "year": 1970,
                "genre": "Science Fiction",
                "read": True,
                "rating": 5
            },
            {
                "title": "Collected works of Sherlock Holmes",
                "author": "Arthur Conan Doyle",
                "year": 1887,
                "genre": "Mystery",
                "read": True,
                "rating": 5
            },
            {
                "title": "Collected works of Charles Dickens",
                "author": "Charles Dickens",
                "year": 1850,
                "genre": "Classic Literature",
                "read": False,
                "rating": None
            }
        ],
        "games": [
            {
                "title": "Innovation",
                "designer": "Carl Chudyk",
                "publisher": "Asmadi Games",
                "type": "Card Game",
                "min_players": 2,
                "max_players": 4,
                "playtime": 60,
                "rating": 10
            },
            {
                "title": "Bärenpark",
                "designer": "Phil Walker-Harding",
                "publisher": "Lookout Games",
                "type": "Tile Placement Game",
                "min_players": 2,
                "max_players": 4,
                "playtime": 45,
                "rating": 10
            },
            {
                "title": "Spirit Island",
                "designer": "R. Eric Reuss",
                "publisher": "Greater Than Games",
                "type": "Cooperative Board Game",
                "min_players": 1,
                "max_players": 4,
                "playtime": 120,
                "rating": 10
            }
        ]
    }
}


'''
# Interaction
# 1. Print all the Sci-Fi movies in the household
print("All Sci-Fi Movies in the Household:")
for owner, collection in household_collection.items():
    if "movies" in collection:
        for movie in collection["movies"]:
            if "Sci-Fi" in movie.get("genre", ""):
                print(f"- {movie['title']} ({movie['year']}) owned by {owner.split('_')[0]}")

# 2. Find all favorite games across collections
print("\nFavorite Games in the Household:")
for owner, collection in household_collection.items():
    if "games" in collection:
        for game in collection["games"]:
            if game.get("favorite", False):
                owner_name = owner.split('_')[0]
                print(f"- {game['title']} ({game['type']}) - {owner_name}'s favorite")

# 3. Find all unread books
print("\nBooks Still to be Read:")
for owner, collection in household_collection.items():
    if "books" in collection:
        for book in collection["books"]:
            if not book.get("read", True):
                owner_name = owner.split('_')[0]
                print(f"- {book['title']} by {book['author']} (in {owner_name}'s collection)")

# 4. Show all Isaac Asimov books
print("\nIsaac Asimov Books:")
for owner, collection in household_collection.items():
    if "books" in collection:
        for book in collection["books"]:
            if book.get("author") == "Isaac Asimov":
                print(f"- {book['title']} ({book['year']}) - owned by {owner.split('_')[0]}")

# 5. Calculate the average rating for each collection
print("\nAverage Ratings by Collection:")
for owner, collection in household_collection.items():
    total_rating = 0
    rated_items = 0
    
    for media_type in ["movies", "books"]:
        if media_type in collection:
            for item in collection[media_type]:
                if item.get("rating") is not None:
                    total_rating += item["rating"]
                    rated_items += 1
    
    if rated_items > 0:
        avg_rating = total_rating / rated_items
        owner_name = owner.split('_')[0]
        print(f"{owner_name}'s collection: {avg_rating:.1f}/5 average rating ({rated_items} items rated)")

# 6. Find which collection has the most items
collection_counts = {}
for owner, collection in household_collection.items():
    total_items = sum(len(items) for items in collection.values())
    collection_counts[owner] = total_items

most_items_owner = max(collection_counts, key=collection_counts.get)
owner_name = most_items_owner.split('_')[0]
print(f"\nLargest Collection: {owner_name}'s with {collection_counts[most_items_owner]} items")
'''

'''
# Stage A: Simple Loops - One Level
print("\n=== Looping Through Collections ===")
print("All collections in the house:")
for collection_name in household_collection:
    print("-", collection_name)

# Stage B: Nested Loops - Two Levels
print("\n=== Nested Loops - Show Media Types ===")
print("Media types in each collection:")
for collection_name, collection in household_collection.items():
    print(f"\n{collection_name}:")
    for media_type in collection:
        print(f"- {media_type}")
        
# Stage C: Nested Loops - Three Levels
print("\n=== Nested Loops - Show All Items ===")
print("All items by collection and type:")
for collection_name, collection in household_collection.items():
    print(f"\n{collection_name}:")
    for media_type, items in collection.items():
        print(f"\n  {media_type}:")
        for item in items:
            print(f"    - {item}")
'''