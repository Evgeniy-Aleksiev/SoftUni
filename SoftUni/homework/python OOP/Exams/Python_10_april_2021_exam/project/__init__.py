from project.decoration.ornament import Ornament
from project.aquarium.base_aquarium import BaseAquarium
from project.fish.saltwater_fish import SaltwaterFish
from project.decoration.decoration_repository import DecorationRepository
from project.controller import Controller

#a = BaseAquarium('xaxa', 1222)
bd = Ornament()
db = Ornament()
sw = SaltwaterFish('Goshka', 'mammal', 15)
sw2 = SaltwaterFish('Pehska', 'mammal', 11)

# a.add_decoration(db)
# a.add_decoration(bd)
# # print(a.calculate_comfort())
# a.add_fish(sw)
# a.add_fish(sw2)
# a.feed()

s = DecorationRepository()
#s.add(db)
#
# print(s.decorations)
# print(s.find_by_type('Ornament'))
c = Controller()
c.add_decoration('Ornament')
c.add_decoration('Ornament')
c.add_aquarium('FreshwaterAquarium', 'Goshka')
c.add_aquarium('FreshwaterAquarium', 'Goshka')
c.insert_decoration('Goshka', 'FreshwaterAquarium')
