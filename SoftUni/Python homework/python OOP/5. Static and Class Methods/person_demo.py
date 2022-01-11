class Person:
    _max_name_length = 15
    _min_name_length = 2

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    @staticmethod
    def sample_static_method():
        print(Person.say_hi)
        print('Independent from class')

    def sample_instance_method(self):
        print('(Instance) dependent on the class')

    def say_hi(self):
        self.sample_static_method()
        self.sample_instance_method()
        print('Hello there!')

    def __validate_name(self, value):
        if len(value) < self._min_name_length or self._max_name_length < len(value):
            raise ValueError(f'Name must be between {self._min_name_length} and {self._max_name_length} characters long!')


Person.sample_static_method()
Person('ema').say_hi()
Person('Ema').sample_instance_method()