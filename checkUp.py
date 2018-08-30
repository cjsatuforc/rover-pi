print("Lancement du check up RoverPi");

import FonctionsRoverPi as Rover

Rover.begin()

sorties = [2,3,17,22,25,24,7,8]

# Definition des sorties
Rover.definitionSorties(sorties)

# CheckUp Moteur
Rover.checkUpMoteur("Moteur Arriere Gauche", 4, 18)
Rover.checkUpMoteur("Moteur Arriere Droit", 17, 22)
Rover.checkUpMoteur("Moteur Avant Gauche", 25, 24)
Rover.checkUpMoteur("Moteur Avant Droit", 7, 8)
