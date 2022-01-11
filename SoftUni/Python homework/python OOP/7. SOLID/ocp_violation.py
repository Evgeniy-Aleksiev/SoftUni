from abc import abstractmethod


class Student:
    def __init__(self, name, semester_tax, average_grade):
        self.name = name
        self.semester_tax = semester_tax
        self.average_grade = average_grade

    @abstractmethod
    def get_discount(self):
        pass


class FortyPercentDiscount(Student):
    def get_discount(self):
        if self.average_grade >= 5:
            return self.semester_tax * 0.6


class TwentyPercentDiscount(Student):
    def get_discount(self):
        if 4 <= self.average_grade < 5:
            return self.semester_tax * 0.8


bob = FortyPercentDiscount('Bob', 1000, 6)
print(bob.get_discount())