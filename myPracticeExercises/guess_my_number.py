'''
#? Concepts Covered: Data Types and Casting, User Input, Conditionals and Loops, Basic String Formatting

#*              The Challenge:

❎ Generate a Secret Number: Your program should pick a "secret number" between 1 and 10. You can start by hardcoding this 
for now, e.g., secret_number = 7. Later, you can look into how to generate a random number.

❎ Get User's Guess: Prompt the user to guess the number.

#* Check the Guess:

❎ If the user's guess is correct, tell them "Congratulations! You guessed it!" and end the game.

❎ If the guess is too high, tell them "Too high! Try again."

❎ If the guess is too low, tell them "Too low! Try again."

#* Keep Going: 

Allow the user to keep guessing until they get it right.

Handle Invalid Input: What if the user types "hello" instead of a number? Your program should be able to tell them 
that's not a valid guess and ask them to try again, without crashing.

#* Hints for your approach:

How can you make sure the user's input, which starts as a string, can be compared to a number?

What kind of loop would be best when you don't know exactly how many guesses the user will take?

How can you check if the input is a number before trying to convert it? (Think about try-except blocks, or string methods).

'''

from random import randint

def guessing_game():
    secret_number = randint(1, 10)
    while True:
        try:
            users_guess = int(input('Guess the secret number between 1 - 10: '))
            if users_guess == secret_number:
                print('Congrats! You guessed it!')
                break
            elif users_guess > secret_number:
                print('Too high! Try again')
            else:
                print('Too low! Try again')
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 10')

guessing_game()