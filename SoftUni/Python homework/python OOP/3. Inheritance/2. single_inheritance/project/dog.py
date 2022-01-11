from project.animal import Animal

class Dog(Animal):
    def bark(self):
        return 'barking...'

animal = Animal()
dog = Dog()
print(f'From Dog class {dog.bark()}')
print('From Dog class ' + dog.eat())
print('From Animal class ' + animal.eat())