class Parent():
    def say_hi(self):
        return 'Hello!'

class Child(Parent):
    def go_to_school(self):
        return 'I go to school.'

parent = Parent()
print(parent.say_hi())
child = Child()
print(child.say_hi())
print(child.go_to_school())