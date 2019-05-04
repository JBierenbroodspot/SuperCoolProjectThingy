import person
import fieldgen
import constants
import functions
import os


def draw_field(f, *objects):
    for pos in objects:
        Field.field[pos[0]][pos[1]] = "@"

    for row in f:
        for tile in row:
            print(tile, end='')
        print("\n")


def move(f, p, a):
    x = len(f[0]) - 1
    y = len(f) - 1
    if a == "w":
        p[0] -= 1
        if p[0] < 0:
            p[0] = 0
    elif a == "s":
        p[0] += 1
        if p[0] > y:
            p[0] = y
    elif a == "a":
        p[1] -= 1
        if p[1] < 0:
            p[1] = 0
    elif a == "d":
        p[1] += 1
        if p[1] > x:
            p[1] = x


def equip_item(slot=None, item=None):
    if item is None:
        item = input("What item would you like to equip?\n>>>")
    if slot is None:
        slot = input("In what slot would you like to equip the item?\n>>>")
    player.equip_item(item, slot)


player = person.Person("player", 18, 180, [0, 0])
player.add_item(
    "weapon",
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
    draw_field(Field.field, player.position)

    # Even listening
    action = input().lower().split(' ')
    if action[0] in ["w", "a", "s", "d"]:
        os.system('cls')
        move(Field.field, player.position, action[0])
    if action[0] in ["i", "inv", "inventory"]:
        os.system('cls')
        player.check_inventory()
        functions.wait()
    if action[0] in ["equipment", "eq"]:
        os.system('cls')
        player.check_equipment()
        functions.wait()
    if action[0] in ['equip']:  # equip slot item
        os.system('cls')
        if 1 < len(action):
            if 2 < len(action):
                player.equip_item(action[2], action[1])
            else:
                equip_item(action[1])
        else:
            equip_item()
        functions.wait()
    if action[0] in ["exit", "quit"]:
        end_game = True
