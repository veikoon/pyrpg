"""Player and NPC classes"""

from .item import Item, Weapon, Armor

class Inventory:
    """Inventory class"""

    def __init__(self, items: list[Item]=None):

        self.items      = items

        if self.items is None:
            self.items  = []

    def get_weigth(self) -> float:
        """Get the weight sum of all item in inventory"""
        return sum(i.weight for i in self.items)

    def get_value(self) -> float:
        """Get the value sum of all item in inventory"""
        return sum(i.value for i in self.items)


class Character:
    """Main class"""

    def __init__(self,
                 name :str,
                 last_name :str,
                 weight :float=60.0,
                 money: float=0.0,
                 life: int=100,
                 mana: int=100,
                 inventory: Inventory=None,
                 weapon: Weapon=None,
                 armor: Armor=None):

        self.name           = name.capitalize()
        self.last_name      = last_name.capitalize()
        self.weight         = weight
        self.money          = money
        self.life           = life
        self.mana           = mana
        self.inventory      = inventory
        self.weapon         = weapon
        self.armor          = armor

        if self.inventory is None:
            self.inventory = []

    def __str__(self):
        return f"{self.name} {self.last_name}"


