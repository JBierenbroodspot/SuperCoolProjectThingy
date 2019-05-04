import random


class Field:

    def __init__(self, x, y, terrain):

        self.x = x
        self.y = y
        self.field = []

        while len(self.field) < self.y:
            fieldpart = []
            while len(fieldpart) < self.x:
                fieldpart.append(
                    terrain[random.randint(0, len(terrain) - 1)]
                )
            self.field.append(fieldpart)

        self.empty = self.field[:]

    def copy_field(self):
        copy = []
        for row in self.field:
            copy.append(row.copy())
        return copy

    def replace_field(self, replacement):
        count = 0
        for row in replacement:
            self.field[count] = row.copy()
            count += 1
        return self.field
