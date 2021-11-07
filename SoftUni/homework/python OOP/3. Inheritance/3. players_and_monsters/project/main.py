from project.hero import Hero
from project.elf import Elf
from project.muse_elf import MuseElf
from project.dark_wizard import DarkWizard

hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)
museelf = MuseElf('Z', 5)
print(str(museelf))
print(museelf.__class__.__bases__[0].__name__)
print(museelf.username)
print(museelf.level)
darkwizard = DarkWizard('A', 10)
print(str(darkwizard))
print(darkwizard.__class__.__bases__[0].__name__)
print(darkwizard.username)
print(darkwizard.level)