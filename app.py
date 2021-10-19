"""
Import des librairies
"""

# Pour limiter la main loop
import time

# Pour effectuer des commandes comme clear / cls (efface la console) ou pour redimmentionner le terminal
import os

# Détection de l'OS
from platform import system as systemType
# Si c'est un Windows
if(systemType == "Windows"):
    # Pour détecter les keypress (natif sous windows)
    import msvcrt
else:
    # Sinon on utilise pynput
    import pynput

"""
Les objets du code (on fait de la POO ici ou quoi)
"""

class Player:
    """
    L'objet 'joueur'
    """
    def __init__(self):
        """
        Mise en place des variables
        """
        # Coordonnées (en y) du joueur
        self.coo = 0

    def update(self, key, area):
        """
        Bouge le joueur si besoin
        key est la touche pressée (up / down...)
        area est un pointeur qui dirige vers la case mémoire de la liste contenant le jeu
        """

        # Si la touche est up (touche flechée vers le haut)
        if(key == "up"):

            # On supprime sur le jeu les caractères du joueur
            for i in range(3):
                area[(self.coo + i) % len(area)][0] = " "

            # On change la position
            self.coo -= 1

            # On redessine le joueur aux nouvelles coordonnées
            for i in range(3):
                area[(self.coo + i) % len(area)][0] = "|"

        # Si la touche est down (touche flechée vers le bas)
        elif(key == "down"):

            # On supprime sur le jeu les caractères du joueur
            for i in range(3):
                area[(self.coo + i) % len(area)][0] = " "

            # On change la position
            self.coo += 1

            # On redessine le joueur aux nouvelles coordonnées
            for i in range(3):
                area[(self.coo + i) % len(area)][0] = "|"

class Game:
    """
    L'objet qui sert à gérer la zone de jeu, et le jeu en général plus facilement
    """

    def __init__(self):
        """
        Mise en place des variables + démarage de la partie
        """

        # Le joueur de la partie (on crée un nouvel objet de classe Player)
        self.player = Player()

        # Variable qui sert à controler la boucle principale
        self.isRunning = True

        # La zone de jeu
        # On l'initialise vide
        self.area = []
        # On crée 20 lignes...
        for i in range(20):
            # Contenant un caractère de chacune des 20 colonnes
            self.area.append([" "]*50)

        # Et on lance la partie
        self.play()
        
    def play(self):
        """
        Fonction principale, contenant la boucle principale
        """

        # Tant que isRunning est True
        while self.isRunning:

            # On veut savoir quelle touche à été pressée ("up", "down" ou "")
            key = self.getKey()

            # Si une touche a été pressée
            if(key != ""):
                # On update le joueur
                self.player.update(key, self.area)
                # On dessine le jeu dans la console
                self.draw()
            # Et on attend pour éviter de surcharger le processeur
            time.sleep(0.1)

    def getKey(self):
        """
        Fonction qui permet de savoir quel touche a été pressée (sous Windows)
        Le fonctionnement est un peu compliqué, venez me dm si vous voulez savoir
        """
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
            
    def clear(self):
        """
        Commande du système pour effacer le contenu de la console. Sous Linux et Mac, c'est 'clear'
        """
        os.system("cls")
        
# Si l'OS et Python sont prêt à lancer le jeu
if __name__ == "__main__":
    # On redimentionne la console
    if(systemType == "Windows"):
        os.system("mode con cols=54 lines=22")
    # On crée une nouvelle partie
    game = Game()