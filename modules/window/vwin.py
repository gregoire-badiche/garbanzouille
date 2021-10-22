"""
The Windows version of window module
"""

import msvcrt
import os

class Handler:
    def __init__(self):
        pass
    def getk(self):
        arrow = False
        while(msvcrt.kbhit()):
            key = msvcrt.getch()
            if(key == b"\xe0"):
                arrow = True
            if(arrow == True and key == b"H"):
                return 'up'
            if(arrow == True and key == b"P"):
                return 'down'
            if(arrow == True and key == b"K"):
                return 'left'
            if(arrow == True and key == b"M"):
                return 'right'
        return ""

def resize(c, r):
    os.system("mode con cols=" + str(c) + " lines=" + str(r))

def clear():
    os.system('cls')
