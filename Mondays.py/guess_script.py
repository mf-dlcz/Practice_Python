import guess

print('Welcome to the Guessing Game!')

user_choice = int(input('Guess a number to start playing:' ))

# game over = guess.game(user_choice)

game_over = False

while game_over == False:
    user_choice = int(input('Guess a number: '))
    game_over = guess.game(user_choice)