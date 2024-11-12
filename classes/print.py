"""Custom printing class"""
from datetime import datetime
from enum import Enum

class Style(Enum):
    """Font style"""
    RESET = '\033[0m'
    BOLD = '\033[01m'
    DISABLE = '\033[02m'
    UNDERLINE = '\033[04m'
    REVERSE = '\033[07m'
    STRIKETHROUGH = '\033[09m'
    INVISIBLE = '\033[08m'

class Color(Enum):
    """Font color"""
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    ORANGE = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    LIGHTGREY = '\033[37m'
    DARKGREY = '\033[90m'
    LIGHTRED = '\033[91m'
    LIGHTGREEN = '\033[92m'
    YELLOW = '\033[93m'
    LIGHTBLUE = '\033[94m'
    PINK = '\033[95m'
    LIGHTCYAN = '\033[96m'

class Background(Enum):
    """Background color"""
    BLACK = '\033[40m'
    RED = '\033[41m'
    GREEN = '\033[42m'
    ORANGE = '\033[43m'
    BLUE = '\033[44m'
    PURPLE = '\033[45m'
    CYAN = '\033[46m'
    LIGHTGREY = '\033[47m'

class Printing:
    """Printing class"""

    def log(self, text):
        """Write log in file"""
        with open("save/game1.log", "a", encoding="UTF-8") as f:
            f.write(f"{datetime.now():%d-%m-%Y %M:%H} - {text}\n")

    def custom_print(self,
            text: str,
            color: Color=None,
            style: Style=None,
            background: Background=None):
        """Custom printing"""

        _color = '' if not color else color.value
        _style = '' if not style else style.value
        _background = '' if not background else background.value
        _text = f"{_color}{_style or ''}{_background or ''}{text}{Style.RESET.value}"
        self.log(text)
        print(_text)

    def print(self, text):
        """Normal print"""
        self.log(text)
        print(text)
