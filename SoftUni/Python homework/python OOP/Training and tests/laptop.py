class Laptop:
    def __init__(self, name, model):
        self.name = name
        self.model = model

my_laptop = Laptop('Inspiron 15', 'Dell')
print(my_laptop.name)
print(my_laptop.model)
print(my_laptop.__dict__)

print('--------------')

your_laptop = Laptop('Predator', 'ASUS')
print(your_laptop.name)
print(your_laptop.model)
print(your_laptop.__dict__)