"""Fichier contenant la classe Player"""

class Player:
    """
    L'objet 'joueur'
    """
    def __init__(self, area):
        """
        Mise en place des variables
        """
        # Coordonnées (en y) du joueur
        self.cooX = 0
        self.cooY = -1
        self.area = area
        self.char = "O"
        self.counter = 0

        self.update("down")

    def update(self, key):
        """
        Bouge le joueur si besoin
        key est la touche pressée (up / down...)
        area est un pointeur qui dirige vers la case mémoire de la liste contenant le jeu
        """

        # Si la touche est up (touche flechée vers le haut)
        if(key == "up" and self.cooY - 1 >= 0):

            # On supprime sur le jeu les caractères du joueur
            self.area[self.cooY][self.cooX] = " "

            # On change la position
            self.cooY -= 1

            # On redessine le joueur aux nouvelles coordonnées
            self.area[self.cooY][self.cooX] = "O"
            self.char = "O"
            self.counter = 0

        # Si la touche est down (touche flechée vers le bas)
        elif(key == "down" and self.cooY + 1 < len(self.area)):

            # On supprime sur le jeu les caractères du joueur
            self.area[self.cooY][self.cooX] = " "

            # On change la position
            self.cooY += 1

            # On redessine le joueur aux nouvelles coordonnées
            self.area[self.cooY][self.cooX] = "O"
            self.char = "O"
            self.counter = 0
        
        elif(key == "left" and self.cooX - 1 >= 0):

            # On supprime sur le jeu les caractères du joueur
            self.area[self.cooY][self.cooX] = " "

            # On change la position
            self.cooX -= 1

            # On redessine le joueur aux nouvelles coordonnées
            self.area[self.cooY][self.cooX] = "O"
            self.char = "O"
            self.counter = 0
        
        elif(key == "right" and self.cooX + 1 < len(self.area[0])):

            # On supprime sur le jeu les caractères du joueur
            self.area[self.cooY][self.cooX] = " "

            # On change la position
            self.cooX += 1

            # On redessine le joueur aux nouvelles coordonnées
            self.area[self.cooY][self.cooX] = "O"
            self.char = "O"
            self.counter = 0
        
        else:
            self.counter += 1
            if(self.counter % 5 == 0):
                if(self.char == "O"):
                    self.char = "o"
                else:
                    self.char = "O"
                self.area[self.cooY][self.cooX] = self.char
