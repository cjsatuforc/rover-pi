print("Lancement du control du RoverPi");

import classRoverPi
import time
from Tkinter import *

rover = classRoverPi.RoverPi(2,3,17,22,25,24,7,8)
rover.definitionSorties()
rover.stop()

rover.avancer(1)
rover.droite(2)
rover.avancer(1)
rover.reculer(2)
rover.avancer(1)
rover.gauche(2)
rover.reculer(1)
