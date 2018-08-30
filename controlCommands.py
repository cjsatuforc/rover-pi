print("Lancement du control du RoverPi");

import classRoverPi
import time
from Tkinter import *

rover = classRoverPi.RoverPi(2,3,17,22,25,24,7,8)
rover.definitionSorties()
rover.stop()

menu = True

while menu:
    command = raw_input(" > ")

    if command == "stop":
        rover.stop()
    elif command == "avancer":
        rover.avancer()
    elif command == "reculer":
        rover.reculer()
    elif command == "adroite":
        rover.avancerDroite()
    elif command == "agauche":
        rover.avancerGauche()
    elif command == "droite":
        rover.droite()
    elif command == "gauche":
        rover.gauche()
    elif command == "rdroite":
        rover.reculerDroite()
    elif command == "rgauche":
        rover.reculerGauche()
    elif command == "checkUp":
        rover.checkUp();
    elif command == "exit":
        menu = False
    else:
        print("Commande inconnue")
