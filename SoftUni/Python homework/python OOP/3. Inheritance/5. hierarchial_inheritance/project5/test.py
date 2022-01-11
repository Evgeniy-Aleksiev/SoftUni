from project5.dog import Dog
from project5.cat import Cat
from project5.animal import Animal


animal = Animal()
dog = Dog()
cat = Cat()

print('From class Animal:')
print(animal.eat())
print()
print('From class Dog:')
print(dog.eat())
print(dog.bark())
print()
print('From class Cat:')
print(cat.eat())
print(cat.meow())
