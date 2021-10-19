import time
import os
import msvcrt

os.system("mode con cols=54 lines=22")

class Player:
    def __init__(self):
        self.coo = 0
    def update(self, key, area):
        if(key == "up"):
            for i in range(3):
                area[(self.coo + i) % len(area)][0] = " "
            self.coo -= 1
            for i in range(3):
                area[(self.coo + i) % len(area)][0] = "|"
        elif(key == "down"):
            for i in range(3):
                area[(self.coo + i) % len(area)][0] = " "
            self.coo += 1
            for i in range(3):
                area[(self.coo + i) % len(area)][0] = "|"

class Game:
    
    def __init__(self):
        self.player = Player()
        self.isRunning = True
        self.area = []
        for i in range(20):
            self.area.append([" "]*50)
        self.play()
        
    def play(self):
        while self.isRunning:
            key = self.getKey()
            if(key != ""):
                self.player.update(key, self.area)
                self.draw()
            time.sleep(0.1)

    def getKey(self):
        arrow = False
        while(msvcrt.kbhit()):
            key = msvcrt.getch()
            if(key == b"\xe0"):
                arrow = True
            if(arrow == True and key == b"H"):
                return 'up'
            if(arrow == True and key == b"P"):
                return 'down'
        return ""
    
    def draw(self):
        #self.clear()
        print("")
        for i in range(len(self.area)):
            print("  ",end="")
            for j in range(len(self.area[i])):
                print(self.area[i][j], end="")
            print("")
            
    def clear(self):
        os.system("cls")
        

game = Game()

