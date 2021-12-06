from project import Ornament
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.aquarium.base_aquarium import BaseAquarium
from project.decoration.plant import Plant


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
        aquarium = [a for a in self.aquariums if a.name == aquarium_name][:1]
        decoration = self.decorations_repository.find_by_type(decoration_type)

        if aquarium and decoration is not 'None':
            aquarium.add_decoration()



    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        pass

    def feed_fish(self, aquarium_name: str):
        pass

    def calculate_value(self, aquarium_name: str):
        pass

    def report(self):
        pass