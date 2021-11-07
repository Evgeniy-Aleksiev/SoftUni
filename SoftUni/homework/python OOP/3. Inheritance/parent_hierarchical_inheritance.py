class Parent:
    def init(self, name):
        self.name = name

    def say_hi(self):
        return f'Hi! I am {self.name}'


class Daughter(Parent):
    def __init__(self, name):
        super().__init__(name)

    def relation(self):
        return 'I am my parent\'s daughter'

class Son(Parent):
    def __init__(self, name):
        super().__init__(name)

    def relation(self):
        return 'I am my parent\'s son'


