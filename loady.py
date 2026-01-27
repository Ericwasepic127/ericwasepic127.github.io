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

def loadbar(icon="", long=25, sleeps=0.1):
    """
    Regular loading bar
    Arguments: 
        icon='' - What should display if increases 
        long=25 - How longs 
        sleeps=0.1 - How long between loads
    """
    level = long - 1
    for a in range(long):
        dashes = icon * a
        spaces = ' ' * level
        print(f'[{dashes}{spaces}]', end='\r')
        level -= 1
        sl(sleeps)
    print("\n")

def funrandomerchapter(icon="0123456789", long=25, sleeps=0.1):
    """
    Randomly selects from icon, then increase 
    Arguments: 
        icon='0123456789' - What should display if increases 
        long=25 - How long
        sleeps=0.1 - How long between loads
    """
    level = long - 1
    for a in range(long):
        dashes = ch(icon) * a
        spaces = ' ' * level
        print(f'[{dashes}{spaces}]', end='\r')
        level -= 1
        sl(0.1)
    print("\n")

def funconituner(icon="0123456789", long=10, sleeps=0.1):
    """
    Loops from icon, increase 
    Arguments: 
        icon='0123456789' - What should display if increases 
        long=10 - How longs 
        sleeps=0.1 - How long between loads
    """
    ico = cy(iter(icon))
    level = long - 1
    for a in range(long):
        dashes = next(ico) * a
        spaces = ' ' * level
        print(f'[{dashes}{spaces}]', end='\r')
        level -= 1
        sl(sleeps)
    print("\n")

def fundecrase(icon="", long=25, sleeps=0.1):
    """
    Reversed loads
    Arguments: 
        icon='' - What should display if decreases 
        long=25 - How longs 
        sleeps=0.1 - How long between loads
    """
    level = long - 1
    for a in range(long):
        dashes = ' ' * a
        spaces = icon * level
        print(f'[{dashes}{spaces}]', end='\r')
        level -= 1
        sl(sleeps)
    print("\n")

def funbetween(icon="#", long=25, sleeps=(0.5, 0.1, 1, 3)):
    """
    Randomly selects from sleep range, then sleeps
    Arguments: 
        icon='#' - What should display if increases 
        long=25 - How long
        sleeps=(0.5, 0.1, 1, 3) - How long between loads
    """
    level = long - 1
    for a in range(long):
        dashes = icon * a
        spaces = ' ' * level
        print(f'[{dashes}{spaces}]', end='\r')
        level -= 1
        sl(ch(sleeps))
    print("\n")

__all__ = {
    "loadbar": loadbar, 
    "funrandomerchapter": funrandomerchapter, 
    "funconituner": funconituner, 
    "fundecrase": fundecrase, 
    "funbetween": funbetween
}
__version__ = "V1.0"

print("Welcome to my project: loady")
print("Arguments:", ", ".join(__all__.keys()))
