"""Player and NPC classes"""

from dataclasses import dataclass
from .item import Item, Weapon, Armor
from .inventory import Inventory
from copy import deepcopy

@dataclass
class Caracteristics:
    """Characteristics of a living creature"""

    strength        : int = 10
    dexterity       : int = 10
    constitution    : int = 10
    intelligence    : int = 10
    wisdom          : int = 10
    charisma        : int = 10

@dataclass
class Character:
    """Main character class"""

    name            : str
    last_name       : str
    weight          : int = 60
    money           : int = 0
    life            : int = 100
    mana            : int = 100
    caracteristics  : Caracteristics = None
    inventory       : Inventory = None
    weapon          : Weapon = None
    armor           : Armor = None

    def __post_init__(self):
        self.name = self.name.capitalize()
        self.last_name = self.last_name.capitalize()

        if self.inventory is None:
            self.inventory = []

        if self.caracteristics is None:
            self.caracteristics = Caracteristics()

    def __str__(self):
        return f"{self.name} {self.last_name}"
