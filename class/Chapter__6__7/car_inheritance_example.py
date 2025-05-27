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
        return f"This car has {self.miles_traveled} miles on it."
        
    def info(self):
        return f"This is a {self.year} {self.color} {self.make} with {self.miles_traveled} miles on it."
    
#syntax for inheritance
class Electric(Car):
    
    def __init__(self, color, make, year, battery):
        #Car.__init__(self, color, make, year)
        #alternate to using the parent class name
        super().__init__(color, make, year)
        self.battery = battery

    #overriding methods - same method name as parent, different behavior
    def fill_gas(self):
        print("I am an electric car and will not need to fill gas.")

my_ec = Electric("White", "T", 2025, 80)    

my_ec.move_forward(1982)
print(my_ec.miles_traveled)
my_ec.fill_gas()
#self automatically receives car object information
# car1 = Car("Blue", "Ford", 1952)
# car1.fill_gas()
# #accessing a class attribute
# # print(Car.miles_traveled)

# car1.move_forward(569)
# car1.move_forward(41)

# car1.fill_gas()
# print(car1.read_miles())
# # print(car1.info())