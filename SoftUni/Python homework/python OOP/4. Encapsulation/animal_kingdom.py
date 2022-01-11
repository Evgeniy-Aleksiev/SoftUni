class Mammals:
    _kingdom = 'animals'

    def __init__(self, name, anima_type, sound):
        self.name = name
        self.anima_type = anima_type
        self.sound = sound

    def make_sound(self):
        return f'{self.name} makes {self.sound}'

    def get_kingdom(self):
        return self._kingdom.capitalize()

    def info(self):
        return f'{self.name} is of type {self.anima_type}'


class Tiger(Mammals):
    _kingdom = 'tigers'

    def __init__(self, name, anima_type, sound):
        super().__init__(name, anima_type, sound)


mammal = Mammals("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())
print()
tiger = Tiger('Tiger', 'Domestic', 'Roar')
print(tiger.make_sound())
print(tiger.get_kingdom())
print(tiger.info())
print()
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())