#Exercise 1: Guessing Game

secret_number = 20
guess = 0
# Can I validate the input is a number before I do my comparison?

# as long as the guess not same as the secret number, user gets another chance
while guess != secret_number:
    guess = input("Enter your guess: ")
    guess = int(guess)
    if guess==secret_number:
        print("You guessed correctly!")
    elif guess>secret_number:
        print("Your guess is too high!")
    elif guess<secret_number:
        print("Your guess is too low!")


# Exercise 2:
'''
Get user input for numbers continuosly until 'quit'
Compute the average of these numbers.
Find the manimum and minimum 
'''