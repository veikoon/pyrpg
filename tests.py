"""Test classes by instantiate each object"""

from copy import copy
from classes.character import Inventory, Caracteristics, Character
from classes.item import Item, Armor, Weapon

feather = Item(
    id              = "feather",
    name            = "Feather",
    description     = "A simple feather looted from a chicken.",
    weight          = 0,
    value           = 1
)

sword = Weapon(
    id              = "sword",
    name            = "Sword",
    description     = "A simple sword made from iron.",
    weight          = 1500,
    value           = 10,
    dammage         = 4
)

helmet = Armor(
    id              = "helmet",
    name            = "Leather helmet",
    description     = "A simple helmet made from leather.",
    weight          = 400,
    value           = 5,
    dammage_reduction = 4
)

player_inventory = Inventory()
player_inventory.add_item(feather)

player_caracteristics =  Caracteristics(
    strength = 12,
    dexterity = 12,
    constitution = 12,
    intelligence = 12,
    wisdom = 12,
    charisma = 12
)

player = Character(
    name = "vincent",
    last_name = "monnot",
    weapon = sword,
    armor = helmet,
    caracteristics = player_caracteristics,
    inventory = player_inventory
)

def print_player():
    """Print the player onbject as a dict"""
    print(player.__dict__)
    print(f"The inventory of the player value : {player.inventory.get_value()} grams !")
    print(f"The inventory of the player weigth : {player.inventory.get_weigth()} golds !")

def pickup_item():
    """Test looting features"""
    print(player.inventory.__dict__)
    feather_bag = copy(feather)
    feather_bag.quentity = 15
    player.inventory.add_item(feather_bag)
    gold_ingot = Item(
        id              = "gold_ingot",
        name            = "Gold ingot",
        description     = "A simple feather looted from a chicken.",
        weight          = 1000,
        value           = 1000
    )
    player.inventory.add_item(gold_ingot)
    print(player.inventory.__dict__)
    print(f"The inventory of the player value : {player.inventory.get_value()} grams !")
    print(f"The inventory of the player weigth : {player.inventory.get_weigth()} golds !")
