import math

# for x in dir(math):
#     pass
#     # print(x)

# # print(math.acos)

# total = math.pi * 2
# print(total)

###############################

'''             NOTE:
This example also uses the built-in Python function round(). The first argument provided to the 
round() function is the number to be rounded, in this example, the area. The second argument 
specifies the number of decimal places in the rounded number.
'''

def circle_area(radius):
    a = math.pi * radius ** 2
    return round(a, 2)


area_of_circle =circle_area(30)
# print(area_of_circle)

#################################

'''
The expression "Infinity is greater than 1,000" evaluates to True. In the third reference to infinity, 
a negative sign indicates negative infinity, or the opposite of infinity. The comparison "Negative 
infinity is greater than 0" evaluates to False.
'''

# print (math.inf)
# print (math.inf > 1000)         # True
# print (-math.inf > 0 )          # False

#################################

def divide(numerator, denominator):
    if denominator == 0:
        return math.nan
    else:
        return numerator/denominator
        
dividend = divide(5, -1)

if math.isnan(dividend):
    print ("Cannot divide by zero")
else:
    print (dividend)