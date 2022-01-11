# This class is repository for the decorations that are in aqua shop

class DecorationRepository:
    def __init__(self):
        self.decorations = []       # contain all decorations (objects)

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True

        return False

    def find_by_type(self, decoration_type):
        # TODO: Returns the first decoration of the given type if there is. Otherwise, returns a message 'None'
        for decoration in self.decorations:
            if decoration.__class__.__name__ == decoration_type:
                return decoration
        return 'None'
