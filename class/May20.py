"""
Inheritance: OOP
"""

class Car:
    #class attribute
    # miles_traveled = 0
    
    def __init__(self, color, make, year):
        self.color = color
        self.make = make
        self.year = year
        self.miles_traveled = 0 #default value for an instance attribute
        
    def move_forward(self, miles):
        self.miles_traveled = self.miles_traveled + miles
        
    def fill_gas(self):
        print("Filling gas...will take about 5 minutes.")
        
    def read_miles(self):
        return f"This car has {self.miles_traveled} miles on it"

    def info(self):
        return f"This is a {self.year} {self.color} {self.make} with {self.miles_traveled} miles on it."
    

# syntax for inheritance
class Electric(Car):

    def __init__(self, color, make, year, battery):
        # Car.__init__(self, color, make, year)
        # alternate to using the parent class name
        super().__init__(color, make, year)
        self.battery = battery
    
    #overriding method:
    def fill_gas(self):
        print("I'm an electric car. I don't need gas!")




my_elec = Electric("White", "T", 2025, 80)
my_elec.fill_gas()


# Creates an object named car1 with attributes
car1 = Car("Black", "Lexus", 2020)

car1.move_forward(1140)
car1.fill_gas()
print(car1.read_miles())