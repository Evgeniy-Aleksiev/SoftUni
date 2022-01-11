class MyClass:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __len__(self):
        return self.size


my_class = MyClass('Class Name', 3)
print(len(my_class))

print()

print(1 + 1)
print("Hello, " + 'SoftUni')
print(["1", "2"] + ["3", "4"])

print()


class Items:
    def __init__(self):
        self._items = []

    def add_items(self, value):
        self._items.append(value)

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __add__(self, other):
        result = Items()
        [result.add_items(x) for x in self._items]
        [result.add_items(x) for x in other._items]
        return result


ii = Items()
ii.add_items(1)
ii.add_items(2)
ii.add_items(3)

print(len('asd'))
print(len([1, 2, 3]))
print(len((1, 4, 5, 2, 3)))
print(len({1, 2, 4, 5}))
print(len(ii))

i2 = Items()
i2.add_items(2)

i_result = ii + i2
print(i_result)
print(f'{ii} + {i2} = {ii + i2}')

print()
