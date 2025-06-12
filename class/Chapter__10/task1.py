import logging
import random

# TODO: Set up logging configuration here

def choose_path():
    # TODO: Implement this function
    # It should:
    # 1. Ask the player to choose path 1 or 2
    # 2. Handle invalid inputs using try/except
    # 3. Return the chosen path number
    pass

def adventure():
    print("Welcome to the Mini Adventure!")
    # TODO: Log that the adventure has started

    print("You're standing at a fork in the road.")
    # TODO: Get player's choice using choose_path()
    # TODO: Log the player's choice
        
    # TODO: Implement what happens on path 1
    # If path 1 is chosen:
        # use random.random() to generate a floating point number
        #   - 50% chance to find treasure
        #   - 50% chance to get lost
    # Remember to log what happens!
        
    # TODO: Implement what happens on path 2
    # If path 2 is chosen:
        # use random.random() to generate a floating point number
        #   - 50% chance to find village
        #   - 50% chance bridge collapses
    # Remember to log what happens!

    print("Thanks for playing!")
    # TODO: Log that the adventure has ended

# TODO: Implement error handling
# Hint: Use a try/except block around the main game logic in adventure()
# to catch and handle any unexpected errors
# Remember to log any errors that occur