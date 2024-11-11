"""Unitary tests for character"""

import unittest
from copy import deepcopy
from classes.item import Item, Armor, Weapon
from classes.inventory import Inventory
from classes.character import Equipment, Statistics, Caracteristics, Character

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

player_equipment = Equipment()
player_equipment.armor = helmet
player_equipment.weapon = sword
player_equipment.inventory = player_inventory

player_statistics = Statistics()

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

    def test_add_all_bonus(self):
        """Test add_all_modifier fucntion"""
        _caracteristics = deepcopy(self.caracteristics)
        _caracteristics.add_all_bonus(-12)
        self.assertEqual(_caracteristics.get_strength(), 0)
        self.assertEqual(_caracteristics.get_dexterity(), 0)
        self.assertEqual(_caracteristics.get_constitution(), 0)
        self.assertEqual(_caracteristics.get_intelligence(), 0)
        self.assertEqual(_caracteristics.get_wisdom(), 0)
        self.assertEqual(_caracteristics.get_charisma(), 0)

    def test_random_rolls_failed(self):
        """Test random roll failed by setting the stats at 0"""
        _caracteristics = deepcopy(self.caracteristics)
        _caracteristics.add_all_bonus(-12)
        self.assertEqual(_caracteristics.roll_strength(), False)
        self.assertEqual(_caracteristics.roll_dexterity(), False)
        self.assertEqual(_caracteristics.roll_constitution(), False)
        self.assertEqual(_caracteristics.roll_intelligence(), False)
        self.assertEqual(_caracteristics.roll_wisdom(), False)
        self.assertEqual(_caracteristics.roll_charisma(), False)

    def test_random_rolls_success(self):
        """Test random roll success by setting the stats at 20"""
        _caracteristics = deepcopy(self.caracteristics)
        _caracteristics.add_all_bonus(8)
        self.assertEqual(_caracteristics.roll_strength(), True)
        self.assertEqual(_caracteristics.roll_dexterity(), True)
        self.assertEqual(_caracteristics.roll_constitution(), True)
        self.assertEqual(_caracteristics.roll_intelligence(), True)
        self.assertEqual(_caracteristics.roll_wisdom(), True)
        self.assertEqual(_caracteristics.roll_charisma(), True)


class TestCharacter(unittest.TestCase):
    """Main class to test character"""
    # pylint: disable=line-too-long

    player = Character(
        name = "Veikoon",
        last_name = "Tulma",
        caracteristics = player_caracteristics,
        statistics = player_statistics,
        equipment = player_equipment,
    )

    def test_empty_character(self):
        """Mock npc creation"""
        npc = Character("James", "Smith")
        npc.give(feather)
        self.assertEqual(npc.get_inventory(), Inventory({feather.id: feather}))

    def test_get_calculated_stat(self):
        """Test calcul"""
        self.assertEqual(self.player.get_calculated_stat(1,2,3), 9)
        self.assertEqual(self.player.get_calculated_stat(3,2,1), 5)
        self.assertEqual(self.player.get_calculated_stat(1,3,2), 8)

    def test_life_statistic(self):
        """Test statistics calculs"""
        _player = deepcopy(self.player)
        _player.statistics.life_bonus = 20
        _player.statistics.life_modifier = 1.25
        self.assertEqual(_player.get_life(), (_player.statistics.life + _player.statistics.life_bonus) * _player.statistics.life_modifier)

    def test_mana_statistic(self):
        """Test statistics calculs"""
        _player = deepcopy(self.player)
        _player.statistics.mana_bonus = 20
        _player.statistics.mana_modifier = 1.25
        self.assertEqual(_player.get_mana(), (_player.statistics.mana + _player.statistics.mana_bonus) * _player.statistics.mana_modifier)

    def test_armor_statistic(self):
        """Test statistics calculs"""
        _player = deepcopy(self.player)
        _player.statistics.armor_bonus = 20
        _player.statistics.armor_modifier = 1.25
        self.assertEqual(_player.get_defense(), (_player.equipment.armor.dammage_reduction + _player.statistics.armor_bonus) * _player.statistics.armor_modifier)

    def test_weapon_statistic(self):
        """Test statistics calculs"""
        _player = deepcopy(self.player)
        _player.statistics.dammage_bonus = 20
        _player.statistics.dammage_modifier = 1.25
        self.assertEqual(_player.get_damage(), (_player.equipment.weapon.dammage + _player.statistics.dammage_bonus) * _player.statistics.dammage_modifier)

    def test_equipment_accessors(self):
        """Test accessors"""
        self.assertEqual(self.player.get_armor(), helmet)
        self.assertEqual(self.player.get_weapon(), sword)
        self.assertEqual(self.player.get_inventory(), player_inventory)
        