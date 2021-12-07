from project import Ornament, SaltwaterFish
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.aquarium.base_aquarium import BaseAquarium
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish


class ValidAquariumType:
    @staticmethod
    def create(aquarium_type, aquarium_name):
        if aquarium_type == 'FreshwaterAquarium':
            return FreshwaterAquarium(aquarium_name)
        if aquarium_type == 'SaltwaterAquarium':
            return SaltwaterAquarium(aquarium_name)
        return None


class ValidDecorationTypes:
    @staticmethod
    def create(decoration_type):
        if decoration_type == 'Ornament':
            return Ornament()
        if decoration_type == 'Plant':
            return Plant()
        return None


class ValidFishTypes:
    @staticmethod
    def create(fish_type, name, species, price):
        if fish_type == 'FreshwaterFish':
            return FreshwaterFish(name, species, price)
        if fish_type == 'SaltwaterFish':
            return SaltwaterFish(name, species, price)
        return None


class WaterSuitable:
    @staticmethod
    def check_if_fish_is_suitable(fish_type, aquarium_type):
        if fish_type == 'FreshwaterFish':
            return aquarium_type == 'FreshwaterAquarium'
        if fish_type == 'SaltwaterFish':
            return


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        aquarium = ValidAquariumType().create(aquarium_type, aquarium_name)

        if not aquarium:
            return 'Invalid aquarium type.'

        self.aquariums.append(aquarium)
        return f'Successfully added {aquarium_type}.'

    def add_decoration(self, decoration_type: str):
        decoration = ValidDecorationTypes().create(decoration_type)

        if not decoration:
            return 'Invalid decoration type.'

        self.decorations_repository.add(decoration)
        return f'Successfully added {decoration_type}.'

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name]
        decoration = self.decorations_repository.find_by_type(decoration_type)

        if aquarium and decoration != 'None':
            aquarium[0].add_decoration(decoration)
            self.decorations_repository.remove(decoration)

            return f'Successfully added {decoration_type} to {aquarium_name}.'
        return f'There isn\'t a decoration of type {decoration_type}.'

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        fish = ValidFishTypes().create(fish_type, fish_name, fish_species, price)
        aquarium = [a for a in self.aquariums if a.name == aquarium_name]

        if not fish:
            return f'There isn\'t a fish of type {fish_type}.'

        return aquarium[0].add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                aquarium.feed()
                return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
        decoration_value = sum([d.price for d in aquarium.decorations])
        fish_value = sum([f.price for f in aquarium.fish])

        return f'The value of Aquarium {aquarium_name} is {(decoration_value + fish_value):.2f}.'

    def report(self):
        result = ''
        for aquarium in self.aquariums:
            result += str(aquarium)
            result += '\n'

        return result
