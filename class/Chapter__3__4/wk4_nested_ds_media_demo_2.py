# movies
son_movies = [
    {'title': 'Alien', 'year': 1979},
    {'title': 'Godzilla', 'year': 1954},
    {'title': 'Ghostbusters', 'year': 1984}
]

matrix = 'The Matrix'
demolition_man = 'Demolition Man'
my_cousin_vinny = 'My Cousin Vinny'
spouse_movies = [matrix, demolition_man, my_cousin_vinny]

fifth_element = 'The Fifth Element'
my_fair_lady = 'My Fair Lady'
starship_troopers = 'Starship Troopers'
my_movies = [fifth_element, my_fair_lady, starship_troopers]

# books
son_books = [
    {'title': 'Goosebumps', 'author': 'R.L. Stine'}
]

dune = 'Dune'
i_robot = 'I, Robot'
foundation = "Foundation"
spouse_books = [dune, i_robot, foundation]

ringworld = 'Ringworld'
sherlock = 'Collected works of Sherlock Holmes'
dickens = 'Collected works of Charles Dickens'
my_books = [ringworld, sherlock, dickens]


# games
son_games = [
    {'title': 'The Fast and the Furious', 'type': 'Card Game'},
    {'title': 'Jaws', 'type': 'Board Game'},
    {'title': 'Uno', 'type': 'Card Game'}
]

pax_pamir = 'Pax Pamir 2nd edition'
terraforming_mars = 'Terraforming Mars'
castles_of_burgundy = 'Castles of Burgundy'
spouse_games = [pax_pamir, terraforming_mars, castles_of_burgundy]

innovation = 'Innovation'
barenpark = 'Bärenpark'
spirit_island = 'Spirit Island'
my_games = [innovation, barenpark, spirit_island]

# combine collections
'''
household_collection
    └── son_collection
        ├── movies
        │   ├── alien
        │   ├── godzilla
        │   └── ghostbusters
        └── books
            └── goosebumps
'''
son_collection = {
    'movies': son_movies,
    'books': son_books,
    'games': son_games
}

spouse_collection = {
    'movies': spouse_movies,
    'books': spouse_books,
    'games': spouse_games
}

my_collection = {
    'movies': my_movies,
    'books': my_books,
    'games': my_games
}

house_collection = {
    'son_collection' : son_collection,
    'spouse_collection' : spouse_collection,
    'my_collection': my_collection
}

# Interaction
# Example operations with this structure:

# 1. Simple access - getting all of son's movies

# print(house_collection['son_collection'])

# print(house_collection['son_collection']['movies'][0])

# DETECTIVE WORK
# figure out where son's games are
# figure out the type of collection you are working with
# get the next data structure
# detective: we discovered the base was a dictionary so get the keys
# if it was a list, determine the length of the list and chose an index
print(type(house_collection), house_collection.keys())

# pick a key to learn more about the structure
sons_stuff = house_collection['son_collection']
print("son's collection", type(sons_stuff), sons_stuff.keys())

# dive deeper
# sons_games = sons_stuff['games'] # same as below
sons_games = house_collection['son_collection']['games']
print('son games', type(sons_games)) # this tells us it is a list
print('length', len(sons_games)) # with few items, feel safe displaying all of them

# display all the games
print(house_collection['son_collection']['games'])

# each game is a dictionary, so lets get just the titles
print("the games: --------")
for game in house_collection['son_collection']['games']:
    # print(game.keys()) # this tells me we have a title
    print(game['title'])