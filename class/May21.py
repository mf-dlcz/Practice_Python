"""
Car Association:
"""

class PowerPlant:
    def refuel(self, amount):
        pass
    
    def get_fuel_level(self):
        pass
    
class ICE_Engine(PowerPlant):
    def __init__(self, tank_capacity=10):
        super().__init__()
        self.tank_capacity = tank_capacity
        self.fuel_level = 0
    def refuel(self, gallons):
        self.fuel_level += gallons
        
class EV_Battery(PowerPlant):
    def __init__(self, battery_capacity=80):
        super().__init__()
        self.battery_capacity = battery_capacity
        self.charge_level = 0
        
    def refuel(self, kwh):
        self.battery_level = kwh
        
class Car:    
    def __init__(self, color, make, year, powerplant=None):
        self.color = color
        self.make = make
        self.year = year
        self.miles_traveled = 0 #default value for an instance attribute
        self.powerplant = powerplant
        
    def move_forward(self, miles):
        self.miles_traveled = self.miles_traveled + miles
        
    def fill_gas(self):
        print("Filling gas...will take about 5 minutes.")
        
    def read_miles(self):
        return f"This car has {self.miles_traveled} miles on it."
        
    def info(self):
        return f"This is a {self.year} {self.color} {self.make} with {self.miles_traveled} miles on it."
    
 
 
ice_engine = ICE_Engine(12)
ice_car = Car("Blue", "Ford", 2024, ice_engine)
print(ice_car.info())

ev_engine = EV_Battery(110)
ev_car = Car("Silver", "Nissan", 2015, ev_engine)
print(ev_car.info())

# my_ec = Electric("White", "T", 2025, 80)    
# my_ec.move_forward(1982)
# print(my_ec.miles_traveled)
# my_ec.fill_gas()
# #self automatically receives car object information
# # car1 = Car("Blue", "Ford", 1952)
# # car1.fill_gas()
# # #accessing a class attribute
# # # print(Car.miles_traveled)

# # car1.move_forward(569)
# # car1.move_forward(41)

# # car1.fill_gas()
# # print(car1.read_miles())
# print(my_ec.info())