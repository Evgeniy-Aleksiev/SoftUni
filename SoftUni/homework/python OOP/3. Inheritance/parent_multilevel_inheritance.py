class Parent:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def get_age(self):
        return self.age

class GrandChilld(Child):
    def __init__(self, name, age, address):
        super().__init__(name, age)
        self.address = address

    def get_address(self):
        return self.address

parent = Parent('Evgeniy')
print('Parent: ')
print(parent.get_name())
print('-----------')
child = Child('Evgeniy', 13)
print('Child:')
print(child.get_name())
print(child.get_age())
print('-----------')
grand_child = GrandChilld('Evgeniy', 13, 'Address 15-17')
print('Grand child:')
print(grand_child.get_name())
print(grand_child.get_age())
print(grand_child.get_address())