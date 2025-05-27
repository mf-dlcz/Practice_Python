class Pet:
    
    def __init__(self, name):
        self.name = name
        self.age = 1
        
pet1 = Pet("Fluffy")

#vars() function
print(vars(pet1)) #returns the dictionary that stores the object's data attributes
