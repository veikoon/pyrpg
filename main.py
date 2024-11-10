"""
Main file
"""
from classes.item import Item

def main():
    """Main class"""
    sword = Item(
        name            = "Sword",
        description     = "A simple sword made in iron.",
        weight          = 1500,
        value           = 10
    )

    print(sword.get_description())

if __name__ == "__main__":
    main()
