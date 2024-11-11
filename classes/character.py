"""Player and NPC classes"""

from dataclasses import dataclass
from commons.utils import roll_20
from classes.item import Weapon, Armor
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

    strength_modifier       : int = 0
    dexterity_modifier      : int = 0
    constitution_modifier   : int = 0
    intelligence_modifier   : int = 0
    wisdom_modifier         : int = 0
    charisma_modifier       : int = 0

    def get_strength(self) -> int:
        """Strength accessor"""
        return self.strength + self.strength_modifier

    def get_dexterity(self) -> int:
        """Dexterity accessor"""
        return self.dexterity + self.dexterity_modifier

    def get_constitution(self) -> int:
        """Cnstitution accessor"""
        return self.constitution + self.constitution_modifier

    def get_intelligence(self) -> int:
        """Intelligence accessor"""
        return self.intelligence + self.intelligence_modifier

    def get_wisdom(self) -> int:
        """Wisdom accessor"""
        return self.wisdom + self.wisdom_modifier

    def get_charisma(self) -> int:
        """Charisma accessor"""
        return self.charisma + self.charisma_modifier

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

    def add_all_modifier(self, modifier):
        """Add a modifier to all characteristics modifier"""
        self.strength_modifier      += modifier
        self.dexterity_modifier     += modifier
        self.constitution_modifier  += modifier
        self.intelligence_modifier  += modifier
        self.wisdom_modifier        += modifier
        self.charisma_modifier      += modifier

@dataclass
class Character:
    """Main character class"""

    # pylint: disable=too-many-instance-attributes
    # Naaaah pylint it's ok trust me

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
