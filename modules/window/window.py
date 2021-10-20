"""
Window event / commands handler
"""

from platform import system

if(system == "Windows"):
    # Pour détecter les keypress (natif sous windows)
    from modules.window.vwin import *
else:
    # Sinon on utilise pynput
    from modules.window.vunix import *

handler = Handler()


def getKeyPress():
    return handler.getk()