"""Fichier contenant la classe Game"""

# Import du module pour gérer le cross-platform
import modules.window.window as window

# Pour limiter la main loop
import time

#Pour la gestion des modules
import sys

# Pour effectuer des commandes comme clear / cls (efface la console) ou pour redimmentionner le terminal
import os

#Bloc important les objets du code. A réutililser dans tous les modules créant un objet nécessitant la gestion d'autres objets.
sys.path.append(os.path.abspath('objets'))
for i in sorted(os.listdir(os.path.abspath('objets'))):
    if not i.startswith('_'):
        exec('from %s import *' %(i[:-3]))
        print('imported %s' %(i))

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

        # On dessine une première fois le jeu
        self.draw()

        # Tant que isRunning est True
        while self.isRunning:
            # On veut savoir quelle touche à été pressée ("up", "down" ou "")
            key = window.getKeyPress()

            # # Si une touche a été pressée
            #if(key != ""):
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