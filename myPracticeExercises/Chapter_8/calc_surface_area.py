# Challenge: Calculate Surface Area

import math

def surface_area(radius):
    surf_area = 4 * math.pi * radius ** 2
    return round(surf_area, 4)

#       TEST:
surfaceArea1 = surface_area(1)
surfaceArea2 = surface_area(2)
surfaceArea3 = surface_area(3)


print(surfaceArea1)
print(surfaceArea2)
print(surfaceArea3)