def get_info(**kwargs):
    return f'This is {kwargs["name"]} from {kwargs["town"]} and he is {kwargs["age"]} years old'


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))


def get_some_func(name, town, age=22):
    return f'This is {name} from {town} and he is {age} years old'


person = {"name": "George", "town": "Sofia", "age": 20}
print(get_some_func(**person))

