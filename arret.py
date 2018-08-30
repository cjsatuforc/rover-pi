print("Mise a zero des Pins");

import classRoverPi
import time

rover = classRoverPi.RoverPi(2,3,17,22,25,24,7,8)

rover.definitionSorties()
rover.stop
