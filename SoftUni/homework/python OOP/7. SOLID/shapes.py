from abc import ABC, abstractmethod
from math import pi


class Shapes(ABC):

    @abstractmethod
    def calc_area(self):
        pass


class Rectangle(Shapes):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_area(self):
        return self.width * self.height


class Triangle(Shapes):
    def __init__(self, side, height):
        self.side = side
        self.height = height

    def calc_area(self):
        return  self.side * self.height / 2


class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        return pi * self.radius**2


class AreaCalculator:

    def __init__(self, shapes):
        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calc_area()

        return total


shapes = [Rectangle(1, 6), Triangle(2, 3), Circle(4)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)

