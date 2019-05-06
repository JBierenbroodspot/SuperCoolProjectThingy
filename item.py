class Item(object):

    def __init__(self, name, position, icon, value=None, descr=None):
        self.name = name
        self.position = position
        self.icon = icon
        self.value = value
        self.description = descr

    def pick_up(self, player):
        player.inventory.append(self.name)
        del self.position


class Weapon(Item):

    def __init__(self, name, position, icon, damage, value=None, descr=None):
        super().__init__(name, position, icon, value, descr)
        self.damage = damage


class Sword(Weapon):

    def __init__(self, name, position, icon, damage, damage_type, value=None, descr=None):
        super(Sword, self).__init__(name, position, icon, value, descr, damage)
        self.damage_type = damage_type


class Mace(Weapon):

    def __init__(self, name, position, icon, damage, damage_type, value=None, descr=None):
        super(Mace, self).__init__(name, position, icon, value, descr, damage)
        self.damage_type = damage_type
