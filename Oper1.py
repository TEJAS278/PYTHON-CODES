import math
 
class Circle:
 
    def __init__(self, radius):
        self.__radius = radius
 
    def setRadius(self, radius):
        self.__radius = radius
 
    def getRadius(self):
        return self.__radius
 
    def area(self):
        return math.pi * math.pow(self.__radius,2)
 
    def __add__(self, n):
        return Circle( self.__radius + n.__radius )
 
c1 = Circle(4)
print(c1.getRadius())
 
c2 = Circle(5)
print(c2.getRadius())
 
c3 = c1 + c2 # This became possible because we have overloaded + operator by adding a    method named __add__
print(c3.getRadius())
print("Area of circle :",c1.area())
