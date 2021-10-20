"""
Fichier principal du jeu

Import des librairies
"""

# Pour limiter la main loop
import time

# Pour effectuer des commandes comme clear / cls (efface la console) ou pour redimmentionner le terminal
import os

# Import du module pour gérer le cross-platform
import modules.window.window as window

"""
Les objets du code (on fait de la POO ici ou quoi)
"""

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
            for i in range(3):
                self.area[self.cooY][self.cooX] = "O"

        # Si la touche est down (touche flechée vers le bas)
        elif(key == "down" and self.cooY + 1 < len(self.area)):

            # On supprime sur le jeu les caractères du joueur
            self.area[self.cooY][self.cooX] = " "

            # On change la position
            self.cooY += 1

            # On redessine le joueur aux nouvelles coordonnées
            for i in range(3):
                self.area[self.cooY][self.cooX] = "O"
        
        elif(key == "left" and self.cooX - 1 >= 0):

            # On supprime sur le jeu les caractères du joueur
            self.area[self.cooY][self.cooX] = " "

            # On change la position
            self.cooX -= 1

            # On redessine le joueur aux nouvelles coordonnées
            for i in range(3):
                self.area[self.cooY][self.cooX] = "O"
        
        elif(key == "right" and self.cooX + 1 < len(self.area[0])):

            # On supprime sur le jeu les caractères du joueur
            self.area[self.cooY][self.cooX] = " "

            # On change la position
            self.cooX += 1

            # On redessine le joueur aux nouvelles coordonnées
            for i in range(3):
                self.area[self.cooY][self.cooX] = "O"

class Game:
    """
    L'objet qui sert à gérer la zone de jeu, et le jeu en général plus facilement
    """

    def __init__(self):
        """
        Mise en place des variables + démarage de la partie
        """

        # Variable qui sert à controler la boucle principale
        self.isRunning = True

        # La zone de jeu
        # On l'initialise vide
        self.area = []
        # On crée 20 lignes...
        for i in range(20):
            # Contenant un caractère de chacune des 20 colonnes
            self.area.append([" "]*50)
        
        # Le joueur de la partie (on crée un nouvel objet de classe Player)
        self.player = Player(self.area)

        # Et on lance la partie
        self.play()
        
    def play(self):
        """
        Fonction principale, contenant la boucle principale
        """

        self.draw()

        # Tant que isRunning est True
        while self.isRunning:
            # On veut savoir quelle touche à été pressée ("up", "down" ou "")
            key = window.getKeyPress()

            # # Si une touche a été pressée
            if(key != ""):
            # On update le joueur
                self.player.update(key)
                window.clear()
                # On dessine le jeu dans la console
                self.draw()
            # Et on attend pour éviter de surcharger le processeur
            time.sleep(0.1)
    
    def draw(self):
        """
        Affiche la grille de jeu (self.area) dans la console, avec une marge de 1 ligne au dessus et
        de 2 caractères sur les côtés
        """

        # Affiche la marge du dessus
        print("")

        # Boucle qui parcourt chaque ligne
        for i in range(len(self.area)):

            # Marge à gauche (il n'y a pas besoin d'en mettre une à droite)
            print("  ",end="")

            # Boucle qui parcourt chaque caractères de chaque ligne
            for j in range(len(self.area[i])):

                # On affiche le caractère
                print(self.area[i][j], end="")
            
            # Retour à la ligne (+ marge du dessous pour la dernière ligne)
            print("")
        
# Si l'OS et Python sont prêt à lancer le jeu
if __name__ == "__main__":
    # On redimentionne la console
    window.resize(54, 22)
    # On crée une nouvelle partie
    game = Game()

#test :D