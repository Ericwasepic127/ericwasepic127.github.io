"""
loady - Loading Bar simulator!
Use for loading! 
Fun loads including!
Get and use! 
Simple! 
"""
# loady.py
from time import sleep as sl
from random import choice as ch
from itertools import cycle as cy

def loadbar(icon="", left=" ", long=25, sleeps=0.1):
    """
    Regular loading bar
    Arguments: 
        icon='' - What should display if increases 
        left=" " - What display left items
        long=25 - How longs 
        sleeps=0.1 - How long between loads
    """
    level = long - 1
    for a in range(long):
        dashes = icon * a
        spaces = left * level
        print(f'[{dashes}{spaces}]', end='\r')
        level -= 1
        sl(sleeps)
    print()

def funrandomerchapter(icon="0123456789", left=" ", long=25, sleeps=0.1):
    """
    Randomly selects from icon, then increase 
    Arguments: 
        icon='0123456789' - What should display if increases 
        left=" " - What display left items
        long=25 - How long
        sleeps=0.1 - How long between loads
    """
    level = long - 1
    for a in range(long):
        dashes = ch(icon) * a
        spaces = left * level
        print(f'[{dashes}{spaces}]', end='\r')
        level -= 1
        sl(sleeps)
    print()

def funconituner(icon="0123456789", left=" ", long=10, sleeps=0.1):
    """
    Loops from icon, increase 
    Arguments: 
        icon='0123456789' - What should display if increases 
        left=" " - What display left items
        long=10 - How longs 
        sleeps=0.1 - How long between loads
    """
    ico = cy(iter(icon))
    level = long - 1
    for a in range(long):
        dashes = next(ico) * a
        spaces = left * level
        print(f'[{dashes}{spaces}]', end='\r')
        level -= 1
        sl(sleeps)
    print()

def fundecrase(icon="", left=" ", long=25, sleeps=0.1):
    """
    Reversed loads
    Arguments: 
        icon='' - What should display if decreases 
        left=" " - What display left items
        long=25 - How longs 
        sleeps=0.1 - How long between loads
    """
    level = long - 1
    for a in range(long):
        dashes = left * a
        spaces = icon * level
        print(f'[{dashes}{spaces}]', end='\r')
        level -= 1
        sl(sleeps)
    print()

def funbetween(icon="#", left=" ", long=25, sleeps=(0.5, 0.1, 1, 3)):
    """
    Randomly selects from sleep range, then sleeps
    Arguments: 
        icon='#' - What should display if increases 
        left=" " - What display left items
        long=25 - How long
        sleeps=(0.5, 0.1, 1, 3) - How long between loads
    """
    level = long - 1
    for a in range(long):
        dashes = icon * a
        spaces = left * level
        print(f'[{dashes}{spaces}]', end='\r')
        level -= 1
        sl(ch(sleeps))
    print()

__all__ = {
    "loadbar": loadbar, 
    "funrandomerchapter": funrandomerchapter, 
    "funconituner": funconituner, 
    "fundecrase": fundecrase, 
    "funbetween": funbetween
}
__version__ = "V1.0"


