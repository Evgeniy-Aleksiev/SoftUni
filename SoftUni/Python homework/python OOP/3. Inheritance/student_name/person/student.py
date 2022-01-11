from person import Person

class Student(Person):
    def __init__(self, first_name, last_name, age, student_id):
        super().__init__(first_name,last_name)
        self.age = age
        self.student_id = student_id

    def get_student_info(self):
        return super().get_full_name() + f'is {self.age} years old with student ID: {self.student_id}.'

evgeniy = Student('Evgeniy', 'Aleksiev', 23, 123123)
print(evgeniy.get_student_info())