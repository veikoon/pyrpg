"""
Main class for items
"""

from dataclasses    import dataclass
from .effect        import Effect

@dataclass
class Item:
    """Generic class for items"""

    id             : str
    name           : str
    description    : str
    weight         : int = 0
    value          : int = 0
    quentity       : int = 1

    def __str__(self):
        return self.name

    def get_weight(self) -> int:
        """Get weigth with format"""
        return self.weight * self.quentity

    def get_value(self) -> int:
        """Get value with format"""
        return self.value * self.quentity

    def get_description(self) -> str:
        """Get full item descripttion"""
        return f"{self.name:<9} | {self.description}\n{self.get_weight():<9} | {self.get_value()}"

@dataclass
class Weapon(Item):
    """Generic weapon class"""

    dammage     : int = 1
    modifier    : int = 1
    effect      : Effect = None

    def get_dammage(self) -> int:
        """Dammage modifier"""
        return self.dammage * self.modifier

@dataclass
class Armor(Item):
    """Generic weapon class"""

    dammage_reduction   : int = 1
    modifier            : int = 1
    effect              : Effect = None

    def get_defense(self) -> int:
        """Defense accessor"""
        return self.dammage_reduction * self.modifier
