class Pet:

    def __init__(self, name, animal_type, age, checked_in):
        self.name = name
        self.age = age
        self.animal_type = animal_type
        self.checked_in = checked_in
        self.happiness = 50
#   ###### Task 2   #######
"""
Display the pet's information in two ways:
    A detailed technical 
""
    def ___repr__(self):
"""
    Gives back a valid Python expression that can be used to
    recreate the object itself. Suitable for developers, for
    debugging purposes.
"""
        return f"Pet(name = "{self.name}", animal_type = {self.animal_type}, age = {self.age}, checked_in = {self.checked_in})"


#   ########## Create an object     ##########

my_pet = Pet("Misty", "dog", 4, False)
print(my_pet.happiness)

my_pet.checked_in = True
print(my_pet.checked_in)

