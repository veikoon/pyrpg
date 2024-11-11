"""Player and NPC classes"""

from dataclasses import dataclass
from .item import Item, Weapon, Armor

@dataclass
class Inventory:
    """Inventory class"""

    items : dict[str:Item] = None

    def __post_init__(self):

        if self.items is None:
            self.items  = {}

    def get_weigth(self) -> float:
        """Get the weight sum of all item in inventory"""
        return sum(i.get_weight() for i in self.items.values())

    def get_value(self) -> float:
        """Get the value sum of all item in inventory"""
        return sum(i.get_value() for i in self.items.values())

    def add_item(self, item: Item) -> dict[str:Item]:
        """Add an item to the inventory"""
        if item.name in self.items:
            self.items[item.id].quentity += item.quentity
        else:
            self.items[item.id] = item

    def add_items(self, items : list[Item]) -> dict[str:Item]:
        """Add multiple item"""
        for i in items:
            self.add_item(i)

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
