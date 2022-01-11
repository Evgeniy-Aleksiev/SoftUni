# import random as module_name
#
# print(module_name.randint(1, 10))

from random import choice as gimme_one, shuffle as mix

text = ['coke', 'steak', 'chips']
print(gimme_one(text))
mix(text)
print(text)