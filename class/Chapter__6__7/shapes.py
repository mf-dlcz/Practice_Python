#Parent class
class Shape:
    
    def __init__(self, color):
        self.color = color
        
    def calc_area(self):
        pass #this method will be overwritten
    
    def get_color(self):
        print(self.color)
        
class Rectangle(Shape):
    
    def __init__(self, color, width, height):
        #call parents init
        #with super, we do not need self
        super().__init__(color)
        self.width = width
        self.height = height
        
    def calc_area(self):
        return self.width*self.height
        
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
        
    def calc_area(self):
        return 3.14 * self.radius * self.radius
        
rec1 = Rectangle("Turquoise", 5, 2)
rec1.get_color()
area = rec1.calc_area()
print(f"The area of the rectangle is {area}")

circle1 = Circle("Green", 4)
circle1.get_color()
circlearea = circle1.calc_area()
print("The are of the circle is ", circlearea)
        