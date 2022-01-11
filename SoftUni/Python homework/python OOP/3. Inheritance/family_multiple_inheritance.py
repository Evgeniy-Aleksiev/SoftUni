class Father:
    def __init__(self, father_name):
        self.father_name = father_name

class Mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name

class Son(Father, Mother):
    def __init__(self, father_name1, mother_name1):
        Father.__init__(self, father_name1)
        Mother.__init__(self, mother_name1)

    def get_parent_info(self):
        return f'Father: {self.father_name}, Mother: {self.mother_name}'

child = Son('Evgeniy Aleksiev', 'Ema Slavova')
print(child.get_parent_info())


class Father1:
    def __init__(self):
        self.father1_name = 'Taylor Evans'

class Mother1:
    def __init__(self):
        self.mother1_name = 'Bet Williams'

class Daughter(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)

    def get_parent_info(self):
        return f'Father: {self.father1_name},Mother: {self.mother1_name}'

child1 = Daughter()
print(child1.get_parent_info())