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

        return a


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        num = self.radius ** 2
        a = math.pi * num

        return a
