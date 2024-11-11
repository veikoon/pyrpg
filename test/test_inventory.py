"""Unitary tests for player"""

import unittest
from copy import deepcopy
from classes.item import Item, Weapon
from classes.inventory import Inventory

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
        # New item
        __returned_inventory = _inventory.add_item(feather)
        self.assertEqual(_inventory.items, __returned_inventory)
        self.assertEqual(len(_inventory.items), 1)
        self.assertEqual(_inventory.get_size(), feather.quentity)
        self.assertEqual(_inventory.get_weigth(), feather.get_weight())
        self.assertEqual(_inventory.get_value(), feather.get_value())
        self.assertDictEqual(_inventory.items, {feather.id: feather})
        # Existing item
        __returned_inventory = _inventory.add_item(feather)
        self.assertEqual(len(_inventory.items), 1)
        self.assertEqual(_inventory.get_size(), feather.quentity * 2)
        self.assertEqual(_inventory.get_weigth(), feather.get_weight() * 2)
        self.assertEqual(_inventory.get_value(), feather.get_value() * 2)
        _feather = deepcopy(feather)
        _feather.quentity = _feather.quentity * 2
        self.assertDictEqual(_inventory.items, {_feather.id: _feather})


    def test_add_items(self):
        """Test picking up multiple items"""

        _inventory = deepcopy(self.inventory)
        __returned_inventory = _inventory.add_items([feather, sword])
        self.assertEqual(_inventory.items, __returned_inventory)
        self.assertEqual(len(_inventory.items), 2)
        self.assertEqual(_inventory.get_size(), feather.quentity + sword.quentity)
        self.assertEqual(_inventory.get_weigth(), feather.get_weight() + sword.get_weight())
        self.assertEqual(_inventory.get_value(), feather.get_value() + sword.get_value())
        self.assertDictEqual(_inventory.items, {feather.id: feather, sword.id: sword})

    def test_remove_item(self):
        """Test removing item"""

        _inventory = deepcopy(self.inventory)
        # Remove completely
        _inventory.add_item(feather)
        _inventory.remove_item(feather, feather.quentity)
        self.assertEqual(_inventory.items, self.inventory.items)

        # Remove partially
        _inventory.add_item(feather)
        _inventory.remove_item(feather)
        _feather = deepcopy(feather)
        _feather.quentity = _feather.quentity - 1
        self.assertEqual(_inventory.items, {_feather.id: _feather})

    def test_remove_items(self):
        """Test removing multiple item"""

        _inventory = deepcopy(self.inventory)
        # Remove completely
        _inventory.add_item(feather)
        _inventory.add_item(sword)
        _inventory.remove_items([feather, sword])
        self.assertEqual(_inventory.items, self.inventory.items)

    def test_get_item(self):
        """Test item accessor"""

        _inventory = deepcopy(self.inventory)
        _inventory.add_item(feather)
        _feather = _inventory.get_item(feather.id)
        self.assertEqual(feather, _feather)

    def test_search_item(self):
        """Test item search"""

        _inventory = deepcopy(self.inventory)
        _inventory.add_item(feather)
        _feather = _inventory.search_item(feather.name)[0]
        self.assertEqual(feather, _feather)
