from abc import ABC, abstractmethod


class WaterSuitable:
    @staticmethod
    def check_if_fish_is_suitable(fish_type, aquarium_type):
        if fish_type == 'FreshwaterFish':
            return aquarium_type == 'FreshwaterAquarium'
        if fish_type == 'SaltwaterFish':
            return aquarium_type == 'SaltwaterAquarium'
        return False


class BaseAquarium(ABC):
    __INVALID_NAME_MESSAGE = 'Aquarium name cannot be an empty string.'

    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity       # represents the number of fish an aquarium can have
        self.decorations = []          # decorations container(objects)
        self.fish = []                 # fish container(objects)

    @classmethod
    def __validate_name(cls, value):
        if not value or not value.strip():
            raise ValueError(cls.__INVALID_NAME_MESSAGE)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    def calculate_comfort(self):
        result = sum([x.comfort for x in self.decorations])
        return result

    def add_fish(self, fish):
        if self.capacity - 1 <= 0:
            return 'Not enough capacity.'

        water_suitable = WaterSuitable().check_if_fish_is_suitable(fish.__class__.__name__, self.__class__.__name__)
        if water_suitable:
            self.capacity -= 1
            self.fish.append(fish)
            return f'Successfully added {fish.__class__.__name__} to {self.name}.'
        return 'Water not suitable.'

    def remove_fish(self, fish):
        self.capacity += 1
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        return f'''{self.name}
Fish: {' '.join([fish.name for fish in self.fish]) if self.fish else 'none'}
Decorations: {len(self.decorations)}
Comfort: {self.calculate_comfort()}'''


