# Détection de l'OS
from platform import system as systemType
# Si c'est un Windows

y = 0

class WindowsListener:
    def __init__(self):
        self.run()
    def run(self):
        while True:
            if(msvcrt.kbhit()):
                print(msvcrt.getch())

class PynputListener:
    def __init__(self):
        with Listener(on_press=self.on_press) as self.listener:  # Create an instance of Listener
            self.listener.join()
    def on_press(self, key):
        print(key)


if(systemType() == "Windows"):
    # Pour détecter les keypress (natif sous windows)
    import msvcrt
    y = WindowsListener()

else:
    # Sinon on utilise pynput
    from pynput.keyboard import Listener
    y = PynputListener()
