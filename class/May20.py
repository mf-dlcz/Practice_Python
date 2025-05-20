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











# Parent Class
class Shape:

    def __init__(self, color):
        self.color = color

    
    def calc_area(self):
        pass

    def get_color(self):
        print(self.color)

# inheritance class
class Rectangle(Shape):

    def __init__(self, color, width, height):
        # call parents init
        # with super, we don't need self
        super().__init__(color)
        self.width = width
        self.height = height

    # overrides the behavior of the parent class
    def cal_area(self):
        return self.width * self.height


class Circle(Shape):
    
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def cal_area(self):
        return 3.14 * self.radius * self.radius

# create a rectangle object
rec1 = Rectangle("Turquoise", 5, 2)
rec1.get_color()
area = rec1.cal_area()
print(f"The area of the rectabgle is {area}")


# creates a circle object
circle1 = Circle("Grey", 4)
circle1.get_color()
circle_area = circle1.calc_area()
print("The area of the circle is ", circle_area)