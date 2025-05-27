# Review create, add, retrieve in lists and dictionaries

#Lists
alien = 'Alien'
godzilla = 'Godzilla'
ghostbusters = 'Ghostbusters'
movies = [alien, godzilla, ghostbusters, "The Avengers"]
# print(movies[0])
# movies.append('The Matrix')
# print(movies)

# for <temp_variable> in <collection>:
# for movie in movies:
#     print(movie)

ledger = [1234,1234,4312,145,642, 5432, 67534, 4578, 785, 1234]
# for number in range(len(ledger)):
#     print(f'Ledger line {number+1} - {ledger[number]}')
# for index, value in enumerate(ledger):
#     print(f'Ledger line {index+1} - {value}')


#Dictionaries
catan = { 'title': 'Catan', 'designer': 'Klaus Teuber', 'publisher': 'Kosmos', 'year': 1995, 'playtime': 60 }

# print(catan['title'])
# print(catan['owned']) # if key does not exist this will give a KeyError
# print(catan.get('owned'))
# how to manage the error in key lookup
# if 'owned' in catan:
#     print(catan['owned'])
# else:
#     print('key not in dictionary')
# catan['players'] = range(2,5)


# first pass at nesting
catan = { 'title': 'Catan', 'designer': 'Klaus Teuber', 'publisher': 'Kosmos', 'year': 1995, 'playtime': 60 }
ticket_to_ride = { 'title': 'Ticket to Ride', 'designer': 'Alan R. Moon', 'publisher': 'Days of Wonder', 'year': 2004, 'playtime': 45}
carcassonne = { 'title': 'Carcassonne', 'designer': 'Klaus-Jürgen Wrede', 'publisher': 'Hans im Glück', 'year': 2000, 'playtime': 30 }

games = [catan, ticket_to_ride, carcassonne]
# print(games)
# print(games[1])
# print(games[1]['playtime'])
# print(len(games))

total_time = 0
for game in games:
    # print(type(game))
    pt = game['playtime']
    total_time = total_time + pt    # total_time += pt
print(f'Total time: {total_time} minutes for {len(games)} games.')