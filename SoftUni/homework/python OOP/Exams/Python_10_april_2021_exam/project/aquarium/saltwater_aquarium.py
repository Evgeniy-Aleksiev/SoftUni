from project import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    __DEFAULT_CAPACITY = 25

    def __init__(self, name):
        super().__init__(name, self.__DEFAULT_CAPACITY)