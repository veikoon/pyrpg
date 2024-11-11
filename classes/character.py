"""Player and NPC classes"""

from dataclasses import dataclass
from commons.utils import roll_20
from classes.item import Weapon, Armor, Item
from classes.inventory import Inventory

@dataclass
class Caracteristics:
    """Characteristics of a living creature"""

    # pylint: disable=too-many-instance-attributes
    # More readable when all characteristics are in the same class

    strength        : int = 10
    dexterity       : int = 10
    constitution    : int = 10
    intelligence    : int = 10
    wisdom          : int = 10
    charisma        : int = 10

    strength_bonus       : int = 0
    dexterity_bonus      : int = 0
    constitution_bonus   : int = 0
    intelligence_bonus   : int = 0
    wisdom_bonus         : int = 0
    charisma_bonus       : int = 0

    def get_strength(self) -> int:
        """Strength accessor"""
        return self.strength + self.strength_bonus

    def get_dexterity(self) -> int:
        """Dexterity accessor"""
        return self.dexterity + self.dexterity_bonus

    def get_constitution(self) -> int:
        """Cnstitution accessor"""
        return self.constitution + self.constitution_bonus

    def get_intelligence(self) -> int:
        """Intelligence accessor"""
        return self.intelligence + self.intelligence_bonus

    def get_wisdom(self) -> int:
        """Wisdom accessor"""
        return self.wisdom + self.wisdom_bonus

    def get_charisma(self) -> int:
        """Charisma accessor"""
        return self.charisma + self.charisma_bonus

    def roll_strength(self) -> bool:
        """Roll a 20 dice under strength"""
        return roll_20() < self.get_strength()

    def roll_dexterity(self) -> bool:
        """Roll a 20 dice under dexterity"""
        return roll_20() < self.get_dexterity()

    def roll_constitution(self) -> bool:
        """Roll a 20 dice under constitution"""
        return roll_20() < self.get_constitution()

    def roll_intelligence(self) -> bool:
        """Roll a 20 dice under intelligence"""
        return roll_20() < self.get_intelligence()

    def roll_wisdom(self) -> bool:
        """Roll a 20 dice under wisdom"""
        return roll_20() < self.get_wisdom()

    def roll_charisma(self) -> bool:
        """Roll a 20 dice under charisma"""
        return roll_20() < self.get_charisma()

    def add_all_bonus(self, bonus):
        """Add a modifier to all characteristics modifier"""
        self.strength_bonus      += bonus
        self.dexterity_bonus     += bonus
        self.constitution_bonus  += bonus
        self.intelligence_bonus  += bonus
        self.wisdom_bonus        += bonus
        self.charisma_bonus      += bonus

@dataclass
class Equipment:
    """Equipment of a character"""
    inventory       : Inventory = None
    weapon          : Weapon = None
    armor           : Armor = None

    def __post_init__(self):
        if self.inventory is None:
            self.inventory = Inventory()

@dataclass
class Statistics:
    """Statistics of a character"""

    # pylint: disable=too-many-instance-attributes

    life            : int = 100
    life_bonus      : int = 0
    life_modifier   : int = 1
    mana            : int = 100
    mana_bonus      : int = 0
    mana_modifier   : int = 1
    armor_bonus     : int = 0
    armor_modifier  : int = 1
    dammage_bonus   : int = 0
    dammage_modifier: int = 1

@dataclass
class Character:
    """Main character class"""

    name            : str
    last_name       : str
    weight          : int = 60
    money           : int = 0
    caracteristics  : Caracteristics = None
    statistics      : Statistics = None
    equipment       : Equipment = None


    def __post_init__(self):
        self.name = self.name.capitalize()
        self.last_name = self.last_name.capitalize()

        if self.equipment is None:
            self.equipment = Equipment()

        if self.caracteristics is None:
            self.caracteristics = Caracteristics()

        if self.statistics is None:
            self.statistics = Statistics()

    def get_calculated_stat(self, flat: int, bonus: int, modifier: int) -> int:
        """Calcul to get the real stat"""
        return (flat + bonus) * modifier

    def get_mana(self) -> int:
        """Mana accessor"""
        return self.get_calculated_stat(
            self.statistics.mana,
            self.statistics.mana_bonus,
            self.statistics.mana_modifier)

    def get_life(self) -> int:
        """Life accessor"""
        return self.get_calculated_stat(
            self.statistics.life,
            self.statistics.life_bonus,
            self.statistics.life_modifier)

    def get_defense(self) -> int:
        """Defense accessor"""
        return self.get_calculated_stat(
            self.get_armor().get_defense(),
            self.statistics.armor_bonus,
            self.statistics.armor_modifier)

    def get_damage(self) -> int:
        """Dammage accessor"""
        return self.get_calculated_stat(
            self.get_weapon().get_dammage(),
            self.statistics.dammage_bonus,
            self.statistics.dammage_modifier)

    def get_inventory(self) -> Inventory:
        """Inventory accessor"""
        return self.equipment.inventory

    def get_weapon(self) -> Weapon:
        """Weapon accessor"""
        return self.equipment.weapon

    def get_armor(self) -> Armor:
        """Armor accessor"""
        return self.equipment.armor

    def give(self, item: Item):
        """Add an item to the character inventory"""
        self.get_inventory().add_item(item)

    def drop(self, item: Item):
        """Remove an item from the character inventory"""
        self.get_inventory().remove_item(item)

    def __str__(self):
        return f"{self.name} {self.last_name}"
