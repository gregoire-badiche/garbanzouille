"""
The UNIX version of the window module
"""

from pynput.keyboard import Listener, Key
import os
import time

class Handler:
    def __init__(self):
        self.listener = Listener(on_press=self.on_press)
        self.listener.start()
        self.key = ""
    def on_press(self, key):
        self.key = key
    def getk(self):
        x = self.convertk(self.key)
        self.key = ""
        return x
    def convertk(self, key):
        if(key == Key.up):
            return "up"
        elif(key == Key.down):
            return "down"
        elif(key == Key.left):
            return "left"
        elif(key == Key.right):
            return "right"
        else:
            return ""

def resize(c, r):
    clear()
    col, row = os.get_terminal_size()
    if(col != c or row != r):
        print("Hey, j'ai pas trouvé comment redimmensionner le terminal sous UNIX...")
        print("tu va donc devoir le faire manuellement :D")
        print("Fais en sorte que le cadre suive les bords de ton terminal")
        print("Une fois que cela est fait, appuye sur la touche entrée pour jouer")
        input("Appuye sur la touche entrée pour continuer")
        clear()
        for i in range(c):
            print("-", end="")
        for i in range(r - 2):
            print("|", end="")
            for i in range(c - 2):
                print(" ", end="")
            print("|", end="")
        for i in range(c):
            print("-", end="")
        input()
        clear()

def clear():
    os.system("clear")