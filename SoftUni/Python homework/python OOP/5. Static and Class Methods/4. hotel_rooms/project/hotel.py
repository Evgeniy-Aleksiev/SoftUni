class Hotel:

    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for current_room in self.rooms:
            if current_room.number == room_number:
                result = current_room.take_room(people)
                if isinstance(result, int):
                    self.guests += people

    def free_room(self, room_number):
        for current_room in self.rooms:
            if current_room.number == room_number:
                result = current_room.free_room()
                if isinstance(result, int):
                    self.guests -= result

    def status(self):
        total_free_rooms = [str(r.number) for r in [x for x in self.rooms if not x.is_taken]]
        total_taken_rooms = [str(r.number) for r in [x for x in self.rooms if x.is_taken]]
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(total_free_rooms)}\n" \
               f"Taken rooms: {', '.join(total_taken_rooms)}"


