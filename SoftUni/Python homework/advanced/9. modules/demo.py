import random

fruits = ['apple', 'banana', 'cherry']
print(fruits)
print(random.choice(fruits))
fruits = ['apple', 'banana', 'cherry']
random.shuffle(fruits)
print(fruits)