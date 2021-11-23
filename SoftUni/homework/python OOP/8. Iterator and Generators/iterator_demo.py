class Person:
    def __init__(self, name):
        self.name = name
        self.index = 0

    # Without __iter__ method will raise TypeError: 'Person' object is not iterable
    def __iter__(self):
        return self

    # Without __next__ method will raise TypeError: iter() returned non-iterator of type 'Person'
    def __next__(self):

        # Without checking the index will rise IndexError: string index out of range
        if self.index == len(self.name):
            raise StopIteration

        value = self.name[self.index]
        self.index += 1
        return value


gosho = Person('Gosho')
for x in gosho:
    print(x)


print('\n------------\n')


class Person1:
    def __init__(self, name):
        self.name = name
        self.index = 0

    # return an object with a method __next__
    def __iter__(self):
        return PersonIterator(self)


class PersonIterator:
    def __init__(self, person):
        self.person = person
        self.index = 0

    def __next__(self):
        if self.index == len(self.person.name):
            raise StopIteration

        value = self.person.name[self.index]
        self.index += 1
        return value


gosho2 = Person1('Gosho')
iter1 = iter(gosho2)
iter2 = iter(gosho2)
print(iter1)

print('From iter1: ', next(iter1))
print('From iter2: ', next(iter2))
print('From iter1: ', next(iter1))
print('From iter1: ', next(iter1))
print('From iter2: ', next(iter2))
print('From iter2: ', next(iter2))

