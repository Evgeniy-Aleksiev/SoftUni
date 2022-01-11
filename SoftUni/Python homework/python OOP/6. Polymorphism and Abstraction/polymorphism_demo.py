class Shape:
    def calculate_area(self):
        return


class Square(Shape):
    side_length = 2

    def calculate_area(self):
        return self.side_length * 2


class Triangle(Shape):
    base_length = 4
    height = 3

    def calculate_area(self):
        return 0.5 * self.base_length * self.height


a = Triangle()
print(str(a.calculate_area()))

for obj in Square(), Triangle():
    if isinstance(obj, Square):
        area = obj.calculate_area()
    elif isinstance(obj, Triangle):
        area = obj.calculate_area()

    print(area)


# Override, compile-time polymorphism
class Person:
    @staticmethod
    def say_hello():
        return 'Hi!'

    @staticmethod
    def say_hello():
        return 'Hello!'

print(Person.say_hello())