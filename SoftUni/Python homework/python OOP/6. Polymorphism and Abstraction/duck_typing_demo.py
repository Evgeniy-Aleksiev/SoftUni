class Cat:
    @staticmethod
    def sound():
        print('Meow!')


class Train:
    @staticmethod
    def sound():
        print('Sound from wheel slipping')


for any_type in Cat(), Train():
    any_type.sound()