"""Unitary tests for player"""

import unittest
from copy import deepcopy
from classes.character import Inventory, Caracteristics, Character
from classes.item import Item, Armor, Weapon

feather = Item(
    id              = "feather",
    name            = "Feather",
    description     = "A simple feather looted from a chicken.",
    weight          = 0,
    value           = 1,
    quentity        = 2
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

class TestInventory(unittest.TestCase):
    """Main class to test inventory"""

    inventory = Inventory()

    def test_default_value(self):
        """Test defaults values"""

        self.assertDictEqual(self.inventory.items, {})
        self.assertEqual(self.inventory.get_size(), 0)
        self.assertEqual(self.inventory.get_weigth(), 0)
        self.assertEqual(self.inventory.get_value(), 0)
        self.assertEqual(self.inventory.max_size, 40)

    def test_add_item(self):
        """Test picking up an item"""

        _inventory = deepcopy(self.inventory)
        __returned_inventory = _inventory.add_item(feather)
        self.assertEqual(_inventory.items, __returned_inventory)
        self.assertEqual(len(_inventory.items), 1)
        self.assertEqual(_inventory.get_size(), feather.quentity)
        self.assertEqual(_inventory.get_weigth(), feather.get_weight())
        self.assertEqual(_inventory.get_value(), feather.get_value())
        self.assertDictEqual(_inventory.items, {feather.id: feather})
