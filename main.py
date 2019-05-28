import player
import fieldgen
import creature
import constants
import functions
import item
import os

# ========== Pre-game initialisation ========== #
object_list = []


# ========== Functions ========== #
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
        elif does_collide(object_list):
            moved.position[0] += 1
    elif a == "s" and not does_collide(object_list):
        moved.position[0] += 1
        if moved.position[0] > y:
            moved.position[0] = y
        elif does_collide(object_list):
            moved.position[0] -= 1
    elif a == "a" and not does_collide(object_list):
        moved.position[1] -= 1
        if moved.position[1] < 0:
            moved.position[1] = 0
        elif does_collide(object_list):
            moved.position[1] += 1
    elif a == "d" and not does_collide(object_list):
        moved.position[1] += 1
        if moved.position[1] > x:
            moved.position[1] = x
        elif does_collide(object_list):
            moved.position[1] -= 1
    return moved.position


def equip_item(slot=None, item=None):
    if item is None:
        item = input("What item would you like to equip?\n>>>")
    if slot is None:
        slot = input("In what slot would you like to equip the item?\n>>>")
    player.equip_item(item, slot)


def does_collide(objects):
    collision = False
    iterobj = next(iter(objects))
    for obj in objects:
        if obj != iterobj:  # Checks if you are not comparing same objects
            if iterobj.position == obj.position:  # Checks if any objects have the same position
                collision = True
                if issubclass(type(obj), item.Item):
                    obj.pick_up(iterobj)
                    object_list.remove(obj)
                    collision = False
    return collision


# ========== Initialisation ========== #
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
Field = fieldgen.Field(30, 10, constants.empty_terrain)
field_empty = Field.copy_field()

# ========== Game loop ========== #
# Since game doesn't use tick or frames, the game won't loop
# unless userinput(event) is given.
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
        elif action in ["i", "inv", "inventory"]:
            os.system('cls')
            player.check_inventory()
            functions.wait()
        elif action in ["equipment", "eq"]:
            os.system('cls')
            player.check_equipment()
            functions.wait()
        elif action in ['equip']:  # equip slot item
            os.system('cls')
            if 1 < len(actions):
                if 2 < len(actions):
                    player.equip_item(actions[2], actions[1])
                else:
                    equip_item(actions[1])
            else:
                equip_item()
            functions.wait()
        elif action in ["exit", "quit"]:
            end_game = True

        does_collide(object_list)
