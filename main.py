import player
import fieldgen
import creature
import constants
import functions
import item
import os

object_list = []


def draw_field(f, objects):
    for obj in objects:
        Field.field[obj.position[0]][obj.position[1]] = obj.icon

    for row in f:
        for tile in row:
            print(tile, end='')
        print("\n")


def move(f, moved, a):
    x = len(f[0]) - 1
    y = len(f) - 1
    if a == "w":
        moved.position[0] -= 1
        if moved.position[0] < 0:
            moved.position[0] = 0
    elif a == "s":
        moved.position[0] += 1
        if moved.position[0] > y:
            moved.position[0] = y
    elif a == "a":
        moved.position[1] -= 1
        if moved.position[1] < 0:
            moved.position[1] = 0
    elif a == "d":
        moved.position[1] += 1
        if moved.position[1] > x:
            moved.position[1] = x
    return moved.position


def equip_item(slot=None, item=None):
    if item is None:
        item = input("What item would you like to equip?\n>>>")
    if slot is None:
        slot = input("In what slot would you like to equip the item?\n>>>")
    player.equip_item(item, slot)


def check_status(objects):
    iterobj = next(iter(objects))
    for obj in objects:
        if obj != iterobj:
            if iterobj.position == obj.position:
                if issubclass(type(obj), item.Item):
                    obj.pick_up(iterobj)
                    object_list.remove(obj)


player = player.Player("player", 18, 180, [0, 0], "@")
sword = item.Item("Sword", [1, 1], "I", 6, "A sword")
orc = creature.Creature("Orc", "Orc", 10, [2, 2], "O")
object_list.append(player)
object_list.append(sword)
object_list.append(orc)
player.add_item(
    "hat",
    "robe",
    "boots",
    "torch",
    "torch",
    "torch"
)
Field = fieldgen.Field(5, 3, constants.empty_terrain)
field_empty = Field.copy_field()


end_game = False
while not end_game:
    os.system('cls')
    Field.field = Field.replace_field(field_empty)
    draw_field(Field.field, object_list)

    # Even listening
    actions = input().lower().split(' ')
    for action in actions:
        if action in ["w", "a", "s", "d"]:
            os.system('cls')
            move(Field.field, player, action[0])
        if action in ["i", "inv", "inventory"]:
            os.system('cls')
            player.check_inventory()
            functions.wait()
        if action in ["equipment", "eq"]:
            os.system('cls')
            player.check_equipment()
            functions.wait()
        if action in ['equip']:  # equip slot item
            os.system('cls')
            if 1 < len(actions):
                if 2 < len(actions):
                    player.equip_item(actions[2], actions[1])
                else:
                    equip_item(actions[1])
            else:
                equip_item()
            functions.wait()
        if action in ["exit", "quit"]:
            end_game = True

        check_status(object_list)
