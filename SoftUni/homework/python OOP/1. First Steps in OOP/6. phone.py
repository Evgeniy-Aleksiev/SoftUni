class Phone:

    def __init__(self, color, size, name, model):
        self.color = color
        self.size = size
        self.name = name
        self.model = model


    def phone_model(self):
        return f"The model of phone is {self.name} {self.model}"


    def turn_on(self):
        return 'The phone is turned on'


phone = Phone("blue", 4.7, "Iphone", "13 Pro Max")
print(phone.phone_model())
print(phone.turn_on())