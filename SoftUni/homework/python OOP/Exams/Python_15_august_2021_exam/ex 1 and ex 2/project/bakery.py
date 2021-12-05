from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class FoodFactory:
    @staticmethod
    def create(food_type, name, price):
        if food_type == 'Bread':
            return Bread(name, price)
        if food_type == 'Cake':
            return Cake(name, price)
        return None


class DrinkFactory:
    @staticmethod
    def create(drink_type, name, portion, brand):
        if drink_type == 'Tea':
            return Tea(name, portion, brand)
        if drink_type == 'Water':
            return Water(name, portion, brand)
        return None


class TableFactory:
    @staticmethod
    def create(table_type, table_number, capacity):
        if table_type == 'InsideTable':
            return InsideTable(table_number, capacity)
        if table_type == 'OutsideTable':
            return OutsideTable(table_number, capacity)


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []             # contains every type of food
        self.drinks_menu = []           # contains every type of drink
        self.tables_repository = []      # contains every table
        self.total_income = 0
        self.food_names = set()
        self.drinks_names = set()
        self.table_numbers = set()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise Exception('Name cannot be empty string or white space!')
        self.__name = value

    def __get_food_by_name(self, name):
        foods = [f for f in self.food_menu if f.name == name]
        return foods[0] if foods else None

    def __get_drink_by_name(self, name):
        drinks = [d for d in self.drinks_menu if d.name == name]
        return drinks[0] if drinks else None

    def __get_table_by_number(self, table_number) -> Table:
        tables = [t for t in self.tables_repository if t.table_number == table_number]
        return tables[0] if tables else None

    def add_food(self, food_type: str, name: str, price: float):
        if name in self.food_names:
            raise Exception(f"{food_type} {name} is already in the menu!")

        food = FoodFactory().create(food_type, name, price)
        self.food_menu.append(food)
        self.food_names.add(food.name)
        return f'Added {name} ({food_type}) to the food menu'

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if name in self.drinks_names:
            raise Exception(f'{drink_type} {name} is already in the menu!')

        drink = DrinkFactory().create(drink_type, name, portion, brand)
        self.drinks_menu.append(drink)
        self.drinks_names.add(drink.name)
        return f'Added {name} ({brand}) to the drink menu'

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_number in self.table_numbers:
            raise Exception(f'Table {table_number} is already in the bakery!')

        table = TableFactory().create(table_type, table_number, capacity)
        self.tables_repository.append(table)
        self.table_numbers.add(table_number)
        return f'Added table number {table_number} in the bakery'

    def reserve_table(self, number_of_people: int):
        def is_table_free(table):
            return not table.is_reserved and number_of_people <= table.capacity

        tables = [t for t in self.tables_repository if is_table_free(t)]

        if not tables:
            return f'No available table for {number_of_people} people'

        table_to_reserved = tables[0]
        table_to_reserved.reserve(number_of_people)
        return f'Table {table_to_reserved.table_number} has been reserved for {number_of_people} people'

    def order_food(self, table_number, *food_name):
        table = self.__get_table_by_number(table_number)

        if not table:
            return f'Could not find table {table_number}'

        food_name_in_menu = [name for name in food_name if name in self.food_names]
        food_names_not_in_menu = [name for name in food_name if name not in self.food_names]

        foods = [self.__get_food_by_name(name) for name in food_name_in_menu]
        [table.order_food(f) for f in foods]

        ordered_foods_str = '\n'.join(repr(f) for f in foods)
        missing_foods_str = '\n'.join(food_names_not_in_menu)
        return f'''Table {table_number} ordered:
{ordered_foods_str}
{self.name} does not have in the menu:
{missing_foods_str}'''

    def order_drink(self, table_number, *drink_name):
        table = self.__get_table_by_number(table_number)

        if not table:
            return f'Could not find table {table_number}'

        drink_name_in_menu = [name for name in drink_name if name in self.drinks_names]
        drinks_names_not_in_menu = [name for name in drink_name if name not in self.drinks_names]

        drinks = [self.__get_drink_by_name(drink) for drink in drink_name_in_menu]
        [table.order_drink(d) for d in drinks]

        ordered_str = '\n'.join(repr(d) for d in drinks)
        missing_str = '\n'.join(drinks_names_not_in_menu)
        return f'''Table {table_number} ordered:
{ordered_str}
{self.name} does not have in the menu:
{missing_str}'''

    def leave_table(self, table_number):
        table = self.__get_table_by_number(table_number)
        table_bill = table.get_bill()
        self.total_income += table_bill
        table.clear()
        return f'''Table: {table_number}
Bill: {table_bill:.2f}'''

    def get_free_tables_info(self):
        table_infos = [t.free_table_info() for t in self.tables_repository if not t.is_reserved]
        return '\n'.join(table_infos)

    def get_total_income(self):
        return f'Total income: {self.total_income:.2f}lv'

