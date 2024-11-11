"""
Main file
"""
from commons.print import Printing, Style, Color, Background

def main():
    """Main class"""
    printing = Printing()
    printing.custom_print("Rouge", Color.RED)
    printing.custom_print("Normal")
    printing.custom_print("Rouge bold", Color.RED, Style.BOLD)
    printing.custom_print("Rouge bold bg white", Color.RED, Style.BOLD, Background.LIGHTGREY)

if __name__ == "__main__":
    main()
