"""Inventory class"""

from copy import deepcopy
from dataclasses import dataclass
from .item import Item

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
            self.items[item.id] = deepcopy(item)
        return self.items

    def add_items(self, items: list[Item]) -> dict[str:Item]:
        """Add multiple item"""
        for i in items:
            self.add_item(i)
        return self.items

    def get_item(self, item_id: str) -> Item:
        """Return item from an id"""
        return self.items[item_id]

    def search_item(self, name: str) -> list[Item]:
        """Return item from a name"""
        return [i for i in self.items.values() if i.name == name]

    def remove_item(self, item: Item, quentity: int=1) -> dict[str:Item]:
        """Remove an item from the inventory"""
        if item.id in self.items:
            item = self.get_item(item.id)
            item.quentity -= quentity
            if item.quentity <= 0:
                del self.items[item.id]
        return self.items

    def remove_items(self, items: list[Item]) -> dict[str:Item]:
        """Remove multiple item"""
        for i in items:
            self.remove_item(i, i.quentity)
        return self.items
