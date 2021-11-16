from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        raise NotImplementedError('Subclass must implement')


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print('Bark!')


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def sound(self):
        print('Meow!')


cat = Cat('Timmy')
cat.sound()
dog = Dog('Shluben')
dog.sound()
animal = Animal('Gerry')
animal.sound()