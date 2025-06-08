#       Class Dog

class Dog:
    def __init__(self, name: str, age: int, breed: str):
        self.name = name
        self.age = age
        self.breed = breed
    
    def bark(self):
        return f'{self.name} is barking'

    def sit(self):
        return f'{self.name} sat down'

    def print_info(self):
        return f'\nName: {self.name} \nAge: {self.age} \nBreed: {self.breed}'

Trixie = Dog('Trixie', 2, 'Rottweiler')
Spot = Dog('Spot', 3, 'Husky')


print(Trixie.bark())
print(Trixie.sit())
print(Spot.bark())
print(Spot.sit())

print(Trixie.print_info())
print(Spot.print_info())
