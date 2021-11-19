
# Bad practice. Here we have two responsibility:
#   student properties management
#   student database management

class Student1:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        pass

    def register(self):
        pass

# Split the responsibility to two classes


class Student:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class StudentRecords:
    def get_student(self, id):
        pass

    def register(self, student):
        pass
