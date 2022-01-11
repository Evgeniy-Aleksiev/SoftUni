class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

class Student(Person):
    pass

evgeniy = Student("Evgeniy", "Aleksiev")
print(evgeniy)
print(evgeniy.get_full_name())


class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'{self.name} is {self.age} years old.'

class Student2(Person2):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def get_id(self):
        return self.student_id

person_pesho = Person2('Pesho Petrov', 19)
print(person_pesho.get_info())
pesho = Student2('Pesho', 19, 123123)
print(pesho.get_info())
print(f'Student ID: {pesho.get_id()}')