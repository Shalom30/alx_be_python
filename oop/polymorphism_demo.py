import math


class Shape:
    def area(self):
        raise NotImplemented


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        a = self.length * self.width

        return f"The area of the Rectangle is: {a}"


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        a = math.pi * (self.radius * self.radius)

        return f"The area of the Circle is: {a}"
