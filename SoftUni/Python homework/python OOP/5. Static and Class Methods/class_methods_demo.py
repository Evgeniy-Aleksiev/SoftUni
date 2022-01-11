class Person:
    attr1 = 'asd'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def sample_class_method(cls):
        print(f'Person: {Person.attr1}')
        print(f'cls: {cls.attr1}')
        print(cls)

    def sample_instance_method(self):
        print(self)


class Student(Person):
    attr1 = 'Student'


Student.sample_class_method()
Person.sample_class_method()
p = Person('asd', 1)
p.sample_instance_method()
Person.sample_instance_method(p)