class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people):
        if self.is_taken or self.capacity < people:
            return f'Room number {self.number} cannot be taken'

        self.guests += people
        self.is_taken = True
        return people

    def free_room(self):
        if not self.is_taken:
            return f'Room number {self.number} is not taken'

        guests = self.guests
        self.is_taken = False
        self.guests = 0
        return guests


