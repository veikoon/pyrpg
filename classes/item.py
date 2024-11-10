"""
Main class for items
"""

class Item:
    """Generic class for items"""
    def __init__(self, name :str, description :str, weight :float=0.0, value: float=0.0):

        self.name           = name.capitalize()
        self.description    = description
        self.weight         = weight
        self.value          = value

    def __str__(self):
        return self.name

    def get_weight(self) -> str:
        """Get weigth with format"""
        return f"{self.weight / 1000} kg" if self.weight > 1000 else f"{self.weight} g"

    def get_value(self) -> str:
        """Get value with format"""
        return f"{self.value} golds"

    def get_description(self) -> str:
        """Get full item descripttion"""
        return f"{self.name:<9} | {self.description}\n{self.get_weight():<9} | {self.get_value()}"

class Weapon(Item):
    """Generic weapon class"""

    def __init__(self, name :str,
                 description :str,
                 weight :float,
                 value: float,
                 dammage: int=1,
                 modifier: int=1,
                 effect=None):

        Item.__init__(name, description, weight, value)
        self.dammage    = dammage
        self.modifier   = modifier
        self.effect     = effect

class Armor(Item):
    """Generic weapon class"""

    def __init__(self, name :str,
                 description :str,
                 weight :float,
                 value: float,
                 dammage_reduction: int=1,
                 modifier: int=1,
                 effect=None):

        Item.__init__(name, description, weight, value)
        self.dammage_reduction  = dammage_reduction
        self.modifier           = modifier
        self.effect             = effect
