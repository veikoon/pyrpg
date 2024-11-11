"""Player and NPC classes"""

from dataclasses import dataclass
from .item import Item, Weapon, Armor

@dataclass
class Inventory:
    """Inventory class"""

    items       : dict[str:Item] = None
    max_size    : int = 40


    def __post_init__(self):

        if self.items is None:
            self.items  = {}

    def get_weigth(self) -> float:
        """Get the weight sum of all item in inventory"""
        return sum(i.get_weight() for i in self.items.values())

    def get_value(self) -> float:
        """Get the value sum of all item in inventory"""
        return sum(i.get_value() for i in self.items.values())

    def get_size(self) -> int:
        """Get the quentity of item"""
        return sum(i.quentity for i in self.items.values())

    def add_item(self, item: Item) -> dict[str:Item]:
        """Add an item to the inventory"""
        if item.id in self.items:
            self.items[item.id].quentity += item.quentity
        else:
            self.items[item.id] = item
        return self.items

    def add_items(self, items: list[Item]) -> dict[str:Item]:
        """Add multiple item"""
        for i in items:
            self.add_item(i)
        return self.items

    def get_item(self, id: str) -> Item:
        """Return item from an id"""
        return self.items[id]

    def search_item(self, name: str) -> list[Item]:
        """Return item from a name"""
        return [i for i in self.items.values() if i.name == name]

    def remove_item(self, item_id: str, quentity: int=1) -> dict[str:Item]:
        """Remove an item from the inventory"""
        if item_id in self.items:
            item = self.get_item(item_id)
            item.quentity -= quentity
            if item.quentity <= 0:
                del self.items[item_id]
        return self.items

    def remove_items(self, items: list[str]) -> dict[str:Item]:
        """Remove multiple item"""
        for i in items:
            self.remove_item(i)
        return self.items

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
