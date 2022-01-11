from abc import ABC, abstractmethod

# Good practice
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Not good practice! It could be achieved using exceptions

class Shape2:
    def __init__(self):
        if type(self) is Shape2:
            raise Exception('This is an abstract class')

    def area(self):
        raise Exception('This is an abstract class')

    def perimeter(self):
        raise Exception('This is an abstract class')


shape = Shape2()