print("Chargement du programme de control du RoverPi...");

import classRoverPi
import time
import pygame
from pygame.locals import *

rover = classRoverPi.RoverPi(2,3,17,22,25,24,7,8)
rover.definitionSorties()
rover.stop()

pygame.init()
menu = True

print("Chargement termine !")
