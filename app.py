"""
Fichier principal du jeu

Import des librairies
"""

# Pour limiter la main loop
import time

# Pour effectuer des commandes comme clear / cls (efface la console) ou pour redimmentionner le terminal
import os

#Pour la gestion des modules
import sys

# Import du module pour gérer le cross-platform
import modules.window.window as window

"""
Importe tous les objets du code (on fait de la POO ici ou quoi)
Ces objets doivent être enregistrés dans le dossier "objets", avec l'extension .py. Ils seront automatiquement détectés et importés.
"""


sys.path.append('objets')
for i in sorted(os.listdir('objets')):
    if not i.startswith('_'):
        exec('from objets.%s import *' %(i[:-3]))
        print('imported %s' %(i))

        
# Si l'OS et Python sont prêt à lancer le jeu
if __name__ == "__main__":
    # On redimentionne la console
    window.resize(54, 22)
    # On crée une nouvelle partie
    game = Game()

#test :D
