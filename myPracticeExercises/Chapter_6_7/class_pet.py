'''
Pet Class
'''

class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self):
        return 'Bark Bark'

    def pet_birthday(self):
        self.age += 1
        return self.age

    def show_details(self):
        '''
        Pet UML - The show_details() method returns a formatted 
        string like: "I have a 3 year old Dog named Buddy."
        '''
        return f'I have a {self.age} year old {self.species} named {self.name}'

sky = Pet('Sky', 'fish', 2)

print(sky.pet_birthday())
print(sky.show_details())
print(sky.make_sound())