class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Person1:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def say_hello(self):
        return f'Say hello {self._name}'


class Person2(Person1):
    def __init__(self, name, age):
        super().__init__(name, age)


class Person3:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def info(self):
        return f'I am {self.__name}, {self.__age} years old.'


class Person4:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_name(self, new_name):
        if not new_name:
            raise ValueError('Name cannot be None')
        self._name = new_name

    def set_age(self, new_age):
        self._age = new_age


class Person5:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, new_name):
        if not new_name:
            raise ValueError('Name cannot be None')
        self.__name = new_name

    def set_age(self, new_age):
        self.__age = new_age


person = Person('Evgeniy', 16)
print(person.name)
print(person.age)
print()
person1 = Person1('Evgeniy1', 16)
print(person1._name)
print(person1._age)
print()
person2 = Person2('Evgeniy2', 18)
print(person2._name)
print(person2._age)
print(person2.__class__.__bases__[0].__name__)
print(person2.say_hello())
print()
person4 = Person4('Evgeniy4', 12)
print(person4.get_name())
print(person4.get_age())
person4.set_name('Aleksiev4')
person4.set_age('23')
print(person4.get_name())
print(person4.get_age())
print()
person5 = Person5('Evgeniy5', 1412)
print(person5.get_name())
print(person5.get_age())
print()
person3 = Person3('Evgeniy3', 23)
print(person3.info())
print(person3.__name)
print(person3.__age)