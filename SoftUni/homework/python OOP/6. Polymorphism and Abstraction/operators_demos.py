class Person:
    def __init__(self, salary):
        self.salary = salary

    def __str__(self):
        return f'Salary: {self.salary}'

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __ne__(self, other):
        return self.salary != other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary


p1 = Person(20000)
p2 = Person(30030)
p3 = Person(20000)

print(f'{p1} < {p2} -> {p1 < p2}')
print(f'{p2} < {p1} -> {p2 < p1}')
print()
print(f'{p1} <= {p2} -> {p1 <= p2}')
print(f'{p2} <= {p1} -> {p2 <= p1}')
print(f'{p3} <= {p1} -> {p3 <= p1}')
print()
print(f'{p1} == {p2} -> {p1 == p2}')
print(f'{p3} == {p1} -> {p3 == p1}')
print()
print(f'{p1} != {p2} -> {p1 != p2}')
print(f'{p3} != {p1} -> {p3 != p1}')
print()
print(f'{p1} > {p2} -> {p1 > p2}')
print(f'{p2} > {p1} -> {p2 > p1}')
print()
print(f'{p1} != {p2} -> {p1 != p2}')
print(f'{p3} != {p1} -> {p3 != p1}')
print()
print(f'{p1} >= {p2} -> {p1 >= p2}')
print(f'{p2} >= {p1} -> {p2 >= p1}')
print(f'{p3} >= {p1} -> {p3 >= p1}')