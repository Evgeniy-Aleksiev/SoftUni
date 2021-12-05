from abc import ABC, abstractmethod

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):
    _MIN_TABLE_NUMBER = 1
    _MAX_TABLE_NUMBER = 50
    _INVALID_TABLE_NUMBER_MESSAGE = None

    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []      # contain every food order made from the table
        self.drink_orders = []     # contain every drink order made from the table
        self.number_of_people = 0  # count people who sit at the table
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError('Capacity has to be greater than 0!"')
        self.__capacity = value

    @classmethod
    def __validate_table_number(cls, value):
        if cls._MIN_TABLE_NUMBER and value < cls._MIN_TABLE_NUMBER:
            raise ValueError(cls._INVALID_TABLE_NUMBER_MESSAGE)
        if cls._MAX_TABLE_NUMBER and cls._MAX_TABLE_NUMBER < value:
            raise ValueError(cls._INVALID_TABLE_NUMBER_MESSAGE)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        self.__validate_table_number(value)
        self.__table_number = value

    def reserve(self, number_of_people):
        self.number_of_people = number_of_people
        self.is_reserved = True

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        total_food_price = sum([x.price for x in self.food_orders])
        total_drink_price = sum([x.price for x in self.drink_orders])

        return total_food_price + total_drink_price

    def clear(self):
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if self.is_reserved:
            return None

        return f'''Table: {self.table_number}
Type: {self.table_type}
Capacity: {self.capacity}'''

    @property
    @abstractmethod
    def table_type(self):
        pass
