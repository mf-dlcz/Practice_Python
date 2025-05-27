#                                   Function Definitions:

def feed_animals():
    food = "bananas"
    print(f"Feeding animals {food} at {zoo_name}")

def rename_zoo():
    global zoo_name
    zoo_name = "AWS Cloud Institute Zoo"
    print("Inside the function!")
    print("Almost done!")
   
#global variable
zoo_name = input("Enter a name for the Zoo: ")

print(f"Welcome to {zoo_name}!")
feed_animals()
rename_zoo() 
print("The zoo has been renamed to: ", zoo_name)

print("End of zoo exercise!")


#                                     SCOOP EXAMPLE:
def my_function():
    global x
    x = 20
    print("Inside the function, x has a value: ", x)

x = 10

my_function()
print(x)


#                                     Superhero Academy: Parameters and arguments

#parameters - placeholders in the function definition
def greeting(hero_name, power):
    print(f"Hi!, I am {hero_name} and my power is {power}!")
    
#send arguments in the function call
#hero = input("Enter a name for the hero: ")
#greeting("whiteboarding", hero)   #positional arguments - order matters 

#keyword arguments - order does not matter!
# greeting(power = "experimenting", hero_name = "Dr. Data")

#default values for parameters
def equip_hero(name='Captain Python', costume = 'cape', mask = True):
    print(f"{name} is wearing a {costume}, and has a mask - {mask}")
    
equip_hero()
equip_hero("CodeMan", "No cape")