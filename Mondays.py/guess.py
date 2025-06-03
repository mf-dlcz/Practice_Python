import random

secret_number = random.randint(1, 100)

def game(guess):

    

    if guess == secret_number :
        print('Success! You have guessed the number!')
        return True
    elif( guess < secret_number ) :
        print('Your guess is too low')
        return False
    elif( guess > secret_number ) :
        print('Guess is too high!')
        return False
    else:
        print('Invalid input, please try again!')
        return False