# Class - a template/blueprint with attributes(data/characteristics), and methods(behavior/actions)
# class Dog:
    #class attributes - belong to the class, and are commonly shared by all objects
    # name = 'Peppah'
    # age = 3
    # breed = "Pomeranian" 
    
    #create instance attributes
    #every method inside a class must have self as the first parameter
    # def __init__(self, name, age, breed):
    #     self.name = name
    #     self.age = age
    #     self.breed = breed
    
    # def bark(self):
    #     print(f"{self.name} says 'Woof! Woof!")
    
#Objects - always comes after class definition
#creating an object(instance of a class) - Instantiation
#object_name = classname() #default constructor
#when init exists, the Dog() expects to receive values for the paramaters in init
#we do not send a value for self variable
# dog_one = Dog("Peppah", 3, "Pomeranian")

# #accessing atributes - dot notation
# print("This is my dog's name: ", dog_one.name)
# print(f"He is a {dog_one.age} year old {dog_one.breed}")

# dog_one.bark()

# dog_two = Dog("Turing", 8, "Brazilian Hound")
# print("This is Clayton's dog's name: ", dog_two.name)
# print(f"He is a {dog_two.age} year old {dog_two.breed}")




# ### Exercise 2:
class Car:
    
    def __init__(self, color, miles):
        self.color = color
        self.miles = miles
        
    def move_forward(self, num_miles):
        self.miles = self.miles + num_miles
        
### creating objects

newcar = Car("Blue", 1034)

print(newcar.color)
print(newcar.miles)

newcar.move_forward(190)
print(newcar.miles)

print(newcar)