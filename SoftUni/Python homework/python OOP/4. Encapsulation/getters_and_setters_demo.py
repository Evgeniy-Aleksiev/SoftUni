class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError('Name cannot be None')
        if not value.isalpha():
            raise ValueError('Name must be only letters')
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not value:
            raise ValueError('Age cannot be None')
        if value <= 0:
            raise ValueError('Age must be greater than zero')
        self.__age = value

    def info(self):
        return f'Persona name: {self.name}, {self.age} years old.'


person = Person('Evgeniy', 19)
print(person.info())
person.name = 'Aleksiev'
person.age = 23
print(person.info())