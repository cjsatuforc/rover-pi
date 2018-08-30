import RPi.GPIO as GPIO
import time

class RoverPi:
    def __init__(self, pinM1A, pinM1B, pinM2A, pinM2B, pinM3A, pinM3B, pinM4A, pinM4B):
        print("Instantiation du Rover")

        # Verification de la version
    	print("Version GPIO: "+GPIO.VERSION)

    	# Desactivation des warnings
    	GPIO.setwarnings(False)

    	# Mise en place des GPIO selon le numerotage de la board
    	GPIO.setmode(GPIO.BCM)

        # Enregistrement des pins
        self.pinM1A = pinM1A
        self.pinM1B = pinM1B
        self.pinM2A = pinM2A
        self.pinM2B = pinM2B
        self.pinM3A = pinM3A
        self.pinM3B = pinM3B
        self.pinM4A = pinM4A
        self.pinM4B = pinM4B

    def definitionSorties(self):
        print("Definition des pins")
    	GPIO.setup(self.pinM1A,GPIO.OUT)
        GPIO.setup(self.pinM1B,GPIO.OUT)
        GPIO.setup(self.pinM2A,GPIO.OUT)
        GPIO.setup(self.pinM2B,GPIO.OUT)
        GPIO.setup(self.pinM3A,GPIO.OUT)
        GPIO.setup(self.pinM3B,GPIO.OUT)
        GPIO.setup(self.pinM4A,GPIO.OUT)
        GPIO.setup(self.pinM4B,GPIO.OUT)

    def checkUp(self, temps=2):
        print("Check up des moteurs")
        self.checkUpMoteur("Moteur Arriere Gauche", self.pinM1A, self.pinM1B, temps)
        self.checkUpMoteur("Moteur Arriere Droit", self.pinM2A, self.pinM2B, temps)
        self.checkUpMoteur("Moteur Avant Gauche", self.pinM3A, self.pinM3B, temps)
        self.checkUpMoteur("Moteur Avant Droit", self.pinM4A, self.pinM4B, temps)

    def checkUpMoteur(self, nomMoteur, pinA, pinB, temps):
    	print("Moteur "+nomMoteur+" : En avant")
    	self.avancerMoteur(pinA, pinB)
    	time.sleep(temps)
    	print("Moteur "+nomMoteur+" : En arriere")
    	self.reculerMoteur(pinA, pinB)
    	time.sleep(temps)
    	print("Moteur "+nomMoteur+" : Stop")
    	self.stopMoteur(pinA, pinB)

    def avancerMoteur(self, pinA, pinB):
        GPIO.output(pinA,True)
    	GPIO.output(pinB,False)

    def reculerMoteur(self, pinA, pinB):
        GPIO.output(pinA,False)
    	GPIO.output(pinB,True)

    def stopMoteur(self, pinA, pinB):
        GPIO.output(pinA,False)
    	GPIO.output(pinB,False)

    def avancer(self, temps=0):
        print("Avant")
        self.avancerMoteur(self.pinM1A, self.pinM1B)
        self.avancerMoteur(self.pinM2A, self.pinM2B)
        self.avancerMoteur(self.pinM3A, self.pinM3B)
        self.avancerMoteur(self.pinM4A, self.pinM4B)
        if temps > 0:
            time.sleep(temps)
            self.stop()

    def reculer(self, temps=0):
        print("Avant")
        self.reculerMoteur(self.pinM1A, self.pinM1B)
        self.reculerMoteur(self.pinM2A, self.pinM2B)
        self.reculerMoteur(self.pinM3A, self.pinM3B)
        self.reculerMoteur(self.pinM4A, self.pinM4B)
        if temps > 0:
            time.sleep(temps)
            self.stop()

    def stop(self):
        print("Stop")
        self.stopMoteur(self.pinM1A, self.pinM1B)
        self.stopMoteur(self.pinM2A, self.pinM2B)
        self.stopMoteur(self.pinM3A, self.pinM3B)
        self.stopMoteur(self.pinM4A, self.pinM4B)

    def avancerDroite(self, temps=0):
        print("Avancer a Droite")
        self.avancerMoteur(self.pinM1A, self.pinM1B)
        self.avancerMoteur(self.pinM3A, self.pinM3B)
        self.stopMoteur(self.pinM2A, self.pinM2B)
        self.stopMoteur(self.pinM4A, self.pinM4B)
        if temps > 0:
            time.sleep(temps)
            self.stop()

    def avancerGauche(self, temps=0):
        print("Avancer a Gauche")
        self.avancerMoteur(self.pinM2A, self.pinM2B)
        self.avancerMoteur(self.pinM4A, self.pinM4B)
        self.stopMoteur(self.pinM1A, self.pinM1B)
        self.stopMoteur(self.pinM3A, self.pinM3B)
        if temps > 0:
            time.sleep(temps)
            self.stop()

    def droite(self, temps=0):
        print("Pivoter a Droite")
        self.avancerMoteur(self.pinM1A, self.pinM1B)
        self.reculerMoteur(self.pinM2A, self.pinM2B)
        self.avancerMoteur(self.pinM3A, self.pinM3B)
        self.reculerMoteur(self.pinM4A, self.pinM4B)
        if temps > 0:
            time.sleep(temps)
            self.stop()

    def gauche(self, temps=0):
        print("Pivoter a Gauche")
        self.reculerMoteur(self.pinM1A, self.pinM1B)
        self.avancerMoteur(self.pinM2A, self.pinM2B)
        self.reculerMoteur(self.pinM3A, self.pinM3B)
        self.avancerMoteur(self.pinM4A, self.pinM4B)
        if temps > 0:
            time.sleep(temps)
            self.stop()

    def reculerDroite(self, temps=0):
        print("reculer a Droite")
        self.reculerMoteur(self.pinM1A, self.pinM1B)
        self.reculerMoteur(self.pinM3A, self.pinM3B)
        self.stopMoteur(self.pinM2A, self.pinM2B)
        self.stopMoteur(self.pinM4A, self.pinM4B)
        if temps > 0:
            time.sleep(temps)
            self.stop()

    def reculerGauche(self, temps=0):
        print("reculer a Gauche")
        self.reculerMoteur(self.pinM2A, self.pinM2B)
        self.reculerMoteur(self.pinM4A, self.pinM4B)
        self.stopMoteur(self.pinM1A, self.pinM1B)
        self.stopMoteur(self.pinM3A, self.pinM3B)
        if temps > 0:
            time.sleep(temps)
            self.stop()
