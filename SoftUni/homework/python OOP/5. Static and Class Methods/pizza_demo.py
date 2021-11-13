class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients + ['beer']

    @classmethod
    def pepperoni(cls):
        return cls(['tomato sauce', 'parmesan', 'pepperoni'])


print(Pizza.pepperoni())
print(Pizza.pepperoni().__dict__)
p = Pizza(['papa'])
print(p.__dict__)
print(Pizza.pepperoni().__dict__)