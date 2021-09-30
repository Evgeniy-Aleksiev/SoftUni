def some_func(a, b, c):
    return a + b + c


nums = 1, 2, 3
print(some_func(*nums))
print(some_func(*(1, 2, 3)))


def get_some_func(name, town, age=22):
    return f'This is {name} from {town} and he is {age} years old'


person = {"name": "George", "town": "Sofia", "age": 20}
print(get_some_func(**person))
print(get_some_func(**{"name": "Evgeniy", "town": "Sofia", "age": 20}))