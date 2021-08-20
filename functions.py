from random import choice, randint


martial_weapons = [
    "battleaxe", "flail", "glaive", "greataxe", "greatsword", "halberd", "lance", "longsword", "maul", "morningstar", "pike", "rapier",
    "scimitar", "shortsword", "trident", "war pick", "warhammer", "whip"
 ]
simple_weapons = ["club", "dagger", "greatclub", "handaxe", "javelin", "light hammer", "mace", "quarterstaff", "sickle", "spear"]
instruments = ["bagpipes", "drum", "dulcimer", "flute", "lute", "lyre", "horn", "pan flute", "shawn", "viol"]
tools = [
    "alchemist’s supplies", "brewer's supplies", "calligrapher's supplies", "carpenter's tools", "cartographer's tools",
    "cobbler's tools", "cook's utensils", "glassblower's tools", "jewler's tools", "leatherworker's tools", "mason's tools",
    "painter's cupplies", "potter's tools", "smith's tools", "tinker's tools", "weaver's tools", "woodcarver's tools"
 ]

def pick_race(data):
    race = choice(data)
    return race


def pick_class(data):
    character_class = choice(data)
    return character_class


def pick_subclass(character_class):
    subclass = choice(character_class["subclasses"])
    return subclass


def pick_background(data):
    background = choice(data)
    return background


def add_equipment_from_class(character_class):
    equipment = []

    for i in character_class["equipment"]:
        item = choice(i)  # Choose a random selection in equipment
        if type(item) is list:  # Check to see if selection is a list
            for itm in item:  # loop through selection
                final = replace_item(itm)  # replace placeholder text, if any, with random item
                equipment.append(final)
        else:
            final = replace_item(item) # replace placeholder text, if any, with random item
            equipment.append(final)
    return equipment


def add_equipment_from_background(background):
    equipment = []
    for item in background["equipment"]:
        if type(item) is list:
            semi = choice(item)
            final = replace_item(semi)
            equipment.append(final)
        else:
            final = replace_item(item)
            equipment.append(final)
    return equipment


def replace_item(item):
    if item == "martial weapon":
        item = choice(martial_weapons)
    elif item == "simple weapon":
        item = choice(simple_weapons)
    elif item == "musical instrument":
        item = choice(instruments)
    elif item == "artisan tool":
        item = choice(tools)
    return item


def roll_for_stats():
    stats_array = []
    n_dice = 4
    dice_rank = 6
    for i in range(6):
        results = [  # Generate n_dice numbers between [1, dice_rank]
            randint(1, dice_rank) for n in range(n_dice)
        ]
        lowest = min(results)  # Find the lowest roll among the results
        results.remove(lowest)  # Remove the first instance of that lowest roll
        stats_array.append(sum(results))
    return stats_array