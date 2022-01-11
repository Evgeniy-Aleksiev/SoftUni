class Dog:
    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name

dog_name = Dog('Rex')
print(dog_name.__dict__)
dog_name.change_name('Fox')
print(dog_name.__dict__)
print(Dog.__dict__)