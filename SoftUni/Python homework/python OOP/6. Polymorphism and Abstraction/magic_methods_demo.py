class Purchase:
    _budget = 1000
    _name = 'Pesho'

    def __init__(self, product_name, cost):
        self.product_name = product_name
        self.cost = cost

    def __add__(self, other):
        name = f'{self.product_name} and {other.product_name}'
        cost = self.cost + other.cost
        return f'Add method:\nTotal cost of <{name}> is: {cost}$'

    def __sub__(self, other):
        products_name = f'{self.product_name} and {other.product_name}'
        budget_left = self._budget - self.cost - other.cost
        if budget_left >= 0:
            return f'{self._name} bought: {products_name} and left with {budget_left}$.'

        return f'{self._name} don\'t have enough money to buy {products_name}. Need {abs(budget_left)}$ more money.'

    def __mul__(self, other):
        products_name = f'{self.product_name} and {other.product_name}'
        total_money_need = self.cost * 2 + other.cost * 3
        return f'Pesho want to buy {products_name} and need {total_money_need}$ to buy 2 sofa\'s and 3 tables'

    def __floordiv__(self, other):
        sum_of_numbers = self.cost // other.cost
        return f'{self.cost} // {other.cost} = {sum_of_numbers}'

    def __truediv__(self, other):
        sum_of_numbers = self.cost / other.cost
        return f'{self.cost} / {other.cost} = {sum_of_numbers}'

    def __pow__(self, power, modulo=None):
        sum_of_numbers = self.cost ** power.cost
        return f'{self.cost} ** {power.cost} = {sum_of_numbers}'


first_purchase = Purchase('Sofa', 100)
second_purchase = Purchase('Table', 100)
print(first_purchase + second_purchase)
print(first_purchase - second_purchase)
print(first_purchase * second_purchase)
print(first_purchase // second_purchase)
print(first_purchase / second_purchase)
print(first_purchase ** second_purchase)
