# Virtual Pet Programming Guide 📝
## Function Creation Instructions

### 1. Welcome Message Function
def welcome_message():
    """
    Purpose: Display the initial welcome message for the game
    Input: None
    Output: None (just prints messages)
    
    Instructions:
    1. Use print() to show a welcome message
    2. Add a second print() for one line game description
    """
    print("\n\tWelcome to the Virtual Pet Game!")
    print("Take care of your virtual pet & have fun!")

### 2. Create Pet Function
def create_pet():
    """
    Purpose: Get the pet's name from the user
    Input: None
    Output: Returns a string (the pet's name)
    
    Instructions:
    1. Use input() to ask for pet's name
    2. Store name in a variable
    3. Return the name variable
    
    Example:
    If user enters "Fluffy", function should return "Fluffy"
    """
    name = input("\nEnter your pet's name: ")
    return name

### 3. Feed Pet Function
def feed_pet(name, hunger):
    """
    Purpose: Feed the pet and update hunger level
    Input: 
        - name (string): pet's name
        - hunger (integer): current hunger level (0-100)
    Output: Returns new hunger level (integer)
    
    Instructions:
    1. Check if hunger is less than 80
    2. If hungry (< 80):
       - Print message that pet is eating
       - Decrease hunger by 30
    3. If not hungry (>= 80):
       - Print message that pet isn't hungry
    4. Return the new hunger value
    
    Example:
    feed_pet("Fluffy", 60) should:
    - Print that Fluffy is eating
    - Return 30 (60 - 30)
    """
    if hunger < 80:
        print(f"{name} is hungry and eating...")
    elif hunger >= 80:
        print(f"{name} is not hungry")
    return hunger - 30

### 4. Pet Nap Function
def pet_nap(name, sleep):
    """
    Purpose: Manage pet's sleep state
    Input:
        - name (string): pet's name
        - sleep (boolean): True if pet needs sleep, False if not
    Output: Returns new sleep state (boolean)
    
    Instructions:
    1. Check if sleep is True
    2. If True:
       - Print message about pet taking a nap
       - Change sleep to False
    3. If False:
       - Print message that pet isn't tired
    4. Return the new sleep value
    
    Example:
    pet_nap("Fluffy", True) should:
    - Print that Fluffy is taking a nap
    - Return False
    """
    if sleep == True:
        print(f"SSHHH.... {name} is sleepy and needs to take a nap.")
        sleep = False
    else:
        print(f"{name} rests for a while, but {name} isn't tired.")
    return sleep

### 5. Pet Shower Function
def pet_shower(name, shower):
    """
    Purpose: Manage pet's cleanliness
    Input:
        - name (string): pet's name
        - shower (boolean): True if pet needs shower, False if clean
    Output: Returns new shower state (boolean)
    
    Instructions:
    1. Check if shower is True
    2. If True:
       - Print message about pet getting clean
       - Change shower to False
    3. If False:
       - Print message about pet avoiding shower
    4. Return the new shower value
    
    Example:
    pet_shower("Fluffy", True) should:
    - Print that Fluffy is getting clean
    - Return False
    """
    if shower == True:
        print(f"{name} is showering")
        shower == False
    elif shower == False:
        print(f"{name} doesn't need to shower")
    return shower

#### main part of the program starts here #####

#Task 1: Create a simple welcome message function that introduces the game.
welcome_message()

##Task2: Create a function that asks for and returns the pet's name.
pet_name = create_pet()

print(f"\n{pet_name} is a beautiful name!")

#Initialize pet variables
pet_sleepy = True
# How it works:
# - Uses True/False (Boolean) values
# - True means your pet needs sleep
# - False means your pet is well-rested

pet_dirty = False
# How it works:
# - Uses True/False (Boolean) values
# - True means your pet needs a shower
# - False means your pet is clean

pet_hunger = 60
# How it works:
# - Goes from 0 to 100
# - Higher numbers mean your pet is less hungry
# - Lower numbers mean your pet needs food

print("\nWhat would you like to do with your pet?")
print("1. \U0001F355 Feed your pet")
print("2. \U0001F4A4 Let your pet rest.")
print("3. \u2668 Give your pet a shower.")
print("4. \u274C EXIT THE GAME")

user_action = input("Enter your choice: ")

#### TO-DO #####
# Based on user's input, call the appropriate function

if user_action == "1":
    pet_hunger = feed_pet(pet_name, pet_hunger)
elif user_action == "2":
    pet_sleepy = pet_nap(pet_name, pet_sleepy)
elif user_action == "3":
    pet_dirty = pet_shower(pet_name, pet_dirty)
elif user_action == "4":
    print("Ciao")