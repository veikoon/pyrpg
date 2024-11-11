"""Unitary tests for character"""

import unittest
from copy import deepcopy
from classes.item import Item, Armor, Weapon
from classes.inventory import Inventory
from classes.character import Caracteristics, Character

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

feather = Item(
    id              = "feather",
    name            = "Feather",
    description     = "A simple feather looted from a chicken.",
    weight          = 0,
    value           = 1,
    quentity        = 2
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

class TestCharacteristic(unittest.TestCase):
    """Main class to test characteristics"""

    caracteristics = deepcopy(player_caracteristics)

    def test_add_all_modifier(self):
        """Test add_all_modifier fucntion"""
        _caracteristics = deepcopy(self.caracteristics)
        _caracteristics.add_all_modifier(-12)
        self.assertEqual(_caracteristics.get_strength(), 0)
        self.assertEqual(_caracteristics.get_dexterity(), 0)
        self.assertEqual(_caracteristics.get_constitution(), 0)
        self.assertEqual(_caracteristics.get_intelligence(), 0)
        self.assertEqual(_caracteristics.get_wisdom(), 0)
        self.assertEqual(_caracteristics.get_charisma(), 0)

    def test_random_rolls_failed(self):
        """Test random roll failed by setting the stats at 0"""
        _caracteristics = deepcopy(self.caracteristics)
        _caracteristics.add_all_modifier(-12)
        self.assertEqual(_caracteristics.roll_strength(), False)
        self.assertEqual(_caracteristics.roll_dexterity(), False)
        self.assertEqual(_caracteristics.roll_constitution(), False)
        self.assertEqual(_caracteristics.roll_intelligence(), False)
        self.assertEqual(_caracteristics.roll_wisdom(), False)
        self.assertEqual(_caracteristics.roll_charisma(), False)

    def test_random_rolls_success(self):
        """Test random roll success by setting the stats at 20"""
        _caracteristics = deepcopy(self.caracteristics)
        _caracteristics.add_all_modifier(8)
        self.assertEqual(_caracteristics.roll_strength(), True)
        self.assertEqual(_caracteristics.roll_dexterity(), True)
        self.assertEqual(_caracteristics.roll_constitution(), True)
        self.assertEqual(_caracteristics.roll_intelligence(), True)
        self.assertEqual(_caracteristics.roll_wisdom(), True)
        self.assertEqual(_caracteristics.roll_charisma(), True)


#class TestCharacter(unittest.TestCase):
#    """Main class to test character"""
#
#    player = Character(
#        name = "Veikoon",
#        last_name = "Tulma",
#        weapon = sword,
#        armor = helmet,
#        caracteristics = player_caracteristics,
#        inventory = player_inventory
#    )
