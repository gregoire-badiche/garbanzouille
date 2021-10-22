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

