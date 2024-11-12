"""
Utils functions globally accessible
"""

from random import randint

def roll(max_value: int) -> int:
    """Roll a custom dice"""
    result = randint(0, max_value)
    return result

def roll_4() -> int:
    """Roll a 4 dice"""
    return roll(4)

def roll_6() -> int:
    """Roll a 6 dice"""
    return roll(6)

def roll_8() -> int:
    """Roll a 8 dice"""
    return roll(8)

def roll_10() -> int:
    """Roll a 10 dice"""
    return roll(10)

def roll_12() -> int:
    """Roll a 12 dice"""
    return roll(12)

def roll_20() -> int:
    """Roll a 20 dice"""
    return roll(20)

def roll_100() -> int:
    """Roll a 100 dice"""
    return roll(100)

class Effect:
    """Class for special effect of weapon & armors"""

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
