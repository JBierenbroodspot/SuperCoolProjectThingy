class Player:

    def __init__(self, name, age, length, position, icon):

        self.name = name
        self.age = age
        self.length = length
        self.equipment = {
            'head': None,
            'body': None,
            'legs': None,
            'feet': None,
            'rhand': None,
            'lhand': None
        }
        self.inventory = []
        self.position = position
        self.icon = icon

    def add_item(self, *args):

        for item in args:
            self.inventory.append(item)

    def equip_item(self, item, slot):
        if slot in self.equipment:
            if item in self.inventory:
                if self.equipment[slot] is None:
                    self.equipment[slot] = item
                else:
                    self.inventory.append(self.equipment[slot])
                    self.equipment[slot] = item
                self.inventory.remove(item)
            else:
                return print("I do not have this item: {0}".format(item))
        else:
            return print("\'{0}\' is not a valid slot. Please select a valid slot".format(slot))

    def check_inventory(self):

        temp_inv = {}

        for item in self.inventory:
            if item not in temp_inv:
                temp_inv[item] = 1
            else:
                temp_inv[item] += 1

        for item in temp_inv:
            print("{0}x {1}".format(temp_inv[item], item))

    def check_equipment(self):
        for item in self.equipment:
            print("{0}: {1}".format(item, self.equipment[item]))
